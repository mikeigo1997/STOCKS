import urllib.request
import json
import pprint

#セッティング情報を取得
import settings
Token = settings.Token


url = 'http://localhost:18080/kabusapi/board/5401@1'
req = urllib.request.Request(url, method='GET')
req.add_header('Content-Type', 'application/json')
req.add_header('X-API-KEY', Token)

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
