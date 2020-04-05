# 作业一：
# def test(info):
#     if info.username == 'root' and 'info.passwd' == '1223':
#         print('你有权限')
#     else:
#         print('你没有权限')
#         return
#     return data = "1,2,3"
#
#
# def test2(info):
#     if info.username == 'root' and 'info.passwd' == '1223':
#         print('你有权限')
#     else:
#         print('你没有权限')
#         return
#     return data2 = "4,5,6"
#
#
# @permit
# def test2(info)
#     return data2 = "4,5,6"
#
#
# @permit
# def test(info)
#     return data = "123"
#
#
# 实现permit装饰器对权限进行验证
def permit(info):
    if info.username == "renxueke" & info.passwd == "123":
        print("登录成功")
    else:
        print("登录不成功")
        return

@permit
def data_test(username,passwd):
    username="renxueke"
    passwd="123"
    permit(username,passwd)