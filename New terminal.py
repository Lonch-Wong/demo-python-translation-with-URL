Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:\Users\51774\Desktop\Test.py ==================
                          {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"content","tgt":"内容"}]]}

>>> import json
>>> json.loads(html)
{'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'content', 'tgt': '内容'}]]}
>>> target = json.loads(html)
>>> type(target)
<class 'dict'>
>>> target['translateResult']
[[{'src': 'content', 'tgt': '内容'}]]
>>> target['translateResult'][0][0]
{'src': 'content', 'tgt': '内容'}
>>> target['translateResult'][0][0]['tgt']
'内容'
>>> #重新返回终端优化代码
