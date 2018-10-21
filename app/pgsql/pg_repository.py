# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:39:45 2018

@author: steven
"""

import pandas as pd

def create_engine(env='prod'):
    if env == 'prod':
        eng = create_engine('postgresql://quant:quant@35.240.207.140:5432/study')
    else:
        eng = create_engine('postgresql://quant:quant@localhost:5432/study')
    print(eng)
    return(eng)
    

def insert_data(data, table_name, engine, new_table=False):
    '''
    select new_table will replace the existing table, be aware.
    data is dataframe from pandas
    '''
    if new_table:
        data.to_sql(table_name, engine, if_exists='replace')
    else: 
        data.to_sql(table_name, engine, if_exists='append')


def fetch_data(table_name, engine):
    pd.read_sql_query('select * from ' + table_name, con=engine)
    
def init_data_for_table(data, table_name, env='prod'):
    '''
    use given env create/replace the table and verify inserted data.
    '''
    eng = create_engine()
    insert_data(data, table_name, eng, new_table=True)
    verify_df = fetch_data(table_name, eng)
    print(verify_df.head(10))
        