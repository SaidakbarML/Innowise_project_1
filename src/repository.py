from src.sql_parser import split_read,read_sql
from src.database import Database
from src.data_loader import load_json
from src.config import load_config
db = Database(load_config())


class Repository:
    def __init__(self,query:str):
        self.query=query

    
    def create_schema(self):
        db.run(read_sql('sql/schema.sql'))

    def insert_rooms(self,rooms:load_json):
        rows = [(int(r['id']),r['name']) for r in rooms]
        db.run_many("INSERT INTO rooms (id, name) VALUES (%s, %s)",rows)
        print('done inserting rooms')
    
    def insert_students(self,students:load_json):
        rows = [(r['birthday'],int(r['id']),str(r['name']),r['room'],r['sex']) for r in students]
        db.run_many("INSERT INTO students (birthday, id, name, room, sex) VALUES (%s,%s,%s,%s,%s)",rows=rows)
        print('done inserting students')
    def fetch(self,query):
        res=db.run(query)
        print(res)
        return res