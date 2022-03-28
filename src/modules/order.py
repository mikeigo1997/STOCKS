import urllib.request
import json
import pprint

API_PWD = "Minamis5"

#APIトークンを取得する関数
#kabuステーションを起動していないと動作しないので注意
def get_API():
    obj = { 'APIPassword': API_PWD }
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:18080/kabusapi/token'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)
            token = content["Token"]
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
    finally:
        return token

#APIトークンを使って、指値で買付する関数
#引数は証券番号・数量・指値
def order(stock_id,quantity,price,expiredate):
    token = get_API()
    obj = { 'Password': API_PWD,
            'Symbol': stock_id, #証券番号
            'Exchange': 1,  #東証=1
            'SecurityType': 1, #株式=1
            'FrontOrderType': 20, #指値=20
            'Side': '2', #売=1,買=2
            'CashMargin': 1, #現物=1
            'DelivType': 2, #譲渡区分（不明）現物売は0
            'FundType': 'AA', #信用代用=AA 現物売りは"  "
            
            'AccountType': 4, #特定口座=4
            'Qty': quantity,
            'Price': price,
            'ExpireDay': expiredate } #注文有効期限 yyyyMMdd形式
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:18080/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', token)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

order("1925",100,3500)