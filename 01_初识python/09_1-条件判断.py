# ======第一种======
# score = 100
# if score > 300:
#     print("回家放牛")
#
# print("回家种地")


# # ======第二种=====
# score = input("请输入你中考分数:")
# score = int(score)
#
# if score > 500:
#     print("至少可以上民中")
# else:
#     print("可上八中或十五中")


# # =========第三种========
# score = int(input("请输入你中考分数:"))
#
# if score > 500:
#     if score > 600:
#         print("上一中没问题了")
#     else:
#         print('有机会上二中或民中')
# else:
#     print("你只能上八中或十五中")


# # =========第四种========
score = int(input("请输入你中考分数:"))

if score >= 600:
    print("上一中没问题了")
elif score >= 500:
    print("有机会上二中或民中")
elif score >= 300:
    print("你只能上八中或十五中")
else:
	print("回家放牛去吧")

