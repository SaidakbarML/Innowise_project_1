# 1 creating database class to connect and close database 

from src.config import load_config, DbConfig
from contextlib import contextmanager
import psycopg2
import logging

logger = logging.getLogger(__name__)



class Database:
    def __init__(self,config:DbConfig):
        self._conf = config
        self._conn = None

    def connect(self): # makes new connection using config
        try:
            self._conn=psycopg2.connect(
                database=self._conf.name,
                user = self._conf.user,
                password = self._conf.password,
                host = self._conf.host,
                port = self._conf.port
            )
            logger.info('connected to the database succesfuly')
            return self._conn
        except Exception as e:
            logger.error('connection failed: %s',e)
            raise e

    def close(self):
        self._conn.close()
#connect to db and automatically commit and close if error rollback
    @contextmanager 
    def connection(self):
        conn = self.connect()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    # run one query and return rows as dict if there is any
    def run(self,raw_sql,params=None):
        with self.connection() as conn:
            curr = conn.cursor()
            curr.execute(raw_sql,params)
            logger.info('Executed query: %s',raw_sql)
            if curr.description:
                columns = [d[0] for d in curr.description]
                return [dict(zip(columns,row)) for row in curr.fetchall()]
            
            return None
    # this method used for inserting many rows at once
    def run_many(self,raw_sql,rows):
        with self.connection() as conn:
            curr = conn.cursor()
            curr.executemany(raw_sql,rows)