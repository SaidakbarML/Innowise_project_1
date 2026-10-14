from pathlib import Path
import os
from pathlib import Path
def read_sql(path): # read sql file as text
    return Path(path).read_text()


# splits text by splitter and gives one part (not used now)
def split_read(sql_str:str,splitter:str,num:int):
    return sql_str.split(splitter)[num]    









