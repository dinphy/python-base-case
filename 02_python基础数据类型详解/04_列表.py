# # 4.1 ===================================================
# # 定义: 能装东西的东西
# # 在python中用[]来表示一个列表. 列表中的元素通过,隔开
# # a = ["张三丰", "张无忌", "张绍刚", [1,2,3,True, ]]
# # 特性:
# #   1. 也像字符串一样也有索引和切片
# #   2. 索引如果超过范围会报错
# #   3. 可以用for循环进行遍历
# #   4. 用len可以拿到列表的长度
# lst = ["金毛狮王", "张绍刚", "张无忌", "郭麒麟"]
# #
# # print(lst[0])
# # print(lst[1:3])
# # print(lst[::-1])
# # print(lst[3652])   # list index out of range
# # for item in lst:
# #     print(item)
# print(len(lst))


# # 4.2 ===================================================
# 列表的增删改查(*)
# lst = []
# # 向列表中添加内容
# # append() 追加(*)
# lst.append("张绍刚")
# lst.append("赵本山")
# lst.append("张无忌")
# # insert() 插入
# lst.insert(0, "赵敏")
# # extend() 可以合并两个列表, 批量的添加
# lst.extend(['武则天', "嬴政", "马超"])
# print(lst)

# # 删除
# ret = lst.pop(3)  # 给出被删除的索引. 返回被删除的元素
# print(lst)
# print(ret)
# lst.remove("马超")  # 删除某个元素(*)
# print(lst)

# # 修改
# lst[4] = "恺"  # 直接用索引就可以进行修改操作
# print(lst)

# 查询
# print(lst[3])  # 直接用索引进行查询操作


# # 小练习(*):
# #   把所有的姓张的人修改成姓王
# lst = ['赵敏', '张绍刚', '张无忌', '武则天', '嬴政', '马超']
#
# # lst[1] = "王绍刚"
#
# # for item in lst:  # 此时, 我们看不到元素的索引位置
# for i in range(len(lst)):  # len(lst)列表的长度 ->  可以直接拿到列表索引的for循环
#     item = lst[i]  # item依然是列表中的每一项
#     if item.startswith("张"):
#         # 张绍刚
#         new_name = "王"+item[1:]
#         print(new_name)
#         # 把新名字丢回列表(需要索引了?)
#         lst[i] = new_name  # 修改
#
# print(lst)


# 4.3 ==============================================
# 列表的其他操作(补充)
# 排序
# lst = [1, 2, 3, "麻花藤", "武大郎"]  # 列表会按照你存放的顺序来保存
# print(lst)

# lst = [222, 444, 123, 43, 123,43243, 111]
# lst.sort()  # 对列表进行升序排序
# lst.sort(reverse=True)   # reverse: 翻转
# print(lst)

# # 列表的嵌套
# lst = ["abc", "def", ["呵呵哒", "妈妈呀", "苦苦脊瓦", ["可乐", "scrapy", 123]], 'aed', "qpr"]
# print(lst[2][3][1])
# lst[2][3][1] = lst[2][3][1].upper()
# print(lst)

# 列表的循环删除(*)
lst = ['赵敏', '张绍刚', '张无忌', '武则天', '嬴政', '马超']

temp = []  # 准备一个临时列表, 负责存储要删除的内容
for item in lst:
    if item.startswith("张"):
        temp.append(item)  # 把要删除的内容记录下来
        # lst.remove(item)  # 有bug

for item in temp:
    lst.remove(item)  # 去原列表中进行删除操作
print(lst)

# 安全稳妥的循环删除方式:
#    将要删除的内容保存在一个新列表中. 循环新列表. 删除老列表













