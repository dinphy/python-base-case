"""
    返回值: 函数执行之后. 会给调用方一个结果. 这个结果就是返回值

    关于return:
        函数只要执行到了return. 函数就会立即停止并返回内容. 函数内的return的后续的代码不会执行
        1. 如果函数内没有return , 此时外界收到的是None
        2. 如果写了return
            1. 只写了return, 后面不跟数据, 此时接收到的依然是None  -> 相当于break
            2. return 值 , 此时表示函数有一个返回值, 外界能够收到一个数据 -> 用的最多
            3. return 值1, 值2, 值3....., 此时函数有多个返回值, 外界收到的是元组, 并且, 该元组内存放所有的返回值
"""
# def func(a, b):
#     # print(a + b)
#     return a + b
#
#
# ret = func(10, 20)
# print(ret * 3)

# def func():
#     pass
#     # return None
#
# ret = func()
#
# print(ret)



# def func():
#     print(123)
#     return   # 会让程序停止.  后续代码不会继续执行. 有点儿像循环里面的break
#     print(456)
#
# ret = func()
# print(ret)


def func():
    return 1, 2, 3, 4


ret = func()
print(ret)