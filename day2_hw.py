# 作业一：
# def test(info):
#     if info.username == 'root' and 'info.passwd' == '1223':
#         print('你有权限')
#     else:
#         print('你没有权限')
#         return
#     return data = "1,2,3"
# def test2(info):
#     if info.username == 'root' and 'info.passwd' == '1223':
#         print('你有权限')
#     else:
#         print('你没有权限')
#         return
#     return data2 = "4,5,6"
# @permit
# def test2(info)
#     return data2 = "4,5,6"
# @permit
# def test(info)
#     return data = "123"

# 实现permit装饰器对权限进行验证
def permit(username,passwd):
    def login_in(func):
        def deco(*args, **kwargs):
            if username=="renxueke"and passwd == "123":
                print("你有权限")
            else:
                print("你没有权限")
                return
            func(*args, **kwargs)
        return deco
    return login_in

@permit("renxueke","123")
def login():
    print("登录成功")
login()

# 作业二：
# 递归函数列出所有文件 使用os.listdir os.isfile
# 练习找出单个目录中的最大文件
# 练习找出目录树中的最大文件

import os
