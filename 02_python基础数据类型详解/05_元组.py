# tuple 元组, 特点: 不可变的列表
# t = ("张无忌", "赵敏", "呵呵哒")
#
# print(t)
# print(t[1:3])
# t[0] = "小王先森"  # 'tuple' object does not support item assignment
# print(t)

# 你固定了某些数据. 不允许外界修改
# 元组如果只有1个元素(*), 需要在元素的末尾添加一个逗号

# t = ("哈哈",)  # ()默认是优先级
# # print( (1+3) * 6)
# print(t)
# print(type(t))

# # 关于元组的不可变(坑), 内存地址不能变.
# t = (1, 2, 3, ["呵呵哒", "么么哒"])  # (张三, 李四, 王二麻子)
# t[3].append("哒哒哒")
# print(t)
