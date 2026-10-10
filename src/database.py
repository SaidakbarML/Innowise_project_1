# 1 creating database class to connect and close database 

from src.config import load_config, DbConfig
from contextlib import contextmanager
import psycopg2



class Database:
    def __init__(self,config:DbConfig):
        self._conf = config
        self._conn = None

    def connect(self):
        try:
            self._conn=psycopg2.connect(
                database=self._conf.name,
                user = self._conf.user,
                password = self._conf.password,
                host = self._conf.host,
                port = self._conf.port
            )
            print('connected to the database succesfuly')
            return self._conn
        except:
            raise "cant connect to the database "

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
    def run(self,raw_sql,params=None):
        with self.connection() as conn:
            curr = conn.cursor()
            curr.execute(raw_sql,params)
            print(f"Executed query: \n {raw_sql}")
            if curr.description:
                columns = [d[0] for d in curr.description]
                return [dict(zip(columns,row)) for row in curr.fetchall()]
            
            return None
    # this method used for inserting many rows at once
    def run_many(self,raw_sql,rows):
        with self.connection() as conn:
            curr = conn.cursor()
            curr.executemany(raw_sql,rows)