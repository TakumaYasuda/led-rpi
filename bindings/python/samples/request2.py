import requests
from bs4 import BeautifulSoup

response = requests.get('http://192.168.11.222/bottest.html')
print(response.status_code)    # HTTPのステータスコード取得
text = response.text    # レスポンスのHTMLを文字列で取得

text2  = BeautifulSoup(html)

print(text2)

