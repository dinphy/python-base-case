# while True:
#     content = input("请输入你要喷的内容(q结束喷人):")
#     if content == "q":  # == 表示判断左右两端是否一致
#         break    # 结束循环
#     print("发送给下路:", content)


# 从1-10
i = 1
while i <= 10:
    if i == 4:
        i = i + 1
        continue  # 终止当前本次循环. 继续执行下一次循环
    print(i)
    i = i + 1


