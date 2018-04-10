import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i']         = content
data['from']      = 'AUTO'
data['to']        = 'AUTO'
data['smartresult'] = 'dict'
data['client']    = 'fanyideskweb'
data['salt']      = '1523259845567'
data['sign']      = '5e74a770f46956fc4db664cd703c4e20'
data['doctype']   = 'json'
data['version']   = '2.1'
data['keyfrom']   = 'fanyi.web'
data['action']    = 'FY_BY_REALTIME'
data['typoResult']= 'false'


data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果：%s" %(target['translateResult'][0][0]['tgt']))
