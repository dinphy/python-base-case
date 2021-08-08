# 输入两个整数a、b(a<b),从区间[a,b]中取出两个整数进行相加并输出这两个数
import random

a = int(input('请输入整数a:'))
b = int(input('请输入整数b:'))
i = random.randint(a,b)
j = random.randint(a,b)

print('i的值为：',i)
print('j的值为：',j)
print('i与j的和为：',i+j)
