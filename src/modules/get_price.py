from pandas_datareader import data
from const import Const
import datetime
import re

def get_price(stock_code):
    """
    実行日前日までの日次データをDF形式で取得
    :param stock_code:(個別銘柄の証券コード or DJI or JPUS)
    :return: DF
      columns: Open    High     Low   Close   Volume
      index:   Date(2017-03-21~実行日の前日）
    """
    #取得対象期間を設定
    #start = datetime.datetime(2017,1,1)
    #end = datetime.datetime.now()

    #過去データを取得
    if stock_code == Const.CODE_DJI:
        df = data.DataReader('^DJI', 'stooq')
    elif stock_code == Const.CODE_JPUS:
        df = data.DataReader('DEXJPUS', 'fred')
    elif re.search(r'\d', stock_code): #数字を含む=日本株の証券番号
        df = data.DataReader(f'{stock_code}.JP', 'stooq')
    else:
        print("ERROR get_price: 引数が不正です")
        exit()

    return df