import sqlite3
import sqlite_db

class VData:

    def __init__(self, db_name):
        self.dbname = db_name

        self.con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        # print('created database file!')


    def create_db(self,table):
        self.cur.execute('''CREATE TABLE stocks
        #                (date text, trans text, symbol text, qty real, price real)''')

        #

        #
        # # Insert a row of data
        # cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        #
        # # Save (commit) the changes
        # con.commit()
        #
        # # We can also close the connection if we are done with it.
        # con.close()
        # return 1

    def insert_data(self, table_name, data):
        sql="INSERT INTO "+table_name+" VALUES ( "+data +" )"
        self.cur.execute(sql)
        self.con.commit()

    def disconnect(self):
        self.con.close()



















# create table cnnvd
# (
#     id               integer not null,
#     dbtype              text,
#     datatype      text,
#     dataformat    text,
#     dta
#     name             text,
#     vulid            text,
#     published        text,
#     modified         text,
#     source           text,
#     severity         text,
#     vultype          text,
#     thrtype          text,
#     vulconfigurationTid text,
#     vulconfoperator text,
#     vulswlistTid        text,
#     vuldescript      text,
#     vulexploit       text,
#     cveid            text,
#     bugtrq           text,
#     vulsolution      text,
#     refsTid             text
# );
#
# create table vulconfsw
# (
#     vulid text,
#     software text,
#     soperator text
# );
#
# create table vulconfterrace
# (
#   vulid text,
#   terrace text,
#   toperator text
# );
#
# create table refs
# (
#   refsid    text,
#   source    text,
#   name  text,
#   url   text,
#     tag text
# );
#
# create table swlist
# (
#   vulswid   text,
#   product   text
# );