import sqlite3

conn=sqlite3.connect('enterprise.db')
cur=conn.cursor()

print('\nCustomers:')
for row in cur.execute("select * from dim_customer"):
    print(row)

print('\nProducts:')
for row in cur.execute("select * from dim_product"):
    print(row)

print('\nsales:')
for row in cur.execute("select * from dim_sale"):
    print(row)

print('\nDate:')
for row in cur.execute("select * from dim_date"):
    print(row)

conn.close()
