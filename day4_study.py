# 域名： www.baidu.com

# URL 格式
#
# <scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<frag>
# <方案>://<用户>:<密码>@<主机>:<端口>/<路径>;<参数>?<查询>#<片段>
#

#使用python解析url
# from urllib.parse import urlparse
# obj=urlparse("https://172.168.10.0:8080/item/统一资源定位系统/5937042?fromtitle=url&fromid=110640")
# print(obj)
# print(obj.path)
# print(obj.scheme)
# print(obj.query)

from urllib.parse import urlencode
data={
    "kw":"中国"
}
print(urlencode(data))