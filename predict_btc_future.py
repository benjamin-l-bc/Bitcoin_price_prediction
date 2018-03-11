# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:06:09 2018

@author: v-beshi
"""

import pyodbc
import pandas as pd



def get_agg_data():
    con=pyodbc.connect('DRIVER={SQL Server};SERVER=ServerName;DATABASE=DB;UID=ID;PWD=Password')
    raw_data=pd.read_sql('select * from dbo.BitcoinTradeHistory',con)
    raw_data['USDT_exceed']=raw_data['huobi_USDT']-raw_data['exchange_rate']

    pre_price15=[]
    for i in range(0,15):
        pre_price15.append(0)
    for i in range(15,len(raw_data)):
        pre_price15.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-15])/(raw_data['ok0330'][i-15]))
    pre_price15=pd.Series(pre_price15,name='pre_price15')

    pre_price10=[]
    for i in range(0,10):
        pre_price10.append(0)
    for i in range(10,len(raw_data)):
        pre_price10.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-10])/(raw_data['ok0330'][i-10]))
    pre_price10=pd.Series(pre_price10,name='pre_price10')

    pre_price5=[]
    for i in range(0,5):
        pre_price5.append(0)
    for i in range(5,len(raw_data)):
        pre_price5.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-5])/(raw_data['ok0330'][i-5]))
    pre_price5=pd.Series(pre_price5,name='pre_price5')

    next_price5=[]
    for i in range(0,len(raw_data)-5):
        next_price5.append((raw_data['ok0330'][i+5]-raw_data['ok0330'][i])/(raw_data['ok0330'][i]))
    for i in range(0,5):
        next_price5.append(0)
    next_price5=pd.Series(next_price5,name='next_price5')

    next_price10=[]
    for i in range(0,len(raw_data)-10):
        next_price10.append((raw_data['ok0330'][i+10]-raw_data['ok0330'][i])/(raw_data['ok0330'][i]))
    for i in range(0,10):
        next_price10.append(0)
    next_price10=pd.Series(next_price10,name='next_price10')   

    next_price15=[]
    for i in range(0,len(raw_data)-15):
        next_price15.append((raw_data['ok0330'][i+15]-raw_data['ok0330'][i])/(raw_data['ok0330'][i]))
    for i in range(0,15):
        next_price15.append(0)
    next_price15=pd.Series(next_price15,name='next_price15')

    pre_bfx=[0]
    for i in range(1,len(raw_data)):
        pre_bfx.append((raw_data['bfx_last_price'][i]-raw_data['bfx_last_price'][i-1])/(raw_data['bfx_last_price'][i-1]))
    pre_bfx=pd.Series(pre_bfx,name='pre_bfx')

    pre_news10=[]
    for i in range(0,10):
        pre_news10.append(0)
    for i in range(10,len(raw_data)):
        pre_news10.append((raw_data['news_emotion'][i]-raw_data['news_emotion'][i-10])/(raw_data['news_emotion'][i-10]))
    pre_news10=pd.Series(pre_news10,name='pre_news10')

    pre_8btc10=[]
    for i in range(0,10):
        pre_8btc10.append(0)
    for i in range(10,len(raw_data)):
        pre_8btc10.append((raw_data['8btc_emotion'][i]-raw_data['8btc_emotion'][i-10])/(raw_data['8btc_emotion'][i-10]))
    pre_8btc10=pd.Series(pre_8btc10,name='pre_8btc10')

    raw_data=raw_data.drop(['ok0330','DateTime','ok_thisweek','huobi_USDT','exchange_rate','bfx_last_price','news_emotion','8btc_emotion'],axis=1)
    agg_data=pd.concat([raw_data,pre_price15,pre_price10,pre_price5,pre_bfx,pre_news10,pre_8btc10,next_price5,next_price10,next_price15],axis=1)
    return(agg_data)