from src.sql_parser import split_read,read_sql
from src.database import Database
from src.data_loader import load_json
import logging

logger = logging.getLogger(__name__)


class Repository:
    def __init__(self,db):
        self.db=db

    def create_schema(self):
        # drops and creates tables again
        self.db.run(read_sql('sql/schema.sql'))

    def create_index(self):
        self.db.run(read_sql('sql/indexes.sql'))
        
    def insert_rooms(self,rooms:load_json):
        rows = [(int(r['id']),r['name']) for r in rooms] # make tuples for insert
        self.db.run_many("INSERT INTO rooms (id, name) VALUES (%s, %s)",rows)
        logger.info('done inserting rooms')
    
    def insert_students(self,students:load_json):
        rows = [(r['birthday'],int(r['id']),str(r['name']),r['room'],r['sex']) for r in students]
        self.db.run_many("INSERT INTO students (birthday, id, name, room, sex) VALUES (%s,%s,%s,%s,%s)",rows=rows)
        logger.info('done inserting students')

    def fetch(self,query): # run select and return rows
        res=self.db.run(query)
        return res