"""
生成器(generator):
    生成器的本质就是迭代器

    创建生成器的两种方案:
        1. 生成器函数
        2. 生成器表达式

    生成器函数
        生成器函数中有一个关键字yield
        生成器函数执行的时候, 并不会执行函数, 得到的是生成器.

        yield: 只要函数中出现了yield. 它就是一个生成器函数
            作用:
                1. 可以返回数据
                2. 可以分段的执行函数中的内容, 通过__next__()可以执行到下一个yield位置
        优势:
            用好了, 特别的节省内存


    生成器表达式 -> 一次性的
        语法: (数据 for循环 if)

"""

# def func():
#     print(123456)
#     yield 999  # yield也有返回的意思.
#
# ret = func()
# # print(ret)  # <generator object func at 0x115f2dbd0>
# print(ret.__next__())  # yield只有执行到next的时候才会返回数据
# print(ret.__next__())  # StopIteration


# def func():
#     print(123)
#     yield 666
#     print(456)
#     yield 999
#
# ret = func()
# print(ret.__next__())
# print(ret.__next__())


# 去工厂定制10000件衣服
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f"衣服{i}")
#     return lst
#
# lst = order()
# print(lst)

# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f"衣服{i}")
#         if len(lst) == 50:
#             yield lst
#             # 下一次拿数据
#             lst = []
#
#
# gen = order()
# print(gen.__next__())
# print(gen.__next__())


gen = (i**2 for i in range(10))

for item in gen:
    print(item)

lst = list(gen)
print(lst)
#
# s = list("周杰伦")  # list() =>  for  => next()
# print(s)