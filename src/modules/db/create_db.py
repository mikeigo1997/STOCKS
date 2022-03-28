import sqlite3

# stock.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = 'stock.db'
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる。(必須)
conn.close()