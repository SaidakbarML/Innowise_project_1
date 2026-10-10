import os
from dataclasses import dataclass
from dotenv import load_dotenv
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

def dataloaderconf() -> DataLoaderConf:
    return DataLoaderConf(
        drop_tables=drop_tables,
        room_schema=room_schema,
        student_schema=student_schema

    )

