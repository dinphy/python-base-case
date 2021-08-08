"""
作用域: 变量的访问权限

总结: 里面访问外面没问题, 外面访问里面不能直接访问到
"""
# a = 10  # 全局变量 -> 全局作用域
# print(a)
#
# def func():   # 全局的一个函数
#     b = 20   # 局部变量, 局部作用域
#     print(a)
#
# # func()
# # print(b)
#
# def func3():
#     func()
# func3()

def func():
    c = 10086
    return c  # 如果想要在函数外面访问到函数内部的东西. 必须要return

c1 = func()
print(c1)



