# %%
import pymysql
# %%
db_settings = {
    "host": "140.134.76.145",
    "port": 3306,
    "user": "AIoTLab-MySQL",
    "password": "db309-1",
    "db": "test_schema",
    "charset": "utf8"
}

try:
    conn = pymysql.connect(**db_settings)
except Exception as ex:
    print(f'Error: {ex}')
