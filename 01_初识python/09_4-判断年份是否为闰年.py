# 输入一个年份，判断年份是否为闰年
# 闰年：
'''
    1. 十年一闰百年不闰：即如果year能够被4整除，但是不能被100整除，则year是闰年。
    2. 每四百年再一闰：如果year能够被400整除，则year是闰年。
'''

year = int(input('请输入一个年份：'))
if year%4 == 0 and year%100 != 0 or year%400 == 0:  # 运算优先级：括号 > not > and  > or
    print(f'{year}是闰年')
else:
    print(f'{year}是平年')
