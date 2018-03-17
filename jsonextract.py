import json
import urllib.request, urllib.parse

url = input('Enter url:')
print('Retrieving', url)
conn = urllib.request.urlopen(url)
data = conn.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
comments = js['comments']
print('Count:', len(comments))
csum = 0
for comment in comments:
  csum += int(comment['count'])
print('Sum:', csum)
