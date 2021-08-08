# set集合, set集合是无序的
# s = {1,"呵呵哒",2,3}
# print(type(s))
# print(s)

# s = {1, 2, 3, "呵呵", (1, 2, 3), []}  # unhashable type: 'list'
# print(s)

# 不可哈希: python中的set集合进行数据存储的时候. 需要对数据进行哈希计算, 根据计算出来的哈希值进行存储数据
#          set集合要求存储的数据必须是可以进行哈希计算的.
#          可变的数据类型, list, dict, set
# 可哈希: 不可变的数据类型, int, str, tuple, bool.

s = set()  # 创建空集合

s.add("赵本山")
s.add("范伟")
s.add("麻花藤")
# print(s)

# s.pop()  # 由于集合无序. 测试的时候没法验证是最后一个.
# print(s)

# s.remove("范伟")
# print(s)

# # 想要修改. 先删除. 再新增
# s.remove("麻花藤")
# s.add("沈腾")
# print(s)

# for item in s:
#     print(item)


# # 交集, 并集, 差集
# s1 = {"刘能", "赵四", "皮长山"}
# s2 = {"刘科长", "冯乡长", "皮长山"}
#
# print(s1 & s2)  # 交集
# print(s1.intersection(s2))
#
# print(s1 | s2)  # 并集
# print(s1.union(s2))
#
# print(s1 - s2)  # 差集
# print(s1.difference(s2))


# 重要的作用: 可以去除重复
# s1 = {"周杰伦", "昆凌", "蔡依林", "侯佩岑"}
# print(s1)
# s1.add("周杰伦")
# print(s1)

lst = ["周杰伦", "昆凌", "蔡依林", "侯佩岑", "周杰伦", "昆凌", "蔡依林", "侯佩岑", "周杰伦", "昆凌", "蔡依林", "侯佩岑"]
print(lst)
print(list(set(lst)))   # 去除重复之后的数据是无序的.

