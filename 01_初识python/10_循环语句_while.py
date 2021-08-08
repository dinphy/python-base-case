# while True:  # 死循环
#     print("喷死你")


# # 用程序去数数, 从1~100
# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1


# 1+2+3+4+5+6+7+8+9......+100 = ?

# i = 1
# s = 0
# while i <= 100:
#     # print(i)  # 从1 到 100 的每一个数
#     s = s + i   # 累加
#     i = i + 1
# print(s)
"""
i     s
1       0+1
2       0+1+2
3       0+1+2+3
4
5
6
7
8
100     0+1+2+3+....+99 + 100
"""

# 1-2+3-4+5-6+7....-100 = ?

sum = 0
num = 1
while num <= 100:
    if num % 2 == 0: # 能被2整数的数，也就是偶数项
        sum = sum - num
    else:
        sum = sum + num
    num = num + 1
print(sum)
