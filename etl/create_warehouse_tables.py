import sqlite3

db_file='enterprise.db'
sql_file='sql/warehouse_tables.sql'

def create_tables():

    conn=sqlite3.connect(db_file)
    cur=conn.cursor()
    
    with open (sql_file,"r") as f:
        sql_script=f.read()

    cur.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Warehouse tables created successfully")
if __name__ == "__main__":
    create_tables()