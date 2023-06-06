import psycopg2
import time

start_time = time.time()

before_connect = time.time()
conn = psycopg2.connect(database="<dbname>",
                        host="<ip>",
                        user="<user>",
                        password="<pass>",
                        port="<port>")



after_connect = time.time()

before_cursor = time.time()
cursor = conn.cursor()
after_cursor = time.time()

before_sql_execution = time.time()

cursor.execute("SELECT id,name,gender,department FROM python.users;")

after_sql_execution = time.time()

before_fetchall = time.time()

print(cursor.fetchall())

after_fetchall = time.time()

before_close = time.time()

conn.close()

after_close = time.time()

elapsed_time = time.time() - start_time
connect_time = before_connect - after_connect
cursor_time= before_cursor - after_cursor
sql_execution_time = before_sql_execution - after_sql_execution
fetchall_time = before_fetchall - after_fetchall
close_time = before_close- after_close

print('It took {} seconds to connect'.format(connect_time))
print('It took {} seconds to cursor'.format(cursor_time))
print('It took {} seconds to execute sql'.format(sql_execution_time))
print('It took {} seconds to fetchall'.format(fetchall_time))
print('It took {} seconds to close'.format(close_time))
print('It took {} seconds to run your code in total'.format(elapsed_time))
#
# export DSN="dbname=mydb host=localhost port=5432 user=myuser password=xxx"
# time python -c "import os, psycopg2; print psycopg2.connect(os.environ['DSN'])"
# time psql -c "" "$DSN"

