# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:39:45 2018

@author: steven
"""
def create_database(db_command_func, *data):
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
        
    if not data:    
        db_command_func(conn.cursor())
    else:
        db_command_func(conn.cursor(),*data)
        
    conn.commit()
    conn.close()

def create_table_if_not_exist(cursor):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sz_stocks (
                        id SERIAL PRIMARY KEY,
                        stock_symbol VARCHAR(255) NOT NULL,
                        pricing_date TIMESTAMP NOT NULL, 
                        open  DECIMAL NOT NULL, 
                        high  DECIMAL NOT NULL, 
                        low  DECIMAL NOT NULL,
                        close  DECIMAL NOT NULL,
                        volume  DECIMAL NOT NULL,
                        created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ); """)
    #CURRENT_TIMESTAMP
    print ("Table create successful!")

