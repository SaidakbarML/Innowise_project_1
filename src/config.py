import os
from dataclasses import dataclass
from dotenv import load_dotenv
from src.sql_parser import read_sql
# from src.sql_parser import drop_tables,room_schema,student_schema
# this load all variables inside .env
load_dotenv()


@dataclass
class DbConfig:
    name: str
    user:str
    password:str
    host : str
    port:int


@dataclass
class DataLoaderConf:
    drop_tables: str
    room_schema:str
    student_schema:str



def load_config() -> DbConfig:
    return DbConfig(
        name=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host=os.getenv('DB_HOST'),
        port=str(os.getenv('DB_PORT'))
    )



def load_queries():
    q1 = read_sql('sql/q1_num_students_eachroom.sql')
    q2 = read_sql('sql/q2_avg_age_eachroom.sql')
    q3 = read_sql('sql/q3_diff_age.sql')
    q4 = read_sql('sql/q4_list_different_room.sql')
    return q1,q2,q3,q4