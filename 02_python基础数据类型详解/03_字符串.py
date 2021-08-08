# # 1. 字符串的格式化问题
# # 我叫xxx, 我住在xxxx, 我今年xx岁, 我喜欢做xxxxx
# name = input("请输入你的名字:")
# address = input("请输入你的住址:")
# age = int(input("请输入你的年龄:"))
# hobby = input("请输入你的爱好:")
#
# # %s 字符串占位
# # %d 占位整数
# # %f 占位小数
# s = "我叫%s, 我住在%s, 我今年%d岁, 我喜欢%s" % (name, address, age, hobby)
# s0 = "我叫%s" % name
# print(s0)
# s1 = "我叫{}, 我住在{}, 我今年{}岁, 我喜欢{}".format(name, address, age, hobby)
# s2 = f"我叫{name},我叫{name},我叫{name},我叫{name},我今年{age}岁,我叫{name},我叫{name}"  # f-string
# print(s2)

# 2. 索引和切片
# 索引: 按照位置提取元素
# s = "我叫周杰伦"
# 可以采用索引的方式来提取某一个字符(文字)
# print(s[3])  # 程序员都是从0开始数数
# print(s[0])
# print(s[-1])  # -表示倒数

# 切片: 从一个字符串中提取一部分内容
# s = "我叫周杰伦,你呢? 你叫周润发吗?"

# print(s[3:6])  # 从索引3位置进行切片, 切到6结束, 坑: 切片拿不到第二个位置的元素
# 语法: s[start:end] 从start到end进行切片. 但是取不到end [start, end)
# print(s[0:5])
# print(s[:5])  # 如果start是从开头进行切片, 可以省略
# print(s[6:])  # 从start开始一直截取到末尾
# : 如果左右两端有空白. 表示开头或者结尾
# print(s[:])

# print(s[-3:-1])  # 目前还是只能从左往右切片
# print(s[-1:-3])  # 没结果, 这里是坑!!!!


# s = "我爱你"
# 可以给切片添加步长来控制切片的方向
# print(s[::-1])  # -表示从右往左
# 语法: s[start:end:step] 从start切到end, 每step个元素出来一个元素

# s = "abcdefghijklmnopqrst"
# print(s[2:11:3])
# print(s[-1:-10:-3])


# ==================================
# 3.字符串常规操作
# 字符串的操作一般不会对原字符串产生影响. 一般是返回一个新的字符串
# 3.1 字符串大小写转换
# s = "python"
# s1 = s.capitalize()
# print(s1)

# s = "I have a dream!"
# s1 = s.title()  # 单词的首字母大写
# print(s1)

# s = "I HAVE A DREAM"
# s1 = s.lower()  # 变成小写字母
# print(s1)

# s = "i have a dream"
# s1 = s.upper()  # 把所有字母变成大写字母
# print(s1)


# # 如何忽略大小写来进行判断  =>  upper()
# verify_code = "xAd1"
# user_input = input(f"请输入验证码({verify_code}): ")
# if verify_code.upper() == user_input.upper():
#     print("验证码正确")
# else:
#     print("验证码不正确")


# ==================================
# 3.2 替换和切割(*)
# strip()  去掉字符串左右两端的空白符(空格, \t, \n)
# s = "    你好,   我叫  周杰伦    "
# s1 = s.strip()
# print(s1)

# # 案例
# username = input("请输入用户名:").strip()
# password = input("请输入密码:").strip()
# if username == "admin":
#     if password == "123456":
#         print("登录成功")
#     else:
#         print("登录失败!")
# else:
#     print("登录失败!")


# ==================================
# # 3.3 replace(old, new) 字符串替换
# s = "你好啊, 我叫赛利亚"
# s1 = s.replace("赛利亚", "周杰伦")
# print(s1)

# a = "hello i am a good man!"
# a1 = a.replace(" ", "")  # 去掉所有的空格
# print(a1)


# split(用什么切割) 字符串切割, 用什么切, 就会损失掉谁.
# a = "python_java_c_c#_javascript"
# lst = a.split("_")  # 切割之后的结果会放在列表当中
# print(lst)
# lst = a.split("_java_")
# print(lst)

# replace(), split(), strip()   => 记住


# ==================================
# 3.4 查找和判断
# 查找
# s = "你好啊. 我叫周润发"
# ret = s.find("周润发12312")  # 返回如果是-1就是没有该字符串出现
# print(ret)
# ret = s.index("周润发12312")  # 如果报错就是没有
# print(ret)

# print("周润发" in s)  # in可以做条件上的判断
# print("周润发" not in s)  # not in 判断是否不存在

# 判断
# name = input("请输入你的名字:")
# # 判断你是不是姓张
# if name.startswith("张"):  # 判断字符串是否以xxxxx开头, endswith()
#     print("你姓张")
# else:
#     print("不姓张")

# money = input("请输入你都里的钱:")
#
# if money.isdigit():  # 判断字符串是否由整数组成.
#     money = int(money)
#     print("可以花钱了")
# else:
#     print("对不起,您输入有误....")
#
#
# # startswith(), isdigit(), in, not in, find


# ==================================
# 3.5 补充和总结
# s = "hello"
# print(len(s))  # length  长度

# join()
# s = "python_java_c_javascript"
# lst = s.split("_")
# print(lst)

# lst = ['赵本山', '王大拿', '大张伟', '马大哈']
# # 用_把上面的人的名字连起来
# s = "_".join(lst)
# print(s)

# 总结:
"""
1. f"{变量}"  格式化一个字符串
2. 索引和切片:
    索引: 从0开始的. []
    切片: s[start: end: step], end位置的数据永远拿不到
3. 相关操作:
    字符串操作对原字符串是不发生改变的.
    1. upper() 在需要忽略大小写的时候
    2. strip() 可以去掉字符串左右两端的空白(空格, \t, \n)
    3. replace() 字符串替换
    4. split()  对字符串进行切割
    5. join()  拼接一个列表中的内容成为新字符串
    6. startswith() 判断字符串是否以xxx开头
    7. len() 字符串长度(内置函数)

    字符串的循环和遍历
    for c in s:
        print(c)   字符串中的每一个字符

    关于in:
        1. 判断xxx是否在xxxx中出现了
        2. for循环
"""










