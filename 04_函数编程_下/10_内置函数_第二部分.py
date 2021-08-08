"""
zip: 可以把多个可迭代内容进行合并
sorted: 排序
filter: 筛选
map:    映射
"""
#        0         1       2
# lst1 = ["赵本山", "范伟", '苏有朋']
# lst2 = [40, 38, 42]
# lst3 = ["卖拐", "耳朵大有福", "情深深雨蒙蒙"]

# result = []
# for i in range(len(lst1)):
#     first = lst1[i]
#     second = lst2[i]
#     third = lst3[i]
#     result.append((first, second, third))
# print(result)

# result = zip(lst1, lst2, lst3)
# # for item in result:
# #     print(item)
#
# lst = list(result)
# print(lst)


# a = 188
# print(locals())  # 此时locals被写在了全局作用域范围内. 此时看到的就是全局作用域中的内容

# def func():
#     a = 336
#     print(locals())  # 此时locals放在局部作用域范围, 看到的就是局部作用域的内容
# func()


# c = 12
# print(globals())  # globals看到的是全局作用域中的内容
# def func():
#     a = 336
#     print(globals())
#
# func()

# lst = [16,22,68,1,147,256,49]
# s = sorted(lst, reverse=True)  # reverse翻转
# print(s)

# #       1      3        2       4           123132
# lst = ["秋", "张二嘎", "比克", "卡卡罗特", "超级宇宙无敌大帅B"]
#
# # def func(item):  # item对应的就是列表中的每一项数据
# #     return len(item)
#
# s = sorted(lst, key=lambda x: len(x))
# print(s)



# lst = [
#     {"id": 1, "name": "周润发", "age": 18, "salary": 5200},
#     {"id": 2, "name": "周星驰", "age": 28, "salary": 511100},
#     {"id": 3, "name": "周海媚", "age": 78, "salary": 561230},
#     {"id": 4, "name": "周伯通", "age": 12, "salary": 532100},
#     {"id": 5, "name": "周大兴", "age": 35, "salary": 53210},
#     {"id": 6, "name": "周周有辣", "age": 47, "salary": 520},
#     {"id": 7, "name": "周扒皮", "age": 8, "salary": 12},
# ]
#
# # 1.根据每个人的年龄排序
# s = sorted(lst, key=lambda d: d['age'])
# print(s)
#
# # 2.根据工资进行排序. 从大到小
# s = sorted(lst, key=lambda d: d['salary'], reverse=True)
# print(s)


# #        T         T     T         F            F
# lst = ["张无忌", "张三丰", "张翠山", "灭绝小师太", "小狐仙"]
# f = filter(lambda x: x.startswith("张"), lst)
# print(list(f))


lst = [1,2,3,4,5,6,7,8,9]

# result = [item * item for item in lst]
# print(result)

r = map(lambda x: x * x, lst)
print(list(r))

