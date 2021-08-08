"""
推导式:
    简化代码.
    语法:
        列表推导式: [数据 for循环 if判断]
        集合推导式: {数据 for循环 if判断}
        字典推导式: {k:v for循环 if判断}

    不要把推导式妖魔化.
    (数据 for循环 if判断)  -> 不是元组推导式, 根本就没有元组推导式.  这玩意叫生成器表达式

"""
# lst = []
# for i in range(10):
#     lst.append(i)
#
# print(lst)

# lst = [i for i in range(10)]
# print(lst)

# 1. 请创建一个列表[1,3,5,7,9]
# lst = [i for i in range(1, 10, 2)]
# lst = [i for i in range(10) if i % 2 == 1]
# print(lst)

# # 2. 生成50件衣服
# lst = [f"衣服{i}" for i in range(50)]
# print(lst)

# # 3. 将如下列表中所有的英文字母修改成大写
# lst1 = ["allen", "tony", "kevin", "sylar"]
# lst2 = [item.upper() for item in lst1]
# print(lst2)

# s = {i for i in range(10)}
# print(s)

# 4. 请将下列的列表修改成字典, 要求 索引做为key, 数据作为value
lst = ['赵本山', "潘长江", "高达", "奥特曼"]

dic = {i: lst[i] for i in range(len(lst))}
print(dic)

