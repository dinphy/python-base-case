"""
函数可以嵌套函数

综上:
    1, 函数可以作为返回值进行返回
    2, 函数可以作为参数进行互相传递
    函数名实际上就是一个变量名, 都表示一个内存地址

"""

# def func1():
#     pass
#
# def func2():
#     func1()  # 这个叫函数的调用. 不叫嵌套
#
# func2()

# def func1():
#     b = 20
#     def func2():  # 函数的嵌套, 局部变量
#         pass
#     # func2 = def():
#     print(b)
#     func2()  # 局部的东西. 一般都是在局部自己访问使用的
#
#
# print(func1())


# def func1():
#     print(123)
#     def func2():
#         print(456)
#         def func3():
#             print(789)
#         print(1)
#         func3()
#         print(2)
#     print(3)
#     func2()
#     print(4)
#
# func1()

# def func():
#     def inner():
#         print(123)
#     print(inner)
#     return inner  # 返回的是一个函数, 此时我们把一个函数当成一个变量进行返回的
#
# b1 = func()  # b1是func的内部inner
# print(b1)
# b1()

# def an():
#     print(123)
# an()
# bn = an
# bn()


# 代理模式
def func(an):  # 此时an收到的是一个函数
    an()  # 执行这个函数


def target():
    print("我是target")

c = 456
func(target)  # 实参可以是函数











