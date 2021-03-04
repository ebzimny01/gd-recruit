import sqlite3
from sqlite3 import Error

def create_DB(name):
    database = name
    conn = create_connection(database)

    sql_create_recruits_table = """ CREATE TABLE IF NOT EXISTS recruits (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        pos TEXT,
                                        height TEXT,
                                        weight INTEGER,
                                        rating INTEGER,
                                        rank INTEGER,
                                        hometown TEXT,
                                        miles INTEGER,
                                        considering TEXT,
                                        ath INTEGER,
                                        spd INTEGER,
                                        dur INTEGER,
                                        we INTEGER,
                                        sta INTEGER,
                                        str INTEGER,
                                        blk INTEGER,
                                        tkl INTEGER,
                                        han INTEGER,
                                        gi INTEGER,
                                        elu INTEGER,
                                        tec INTEGER,
                                        tot INTEGER,
                                        gpa REAL,
                                        pot TEXT
                                    ); """

    if conn is not None:
        # create recruits table
        create_table(conn, sql_create_recruits_table)
        return conn
    else:
        print("Error! cannot create the database connection.")


def create_connection(database):
    """
    create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)