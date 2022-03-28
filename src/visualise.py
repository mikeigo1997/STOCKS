import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from modules.get_price import get_price


#日経225とNYダウを表示する

#日経225とNYダウを取得
N225 = get_price("1330")
DJI = get_price("DJI")
JPUS = get_price("JPUS")

#終値のカラムをリネーム
N225["N225"] = N225["Close"]
DJI["DJI"] = DJI["Close"]
JPUS["JPUS"] = JPUS["DEXJPUS"]

#dfをマージ
zz = pd.merge(N225, DJI, left_index=True, right_index=True)
z = pd.merge(zz,JPUS,left_index=True, right_index=True)

#グラフ設定
fig = go.Figure()

#fig.add_trace(go.Scatter(x=z.index, y=z["N225"], mode='lines', name="Nikkei225"))
#fig.add_trace(go.Scatter(x=z.index, y=z["DJI"], mode='lines', name="DJI"))
fig.add_trace(go.Scatter(x=z.index, y=z["JPUS"], mode='lines', name="JPUS"))

fig.show()

#print(z)