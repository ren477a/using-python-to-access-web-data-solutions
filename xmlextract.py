import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = input('Enter location:')
print('Retrieving ' + serviceurl)
#serviceurl = 'http://py4e-data.dr-chuck.net/comments_83451.xml'
data = urllib.request.urlopen(serviceurl).read()
print('Retrieved ' + str(len(data)) + ' characters')
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
print('Count: ' + str(len(comments)))
csum = 0
for comment in comments:
  csum += int(comment.find('count').text)
print('Sum: '+ str(csum))
