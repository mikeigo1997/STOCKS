from input.StockDataInput  import StockDataInput
from models.Models import Models

class StockAnalyzer:

    # 今後は引数で渡す
    stock_code_dict = {
        "1925": "大和ハウス",
        "2930": "北の達人",
        "6268": "ナブテスコ",
        "3319": "GDO"
        }

    # main
    def run(self):

        df_dict = StockDataInput.set_data(self.stock_code_dict)
        models  = Models(df_dict)


        # models.set_result()
        # print("ここまで完了")
        print(models.result)




if __name__ == "__main__":

    stock_analyzer = StockAnalyzer()

    print("INFO stock_analyzerを実行します")
    stock_analyzer.run()