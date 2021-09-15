import sqlite3

class VData:

    def __init__(self,db_name):
        self.dbname=db_name

    def create_db(self, db_name):
        con = sqlite3.connect(self.dbname)
        cur=con.cursor()

        # Create table
        cur.execute('''CREATE TABLE stocks
                       (date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        con.commit()

        # We can also close the connection if we are done with it.
        con.close()
        return 1

    def insert_data(db,table_name):
        return 1



