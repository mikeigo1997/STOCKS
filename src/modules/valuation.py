from .get_price import get_price

#証券番号から買付判断する関数

def buy_judge(stock_id):
    """
    引数の証券番号の銘柄について、判定結果を出力
    :param stock_id:
    :return:
    """
    #get_priceを使って、証券番号から過去の株価をdfで取得
    stock_id = stock_id
    df_price = get_price(stock_id)

    #x_NはN日前の終値
    x_1 = df_price.iloc[0,3]
    x_2 = df_price.iloc[0,2]

    #買い注文を入れるか判断する
    #1日前の株価が2日前の株価より10円以上高いなら終値+10円で買付
    if x_1 > x_2 + 10:
        buy_flg = 1
        buy_price = x_1 +10
    else:
        buy_flg = 0
        buy_price = 0 #買いの指値を0円にすれば、万一、誤発注しても約定しないのでセーフ

    #[買フラグ,証券番号,買値]のリストjudgementを返す
    judgement = [buy_flg,stock_id,buy_price]
    print(judgement)
    
    return judgement