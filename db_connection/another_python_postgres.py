import psycopg2


conn = pg.connect(
         host='<ip>>',
         database='<dbanme>',
         username='<username>',
         password='<pass>'
         )

SQLselect=  '''
            select *
            from python.users;
            '''
for database in databases:
    cur=conn.cursor('database')
    call=cur.execute(SQLselect.format(database))
    rows=cur.fetchall
    cols=[desc[0] for desc in cur.description]
    temp = pd.DataFrame(rows, columns=cols