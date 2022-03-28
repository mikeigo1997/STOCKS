from modules.valuation import buy_judge

#お気に入り銘柄リストを作成（二次元配列。企業名はメモ用）
stocks = [
    ["1925","大和ハウス"],
    ["2930","北の達人"],
    ["6268","ナブテスコ"],
    ["3319","GDO"]]



# 発注判断を実行                                                                                                                                                        
judgement = []

for i in stocks:
    judgement.append(buy_judge(i[0]))

print(judgement)

