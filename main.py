from src.database import Database
from src.config import load_config
from src.repository import Repository
from src.data_loader import load_json

rep = Repository('none')

rep.create_schema()
rep.insert_rooms(load_json('data/rooms.json'))
rep.insert_students(load_json('data/students.json'))

rep.fetch('select * from students')
