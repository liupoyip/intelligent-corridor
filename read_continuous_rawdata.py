import os
import time
import json

import mysql.connector
import mysql.connector.cursor
from typing import Optional


class MySQLRawdataReader:

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

    def __init__(self, cfg):
        self.read_cfg()

    def read_cfg(self):
        self.host = cfg['host']
        self.port = cfg['port']
        self.user = cfg['user']
        self.password = cfg['password']
        self.db_name = cfg['machine']
        self.rawdata_table_name = cfg['rawdata_table_name']
        self.headers = cfg['headers']
        self.task_name = cfg['task']

    def connect_to_server(self):
        print('connect to mysql server...')
        print(f'host : {self.host}:{self.port}')
        print(f'user : {self.user}')
        self.db = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password)

    def use_database(self):
        print(f'execute SQL command: {sql}')
        sql = f'USE {self.db_name}'
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)


uploader_cfg_path = 'cfg.json'
with open(uploader_cfg_path, 'r') as file:
    cfg = json.load(file)
rawdata_reader = MySQLRawdataReader(cfg=cfg)
rawdata_reader.connect_to_server()
rawdata_reader.use_database()
