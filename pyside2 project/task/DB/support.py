import sqlite3
import sys
import traceback
import os

in_conn = sqlite3.connect(":memory:" )
path = os.getcwd()
path2 = os.path.join(path, "inmemory_db.db")
print(path2)
defaultdb_conn = sqlite3.connect(path2)


def get_backup():
    try:
        # qry = "create table emp2( name varchar(50), age int(50), adde varchar(50), mobile_no int);"
        qry2 = "select * from emp2"
        qry3 = "insert into emp2 values('harsh',25,'usaiudhg',35646)"

        defaultdb_cur = defaultdb_conn.cursor()
        # defaultdb_cur.execute(qry)

        defaultdb_cur.execute(qry3)

        defaultdb_cur.execute(qry2)
        result = defaultdb_cur.fetchall()
        print(result)

        defaultdb_conn.backup(in_conn)


        # in_conn.backup(defaultdb_conn)

    except:
        print(traceback.print_exc())



def check_conn():
    defaultdb_conn.cursor()
    in_conn.cursor()

    if in_conn:
        print("connect")
        # create_tab()

    else:
        print("not connect")


def create_tab():
    try:
        defaultdb_conn.cursor()
        cur = in_conn.cursor()
        qry = "create table emp2( name varchar(50), age int(50), adde varchar(50), mobile_no int);"
        cur.execute(qry)
        in_conn.commit()
        print("table created successfully")

    except:
        print(traceback.print_exc())



def display_data():
    try:
        defaultdb_conn.cursor()
        cur = in_conn.cursor()
        qry = "select * from emp2;"
        cur.execute(qry)
        result = cur.fetchall()


        return result
    except:
        print(traceback.print_exc())

def insert_data(name,age,city,mobile):
    try:
        defaultdb_conn.cursor()
        cur = in_conn.cursor()
        ins_qry = "insert into emp2 values(?,?,?,?);"
        sel_query = "select mobile_no from emp2 where mobile_no= ?"
        cur.execute(ins_qry, (name, age, city, mobile))

        # if :
        #     print("already inserted")
        # else:
        #     cur.execute(ins_qry, (name,age,city,mobile))

        print("insert data successfully")

    except:
        print(traceback.print_exc())