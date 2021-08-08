"""
1. 找到这个文件. 双击打开它

open(文件路径, mode="", encoding="")
    文件路径:
        1. 绝对路径
            d:/test/xxxx.txt
        2. 相对路径
            相对于当前你的程序所在的文件夹
            ../ 上一层文件夹
    mode:
        r : read 读取
        w : write 写
        a : append 追加写入
        b : 读写的是非文本文件  -> bytes

    with: 上下文, 不需要手动去关闭一个文件

    修改文件:
        1. 从源文件中读取内容.
        2. 在内存中进行调整(修改)
        3. 把修改后的内容写入新文件中
        4. 删除源文件. 将新文件重命名成源文件

"""

import os  # 和操作系统相关的模块引入
import time  # 和时间相关的模块

# f = open("葫芦娃.txt", mode="r", encoding="utf-8")

# content = f.read()  # 全部读取
# print(content)
# line = f.readline().strip()   # 去掉字符串左右两端的空白. 空格, 换行, 制表符
# print(line)
#
# line = f.readline().strip()
# print(line)
#
# line = f.readline().strip()
# print(line)

# content = f.readlines()
# print(content)


# print("呵呵哒")  # print内部存在一个换行
# print("么么哒")

# 最重要的一种文本读取方式(必须掌握)
# for line in f:   # 从f中读取到每一行数据
#     print(line.strip())


# # 写入文件
# # w模式下. 如果文件不存在. 自动的创建一个文件
# # w模式下. 每一次open都会清空掉文件中的内容
# f = open("名小吃.txt", mode="w", encoding="utf-8")
# f.write("胡辣汤")
#
# f.close()  # 每次操作之后养成好习惯.要关闭链接

# # 准备一个列表.要求把列表中的每一项内容. 写入到文件中
# lst = ['张无忌', "汪峰", "章子怡", "赵敏"]
# f = open("华山会剑.txt", mode="w", encoding="utf-8")  # 大多数情况下要把open写循环外面
#
# for item in lst:
#     f.write(item)
#     f.write("\n")
#
# f.close()


# # a模式
# f = open("华山会剑.txt", mode="a", encoding="utf-8")
# f.write("你好厉害")


# # with
# with open("葫芦娃.txt", mode="r", encoding="utf-8") as f:  # f = open()
#     for line in f:
#         print(line.strip())


# 想要读取图片
# 在读写非文本文件的时候要加上b
# with open("胡一菲.jpeg", mode="rb") as f:
#     for line in f:
#         print(line)


# # 文件的复制:
# # 从源文件中读取内容. 写入到新路径去
# with open("胡一菲.jpeg", mode="rb") as f1, \
#      open("../01_初识python/胡二飞.jpeg", mode="wb") as f2:
#      for line in f1:
#          f2.write(line)



# 文件修改
# 把文件中的周 -> 张
with open("人名单.txt", mode="r", encoding="utf-8") as f1, \
     open("人名单_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line = line.strip()   # 去掉换行
        if line.startswith("周"):
            line = line.replace("周", "张")  # 修改

        f2.write(line)
        f2.write("\n")

time.sleep(3)  # 让程序休眠3秒钟
# 删除源文件
os.remove("人名单.txt")
time.sleep(3)
# 把副本文件重命名成源文件
os.rename("人名单_副本.txt", "人名单.txt")


