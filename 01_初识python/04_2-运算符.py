"""
1. 算数运算
    + - * / % //
2. 比较运算
    > < >= <= == !=
3. 赋值运算
    =  +=, -=, *=.....
    a += b
    a = a + b

    n = 1
    sum = 0
    while n <= 100:
        sum = sum + n  # sum += n
        n = n + 1      # n += 1

4. 逻辑运算
    1. and, 并且, 左右两端同时成立. 结果才能成立
    2. or,  或者, 左右两端有一个成立. 结果就成立
    3. not, 非,   非真既假, 非假既真.

    当and和or以及not同时出现的时候. 最好呢. 加上括号. 不会产生歧义或者不易理解的问题
    如果没有括号怎么办?
    记住运算顺序:
        先算括号 > 算not > and  > or

5. 成员运算
    in     判断xxx是否在xxxx中出现了
    not in 判断xxx是否不在xxxx中出现了
"""

# a = 20
# b = 3
# c = a % b  # 10 / 3 = 3.....1
# d = a // b
# print(c)
# print(d)

# 让用户输入一个数字. 判断是否是35的倍数

# n = int(input("来个数: "))
# if n % 35 == 0:
#     print("是35的倍数")
# else:
#     print("不是35的倍数")


# a = 20
# b = 20
# print(a != b)

# a = 30
# b = 40

# # 互换操作
# temp = a  # 备份, 有桌子
# a = b
# b = temp

# 下面代码仅适用于python
# a, b = b, a
#
# print(a)
# print(b)


# 逻辑运算
# print(True and True and True and False)
# print(False or True or False or False)
# print( not False)

# # 模拟用户登录.
# username = input("用户名:")
# password = input("密码:")
# if username == "admin" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")


# print(True and False or True and False or not True and True or False)
# print(False or False or False or False)

lst = [1,2,3,4,5,]
print(3 in lst)
print(666 not in lst)
