import sqlite3
import pandas as pd

#csvファイル名を指定して、stock.dbにテーブルを作成
#テーブル名はT+ファイル名をつける
f_name = "2930"
t_name = f"T{f_name}"

#csvファイルを読み込む
df = pd.read_csv(f"data/{f_name}.csv")

# カラム名を作成。
df.columns = ['Date','Open','High','Low','Close','Volume']

dbname = 'stock.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# テーブル名を指定して、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
df.to_sql(f'{t_name}', conn, if_exists='replace')

# 作成したデータベースを1行ずつ見る
select_sql = f'SELECT * FROM {t_name}'
for row in cur.execute(select_sql):
    print(row)

cur.close()
conn.close()