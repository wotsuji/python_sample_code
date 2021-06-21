
import urllib.request

# Target URL
target_url = 'https://example.co.jp/'

# URLデータ取得
try:
  response = urllib.request.urlopen(target_url)
except urllib.error.URLError as e:
  print(e.reason)
except urllib.error.HTTPError as e:
  print(e.reason)
content = response.read()
response.close()

# バイト列から文字列に変換
html = content.decode()

title = html.split('<title>')[1].split('</title')[0]
print(title)
