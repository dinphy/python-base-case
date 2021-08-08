"""
for 变量 in 可迭代:
    pass

iterable: 可迭代的东西
iterator: 迭代器
str, list, tuple, dict, set, open()

可迭代的数据类型都会提供一个叫迭代器的东西. 这个迭代器可以帮我们把数据类型中的所有数据逐一的拿到

获取迭代器的两种方案:
    1. iter() 内置函数可以直接拿到迭代器
    2. __iter__()   特殊方法

从迭代器中拿到数据:
    1. next() 内置函数
    2. __next__() 特殊方法

for里面一定是要拿迭代器的. 所以所有不可迭代的东西不能用for循环
for循环里面一定有__next__出现

总结: 迭代器统一了不同数据类型的遍历工作

迭代器本身也是可迭代的
迭代器本身的特性:
    1. 只能向前不能反复
    2. 特别节省内存
    3. 惰性机制

"""

# it = iter("你叫什么名字啊")
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# print(next(it))  # StopIteration: 迭代已经停止了. 不可以再次从迭代器中拿数据了


# it = "呵呵哒".__iter__()
#
# print(it.__next__())
# print(it.__next__())
# print(next(it))

# # 模拟for循环工作原理:
# s = "我是数据"
# it = s.__iter__()  # 拿到迭代器
# while 1:
#     try:
#         data = it.__next__()
#         print(data)  # for循环的循环体
#     except StopIteration:
#         break
# print(123456)



s = "你好啊, 我叫赛利亚"
it = s.__iter__()

for mm in it:
    print(mm)


