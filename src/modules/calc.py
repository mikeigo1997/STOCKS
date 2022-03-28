from db.read_table import read_table

import pandas as pd
import time
import datetime

#証券番号から様々な手法で値を算出する関数群
stock_id = "1330"
date = ""

#ボリンジャーバンドを出力
def bollinger(stock_id):
    df = read_table(stock_id)
    df = df.sort_values(by="Date")

    bband = pd.DataFrame()
    bband['Close'] = df['Close']
    bband['Mean'] = df['Close'].rolling(window=2).mean()
    bband['Std'] = df['Close'].rolling(window=2).std()
    bband['Upper'] = bband['Mean'] + (bband['Std'] * 2)
    bband['Lower'] = bband['Mean'] - (bband['Std'] * 2)

    return bband

#移動平均を出力
def ma(stock_id):
    df = read_table(stock_id)
    df = df.sort_values(by="Date")
    
    ma = pd.DataFrame()
    ma['ma5'] = df['Close'].rolling(window=5).mean()
    ma['ma15'] = df['Close'].rolling(window=15).mean()
    ma['ma30'] = df['Close'].rolling(window=30).mean()

    return ma


#2パラメータを出力(リスト)
def param(stock_id):
    df = read_table(stock_id)
    df = df.sort_values(by="Date")
    
    mean = df['Close'].mean()
    std =  df['Close'].std()

    return [mean,std]


print(param(1330))