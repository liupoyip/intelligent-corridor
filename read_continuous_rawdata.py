import os
from datetime import datetime
import json
from typing import Optional

import mysql.connector
import mysql.connector.cursor
import pandas as pd


db = None
cursor: Optional[mysql.connector.cursor.MySQLCursor] = None
host = None
port = None
user = None
password = None
db_name = None
rawdata_table_name = None
headers = None
data_types = None
current_data: tuple = None
rawdata_table_name = None
cfg = None

target_dir = None
database_dir = None

uploader_cfg_path = 'cfg.json'
with open(uploader_cfg_path, 'r') as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']
db_name = cfg['machine']
rawdata_table_name = cfg['rawdata_table_name']
headers = cfg['headers']
task_name = cfg['task']

# def connect_to_server():
print('connect to mysql server...')
print(f'host : {host}:{port}')
print(f'user : {user}')
db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password)

# use_database():
sql = f'USE {db_name}'
print(f'execute SQL command: {sql}')
cursor = db.cursor()
cursor.execute(sql)

sql = f'Select * from {rawdata_table_name}'
rawdata_store = pd.read_sql(sql, db)
db.close()

print(rawdata_store)
# connect_to_server()
# use_database()

# dummy time range
time_format = '%Y%m%dT%H%M%S'
str_start_time = '20230710T145000'
str_end_time = '20230712T145100'
start_time = datetime.strptime(str_start_time, time_format)
end_time = datetime.strptime(str_end_time, time_format)
header_start_time = headers[1]
header_record_cfg_path = headers[2]

rawdata_store[header_start_time] = pd.to_datetime(
    rawdata_store[header_start_time])
time_mask = (rawdata_store[header_start_time] > start_time) & (
    rawdata_store[header_start_time] <= end_time)
print(time_mask)

masked_rawdata_store = rawdata_store.loc[time_mask]
print(masked_rawdata_store)
masked_rawdata_store = rawdata_store.loc[time_mask]
