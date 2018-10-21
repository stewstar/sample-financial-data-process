# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 08:17:01 2018

@author: steven
"""

from data_extraction.from_csv import extract_header_and_content
from pgsql.pg_repository import init_data_for_table

def get_content_from_csv(file_path, table_name):
    '''
    get data from csv, insert to exsiting table and verify contents.
    '''
    df = extract_header_and_content(file_path)
    print(df)
    init_data_for_table(df, table_name)
    # df.to_sql(table_name, engine, if_exists='replace')
    #a = pd.read_sql_query('select * from ' + table_name, con=engine)
    #return(a)
    
    
get_content_from_csv('../data/SZ000002.csv', 'stock_price')