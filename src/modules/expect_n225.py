from get_price import get_price

#日経225の売買判断する関数

def expect_n225():
    #get_priceを使って、証券番号から過去の株価をdfで取得
    stock_id = "1330"
    df_price = get_price(stock_id)

    #NYダウの分析結果を取得（評価）
    res_dji = analyse_dji()

    #x_NはN日前の終値
    x_1 = df_price.iloc[0,3]
    x_2 = df_price.iloc[0,2]

    #買い注文を入れるか判断する
    #1日前の株価が2日前の株価より10円以上高いなら終値+10円で買付
    if x_1 > x_2 + 10:
        buy_flg = 1
        buy_price = x_1 +10
    elif res_dji == 0:
        buy_flg = 0
        buy_price = 0
    else:
        buy_flg = 0
        buy_price = 0 #買いの指値を0円にすれば、万一、誤発注しても約定しないのでセーフ

    #[買フラグ,証券番号,買値]のリストjudgementを返す
    expectation = [buy_flg,stock_id,buy_price]
    print(expectation)
    
    return expectation


#過去のダウをみて、いい感じなら1だめなら0を返す関数
def analyse_dji():
    #NYダウの取得
    dji = get_price("DJI")
    
    #x_NはN日前の終値
    x_1 = dji.iloc[0,3]
    x_2 = dji.iloc[0,2]
    
    #適当な比較
    if x_1 > x_2 + 10:
        res_dji = 1
    else:
        res_dji = 0
    return res_dji