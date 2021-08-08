"""
https://www.processon.com/view/link/5dbfcf15e4b09df5518ee260
内置函数: 直接能拿来用的函数
print
input
"""
# print("hello world")

# s = "123"
# i = int(s)
# b = bool(s)
# f = float(s)
# complex 复数: 实部+虚部

# # bin, oct, hex
# a = 18  # 十进制
# print(bin(a))  # 0b10010
# print(oct(a))  # 0o22
# print(hex(a))  # 0x12
#
# a = 0b10010
# print(int(a))  # 二进制转化成十进制


# # sum, min, max, pow
# a = 10
# b = 3
# print(pow(a, b))
# print(a ** b)  # 次幂

# lst = [12,456,32,18,64,57]
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = {1,2,3,}
# lst = list("呵呵哒")  # 内部一定会有一个循环(for)
# print(lst)

# s = slice(1, 4, 2)  # [1:4:2]
# print("呵呵呵呵呵呵呵呵呵"[s])


# format, ord, chr
# format 格式化
# a = 18
# print(format(a, "08b"))  # b: 二进制, o: 八进制, x: 十六进制

# a = "中"  # python的内存中使用的是unicode
# print(ord(a))  # 中国的中字在unicode中码位是20013
# print(chr(20013))  # 给出编码位置. 展示出文字
# for i in range(65536):
#     print(chr(i)+" ", end="")


# enumerate, all, any
# print(all([1, "123", '豆沙包']))   # 当成and来看  t and t and t
# print(any([0, "", '']))  # 当成or来看
# lst = ["张无忌", "张翠山", "张三丰", "张大大"]
#
# for index, item in enumerate(lst):
#     print(index, item)
#
# for i in range(len(lst)):
#     print(i, lst[i])
#

# s = "呵呵哒"
# print(hash(s))  # 一定是一个数字 -> 想办法转化成内存地址. 然后进行数据的存储 -> 字典(集合)哈希表
#
#
# print(id(s))
#
# print(help(str))

s = "呵呵哒"
print(help(s))
print(dir(s))  # 当前这个数据能执行哪些操作


