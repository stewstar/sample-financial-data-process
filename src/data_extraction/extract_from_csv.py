# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:16:43 2018

@author: steven
"""
import pandas as pd
from sqlalchemy import create_engine

def get_content_from_csv(file_path):
    engine = create_engine('postgresql://quant:quant@35.240.207.140:5432/study')
    print(engine)
    df = format_df_col(get_df_from_csv(file_path))
    #df.to_sql('data_test', engine, if_exists='replace')
    a = pd.read_sql_query('select * from data_test',con=engine)
    return(a)
    
    
def get_df_from_csv(file_path):
    stock_df = pd.read_csv(file_path)
    # print(stock_df)
    return stock_df.head(5)


def format_df_col(df):
    '''
    prepare columns for data insertion
    '''
    df.columns = ['pricing_date', 'open', 'high', 'low', 'close', 'vol']
    df['pricing_date'] = pd.to_datetime(df['pricing_date'], 
      format="%m/%d/%Y 0:00")
    
    df = df.assign(created_at=pd.Timestamp.now())
    df['created_at'] = pd.to_datetime(df['created_at'])
    return(df)

df2 = get_content_from_csv("../../data/SZ000002.csv")

#df = get_df_from_csv("../../data/SZ000002.csv")