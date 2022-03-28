import pandas as pd
from common.CommonFunc import CommonFunc

class Models:

    def __init__(self, df_dict):
        self.df_dict = df_dict
        self.result = None

    def set_result(self):
        self.result = self.static_analysis(self.df_dict)

    @classmethod
    def static_analysis(cls, df_dict):
        res = {}
        for stock_code in df_dict.keys():
            print(stock_code)
            print(CommonFunc.calc_mean_variance(df_dict[stock_code]["Close"]))
            res[stock_code] = "買い"

        print(res)

        return res
