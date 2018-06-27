# demo-python-translation-with-URL #
# 1.开发环境配置 #
安装Python3.0+

安装Chrome

# 2.操作 #
## 点击以下链接 ##

This is an [example link](http://fanyi.youdao.com/?keyfrom=dict2.top).

在链接点击右键，选择检查(Ctrl+Shift+I)

选择Network标签，在翻译界面内随便输入内容

可以看到我们拦截到的信息

这是我们浏览器和客户端的内容
	
****
## image: ##
![](https://i.imgur.com/XUdv3Rp.png)
****
### 我们这里来分析拦截到的信息： ###

Request URL：实现翻译的地址

Request Method：请求方法是POST形式

Status Code：状态灯，200就是正常响应的意思，404就是页面找不到了

Remote Address：服务器IP地址和打开的端口号

Reques Headers：客户端发送请求的Headers，服务端用来判断是否非人类访问

User-Agent：识别是浏览器访问还是代码访问

Apple WebKit：浏览器实现的核心平台

From Data：表单数据

Json：轻量级的数据交换格式



# 3.选择环境Python环境 #
打开IDLE终端输入代码

File菜单栏New 一个 File

****
![](https://i.imgur.com/smKt3w1.png)

    import urllib.request
导入URL.parse模块，负责解析功能

     import urllib.parse


直接拷贝URL和Form Data：

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = 'content'
    data['from']  = 'AUTO'
    data['to']= 'AUTO'
    data['smartresult'] = 'dict'
    data['client']= 'fanyideskweb'
    data['salt']  = '1523259845567'
    data['sign']  = '5e74a770f46956fc4db664cd703c4e20'
    data['doctype']   = 'json'
    data['version']   = '2.1'
    data['keyfrom']   = 'fanyi.web'
    data['action']= 'FY_BY_REALTIME'
    data['typoResult']= 'false'

需要用urllib.parese.urlencode()函数对它进行一个编码

编码成URL的形式：

  `data = urllib.parse.urlencode(data).encode('utf-8')`

发出请求，得到响应：

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    print(html)

# 4.运行 #

![](https://i.imgur.com/bdMsn9K.png)

运行后会出现新的终端

运行后发现这样的问题

在新的终新输入以下代码

    >>>import json
    >>>json.loads(html)
	
	>>target = json.loads(html)
	>>>type(target)

	>>>target['translateResult']

	>>>target['translateResult'][0][0]

	>>>target['translateResult'][0][0]['tgt']

### 可以看到运行结果已经出来了 ###

# 5.优化代码 #
### 在旧终端优化： ###
    import urllib.request
    import urllib.parse
    import json 					#增加代码处
    
    content = input("请输入需要翻译的内容：")
    
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from']  = 'AUTO'
    data['to']= 'AUTO'
    data['smartresult'] = 'dict'
    data['client']= 'fanyideskweb'
    data['salt']  = '1523259845567'
    data['sign']  = '5e74a770f46956fc4db664cd703c4e20'
    data['doctype']   = 'json'
    data['version']   = '2.1'
    data['keyfrom']   = 'fanyi.web'
    data['action']= 'FY_BY_REALTIME'
    data['typoResult']= 'false'
    
    
    data = urllib.parse.urlencode(data).encode('utf-8')
    
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    
	#增加代码处:
    target = json.loads(html)
    print("翻译结果：%s" %(target['translateResult'][0][0]['tgt']))		

### 运行结果：###

![](https://i.imgur.com/DJ9g5at.png)

# 6.常见问题 #
1. 没有找到translate拦截到的界面：有道词典要进入到自动翻译的页面，否则会出现找不到拦截界面的情况。
2. 无法找到Form Data表单数据：找到Network的标签，再找到translate拦截界面，拉到底部可查看Form Data表单数据
3. 运行时出现"errorCode":50错误：从网页上URL复制的地址内容要删除_o，
例：url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
4. Json Decode Error错误：这个错误出现原因是非Json符合引用，参考自身网页正确的Form Data表单数据
