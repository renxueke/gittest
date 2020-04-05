# import pickle
# import json
# d={"a":1,"b":2,"c":3}
# ll=json.dumps(d)
# print(type(ll))
# lll=json.loads(ll)
# print(type(lll))
#
# l=pickle.dumps(d)
# print(l)
# s=pickle.loads(l)
# print(s)

# import pickle
#
# class Record:
#     def __init__(self,name,phone_number):
#         self.name=name
#         self.phone_number=phone_number
#
# R=pickle.dumps(Record)
# print(R)
# print(pickle.loads(R))
#
# record=Record("renxueke","122")
# r=pickle.dumps(record)
# print(r)
# print(pickle.loads(r))


#
# import pickle
# L=[1,2,3]
# with open("d://L.dat","wb")as f:
#     pickle.dump(L,f)
# with open("d://L.dat","rb")as f:
#     print(pickle.load(f))
#
# class Record:
#     def __init__(self,name,phone_number):
#         self.name=name
#         self.phone_number=phone_number
#
# with open("d:/Record.dat","wb") as f:
#     pickle.dump(Record,f)
# with open("d:/Record.dat","rb") as f:
#     print(pickle.load(f))
#
# record=Record("renxueke","133")
# with open("d:/Record.dat","wb") as f:
#     pickle.dump(record,f)
# with open("d:/Record.dat","rb") as f:
#     print(pickle.load(f))



# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# if __name__=="__main__":
#     print(factorial(5))

# 报错：RecursionError: maximum recursion depth exceeded，栈溢出--解释器为栈的结构

# def test():
#     return test()
# if __name__ == '__main__':
#     test()

#查看递归最大次数，递归深度
# import sys
# s=sys.getrecursionlimit()
# print(s)

# x的n次幂：

# def power (x,n):
#     if n==0 :
#         return 1
#     else:
#         return x*power(x,n-1)
#
# if __name__ == '__main__':
#     print(power(2,6))

# 练习：
# 取出n层嵌套列表里的所有元素
# 提示判断一个元素i是否是list
# 使用isinstance(i,list)函数 [1,2,3,[4,5,6]] 1 2 3 4 5 6

# def get_ele(i):
#     if isinstance(i,list):
#         for l in i:
#             get_ele(l)
#     else:
#         print(i)
#
# if __name__ == '__main__':
#     ll=[1,2,3,[4,5,6]]
#     get_ele(ll)


# 装饰器

# def deco(func):
#     def inner():
#         func()
#         print("running inner()")
#     return inner
#
# @deco
# def target():
#     print("running target()")
#
# @deco
# def target1():
#     print(1)
#
# if __name__ == '__main__':
#     target()
#     target1()

# 等同于上面的代码

# def deco(func):
#     def inner():
#         print("running inner()")
#     return inner
# def target():
#     print("running target()")
#
# if __name__ == '__main__':
#     target=deco(target)
#     target()


# 统计函数执行时间
# import time
# def decorator(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         end_time=time.time()
#         print(end_time-start_time)
#
#     return wrapper
#
# @decorator
# def func():
#     print("hello world")
#     time.sleep(1)
# func()
#
# @decorator
# def func2():
#     print("hello world")
#     time.sleep(1)
# func2()
# 加法函数
# def add_decorator(f):
#     def wrap(x,y):
#         print("加法")
#         return f(x,y)
#     return wrap
# @add_decorator
# def add_method(x,y):
#     return x+y
# print(add_method(2,3))

# 带参数的装饰器
# def out_f(arg):
#     print("out_f"+arg)
#     def decorator(func):
#         def inner():
#             func()
#         return inner
#     return decorator
# @out_f("123")
# def func():
#     print("hello world")
# func()



# 可迭代的对象，迭代器


# 斐波那契数--定义迭代器，菲波那切数列
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()

for f in fibs:
    if f>1000:
        print(f)
        break


