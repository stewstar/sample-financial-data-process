# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:56:48 2018

@author: steven
"""

# This file is just for demo basic knowledge, not for project to use.
# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# http://initd.org/psycopg/docs/usage.html
# http://www.postgresqltutorial.com/postgresql-python/create-tables/

import psycopg2
import io

def create_database(db_command_func, *data):
    try:
        conn = psycopg2.connect(dbname='study', 
                                user='quant', 
                                host='35.240.207.140', 
                                password='quant')
    except:
        print("Unable to connect to the database")
        
    if not data:    
        db_command_func(conn.cursor())
    else:
        db_command_func(conn.cursor(),*data)
        
    conn.commit()
    conn.close()


def create_table_if_not_exist(cursor):
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS stock_price (
                        index BIGINT PRIMARY KEY,
                        stock_symbol VARCHAR(255) NOT NULL,
                        pricing_date TIMESTAMP NOT NULL, 
                        open  DECIMAL NOT NULL, 
                        high  DECIMAL NOT NULL, 
                        low  DECIMAL NOT NULL,
                        close  DECIMAL NOT NULL,
                        volume  DECIMAL NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ); 
                   """)
    print ("Table create successful!")
    
    
def select_table_name(cursor):
    cursor.execute("""
                   SELECT table_schema, table_name 
                   FROM information_schema.tables
                   WHERE table_schema = 'public'
                   """)
    rows = cursor.fetchall()
    return rows


def insert_value(cursor, df):
    output = io.StringIO();
    # ignore the index
    df.to_csv(output, sep='\t',index = False, header = False);
    output.getvalue();
    # jump to start of stream
    output.seek(0);
    cursor.copy_from(output, 'sz_tocks', null='')
    print ("Data insert successful!")


def select_data(cursor,table_name):
    cursor.execute("""
                   SELECT COUNT(*) FOME table_name 
                   WHERE DATE(created_at) = TODAY()
                   """)
    rows = cursor.fetchall()
    return rows

