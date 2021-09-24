import sqlite3


class VData:
    cur=''
    con=''


    def __init__(self, db_name):
        global cur
        global con
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        # print('created database file!')


    def create_db(table):
        cur.execute('''CREATE TABLE stocks
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

    def insert_data(sql,vars):
        cur.execute(sql,vars)


    def disconnect():
        con.commit()
        con.close()



















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