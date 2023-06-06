#!/usr/bin/python
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import sys
import time

start_time = time.time()

def main():
	conn_string = "host='<hostname>' dbname='<dbname>' user='<username>' password='<pass>'"
	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (conn_string))

	conn = psycopg2.connect(conn_string)

	# HERE IS THE IMPORTANT PART, by specifying a name for the cursor
	# psycopg2 creates a server-side cursor, which prevents all of the
	# records from being downloaded at once from the server.
	cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute('SELECT * FROM python.users LIMIT 1000;')

	# Because cursor objects are iterable we can just call 'for - in' on
	# the cursor object and the cursor will automatically advance itself
	# each iteration.
	# This loop should run 1000 times, assuming there are at least 1000
	# records in 'my_table'
	row_count = 0
	for row in cursor:
		row_count += 1
		print("row: %s    %s\n" % (row_count, row))

if __name__ == "__main__":
	main()
	elapsed_time = time.time() - start_time
	print('It took {} seconds to run your code'.format(elapsed_time))