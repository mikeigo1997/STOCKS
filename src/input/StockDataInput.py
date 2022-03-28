import pandas as pd
import numpy as np
from pandas_datareader import data
from common.const import Const
import datetime
import re
import os

class StockDataInput:
    stock_code :str

    df_past_price = None

    @classmethod
    def set_data(cls, stock_code_dict):

        print("INFO start set_data")

        df_dict = {}
        for stock_code in stock_code_dict.keys():
            if os.path.isfile(f"./data/{stock_code}.csv"):
                df_dict[stock_code] = cls.read_csv(stock_code)
            else:
                df_dict[stock_code] = cls.get_price(stock_code)

        print("INFO end set_data")

        return df_dict

    @classmethod
    def read_csv(cls, stock_code):
        print(">>" + stock_code + " done")
        return pd.read_csv(f"./data/{stock_code}.csv")

    @classmethod
    def get_price(cls, stock_code):
        """
        実行日前日までの日次データをDF形式で取得
        :param stock_code:(個別銘柄の証券コード or DJI or JPUS)
        :return: DF

          columns: Open    High     Low   Close   Volume
          index:   Date(2017-03-21~実行日の前日）
        """
        # 取得対象期間を設定
        # start = datetime.datetime(2017,1,1)
        # end = datetime.datetime.now()

        # 過去データを取得
        if stock_code == Const.CODE_DJI:
            df = data.DataReader('^DJI', 'stooq')
        elif stock_code == Const.CODE_JPUS:
            df = data.DataReader('DEXJPUS', 'fred')
        elif re.search(r'\d', stock_code):  # 数字を含む=日本株の証券番号
            df = data.DataReader(f'{stock_code}.JP', 'stooq')
        else:
            print("ERROR get_price: 引数が不正です")
            exit()

        print(">>" + stock_code + " done")
        df["date"] = df.index
        df.to_csv(f"./data/{stock_code}.csv", index=False)

        return df


