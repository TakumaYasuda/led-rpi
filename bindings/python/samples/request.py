import requests

response = requests.get('http://192.168.11.222/bottest.html')
print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得

