# 首先, 字典是以键值对的形式进行存储数据的
# 字典的表示方式: {key:value, key2:value, key3:value}

# dic = {"jay": "周杰伦", "金毛狮王": "谢逊"}
# val = dic["金毛狮王"]  # 用起来只是把索引换成了key
# print(val)

# 字典的key必须是可哈希的数据类(不可变)
# 字典的value可以是任何数据类型
# dic = {[]:123}
# print(dic)

# dic = {"汪峰的孩子": ["孩子1", "孩子2"]}


# #7.2 字典的增删改查

dic = dict()

dic['jay'] = "周杰伦"
dic[1] = 123
# print(dic)

dic['jay'] = "昆凌"  # 此时, 字典中已经有了jay. 此时执行的就是修改操作了
# print(dic)

dic.setdefault("jay", "胡辣汤")  # 设置默认值. 如果以前已经有了tom了. setdefault就不起作用了
# print(dic)

# # 删除
# dic.pop("jay")  # 根据key去删除
# print(dic)

# 查询
# print(dic['jay10010'])  # 如果key不存在. 程序会报错. 当你确定你的key是没问题的, 可以用
# print(dic.get('jay10086'))  # 如果key不存在. 程序返回None. 当不确定你的key的时候. 可以用

# # None
# a = None  # 单纯的就是空, 表示没有的意思
# print(type(a))

# # 例子:
# dic = {
#     "赵四": "特别能歪嘴",
#     "刘能": "老, 老四啊...",
#     "大脚": "跟这个和那个搞对象",
#     "大脑袋": "瞎折腾....",
# }
# name = input("请输入你想知道的我们村的人的名字: ")
# val = dic.get(name)
# if val is None:
#     print("我门村没这个人~~~")
# else:
#     print(val)


# # 7.3 字典进阶操作 -- 循环和嵌套

# dic = {
#     "赵四": "特别能歪嘴",
#     "刘能": "老, 老四啊...",
#     "大脚": "跟这个和那个搞对象",
#     "大脑袋": "瞎折腾....",
# }

# 1. 可以用for循环, 直接拿到key
# for key in dic:
#     print(key, dic[key])

# 2. 希望把所有的key全都保存在一个列表中
# print(list(dic.keys()))  # 拿到所有的key了

# 3. 希望吧所有的value都放在一个列表中
# print(list(dic.values()))

# 4. 直接拿到字典中的key和value
# print(list(dic.items()))
# for key, value in dic.items():  # 可以直接拿到字典的所有的key和value
#     # print(item)  # 确定, item中只有两项元素
#     print(key, value)

# a, b = (1, 2)  # 元组或者列表都可以执行该操作. 该操作被称为解构(解包)
# print(a)
# print(b)


# # 字典的嵌套
# wangfeng = {
#     "name": "汪峰",
#     "age": 18,
#     "wife": {
#         "name": "章子怡",
#         "hobby": "演戏",
#         "assistant": {
#             "name": "小王先森",
#             "age": 19,
#             "hobby": "打游戏"
#         }
#     },
#     "children": [
#         {"name": "孩儿1", "age": 13},
#         {"name": "孩儿2", "age": 10},
#         {"name": "孩儿3", "age": 8},
#     ]
# }
#
# # 汪峰妻子的助手的名字
# name = wangfeng['wife']['assistant']['name']
# print(name)
#
# # 给汪峰的第二个孩子加1岁
# wangfeng['children'][1]['age'] = wangfeng['children'][1]['age'] + 1
# print(wangfeng)


# # 7.4 补充. 关于字典的循环删除
dic = {
    "赵四": "特别能歪嘴",
    "刘能": "老, 老四啊...",
    "大脚": "跟这个和那个搞对象",
    "大脑袋": "瞎折腾....",
}
temp = []  # 存放即将要删除的key
for key in dic:
    if key.startswith("大"):
        temp.append(key)
        # dic.pop(key)  # dictionary changed size during iteration

for t in temp:  # 循环列表, 删除字典中的内容
    dic.pop(t)

print(dic)
