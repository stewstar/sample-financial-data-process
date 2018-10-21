# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:16:43 2018

@author: steven
"""
import pandas as pd

def get_stock_name_from_path(path):
    '''
    extract stock name from provided path assuming the file name is stock name.
    '''
    return path.split('/')[-1].split('.')[0]
        
    
def get_df_from_csv(file_path):
    stock_df = pd.read_csv(file_path)
    # print(stock_df)
    return stock_df.head(5)


def format_df_col(df, stock_symbol):
    '''
    prepare columns for data insertion:
        1. make sure the column names are correct
        2. convert pricing_date to datetime format
        3. add stock symbol
        4. update created_at datetime
    '''
    df.columns = ['pricing_date', 'open', 'high', 'low', 'close', 'volumn']
    df['pricing_date'] = pd.to_datetime(df['pricing_date'], 
      format="%m/%d/%Y 0:00")
    df['stock_symbol'] = stock_symbol
    
    df = df.assign(created_at=pd.Timestamp.now())
    df['created_at'] = pd.to_datetime(df['created_at'])
    return(df)


def extract_header_and_content(file_path):
    return format_df_col(
            get_df_from_csv(file_path), 
            get_stock_name_from_path(file_path)
        )

#df = get_df_from_csv("../../data/SZ000002.csv")