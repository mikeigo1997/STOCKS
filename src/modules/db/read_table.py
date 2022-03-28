import sqlite3
import pandas as pd

#テーブル名を指定してSQLiteからdfを作成
def read_table(stock_id):
    #テーブル名・DB名を指定
    t_name = f"T{stock_id}"
    dbname = r"C:\Users\lovep\Desktop\work\kabu\src\modules\db\stock.db"
    
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    df=pd.read_sql_query(f'SELECT * FROM {t_name}', conn)
    
    cur.close()
    conn.close()

    return df

print(read_table("1330"))