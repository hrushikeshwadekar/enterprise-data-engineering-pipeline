import sqlite3

conn=sqlite3.connect('enterprise.db')

cur=conn.cursor()
for row in cur.execute("select * from fact_sales"):
    print(row)

conn.close()