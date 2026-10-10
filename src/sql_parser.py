from pathlib import Path
import os
from pathlib import Path
def read_sql(path):
    return Path(path).read_text()


def split_read(sql_str:str,splitter:str,num:int):
    return sql_str.split(splitter)[num]    









