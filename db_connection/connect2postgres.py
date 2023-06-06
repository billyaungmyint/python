import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text
import time

start_time = time.time()

before_engine = time.time()
engine = create_engine('postgresql://<username>>:<pass>@<hostname>/<dbname>')
after_engine = time.time()
#connection = engine.connect()

# df = pd.read_sql("select * from users;" , con=engine)
# print(df)
before_connect = time.time()
# with engine.connect() as connection:
#     result = connection.execute(text("select id , name , gender , department from python.users"))
#     for row in result:
#         print(row)
connection = engine.connect()
after_connect = time.time()

before_readsql = time.time()
df = pd.read_sql("select * from python.users;" , con=engine)

after_readsql = time.time()
print(df)

before_close = time.time()
connection.close()
after_close = time.time()

after_time = time.time()

engine_time = before_engine - after_engine
connect_time = before_connect - after_connect
readsql_time = before_readsql - after_readsql
close_time = before_close - after_close
elapsed_time = time.time() - start_time

print('It took {} seconds to create engine'.format(engine_time))
print('It took {} seconds to connect'.format(connect_time))
print('It took {} seconds to read sql'.format(readsql_time))
print('It took {} seconds to close'.format(close_time))
print('It took {} seconds to run your code in total'.format(elapsed_time))
