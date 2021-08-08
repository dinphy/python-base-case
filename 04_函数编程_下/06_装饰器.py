"""
内容回顾:
    1. 函数可以做为参数进行传递
    2. 函数可以作为返回值进行返回
    3. 函数名称可以当成变量一样进行赋值操作

装饰器:   -> 要求记住最后的结论
    装饰器本质上是一个闭包
    作用:
        在不改变原有函数调用的情况下. 给函数增加新的功能.
        直白: 可以在函数前后添加新功能, 但是不改原来的代码

    在用户登录的地方, 日志.
    通用装饰器的写法:
        def wrapper(fn):   wrapper: 装饰器, fn: 目标函数
            def inner(*args, **kwargs):
                # 在目标函数执行之前.....
                ret = fn(*args, **kwargs)   #   执行目标函数
                # 在目标函数执行之后.....
                return ret
            return inner     千万别加()

        @wrapper
        def target():
            pass

        target()  #  =>  inner()

    一个函数可以被多个装饰器装饰.
    @wrapper1
    @wrapper2
    def target():
        print('我是目标')

    规则和规律 wrapper1 wrapper2 TARGET wrapper2 wrapper1
"""

# def func():
#     print('我是函数')
#
#
# def gggg(fn):  # fn要求是个函数
#     fn()  # func()
#
# gggg(func)


# def func():
#     def inner():
#         print("123")
#     return inner
#
# ret = func()
# ret()


# def func1():
#     print("我是函数1")
#
# def func2():
#     print("我是函数2")
#
# func1 = func2
#
# func1()


# def guanjia(game):
#     def inner():
#         print("打开外挂")
#         game()  # 玩起来了
#         print('关闭外挂')
#     return inner
#
#
# @guanjia     # 相当于 play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print('你好啊, 我叫赛利亚, 今天又是美好的一天!')
#
#
# @guanjia
# def play_lol():
#     print("德玛西亚!!!!!!")
#
#
# # play_dnf = guanjia(play_dnf)  # 让管家把游戏重新封装一遍. 我这边把原来的游戏替换了
# # play_lol = guanjia(play_lol)  # 让管家把lol也重新封装一下.
#
# play_dnf()  # 此时运行的是管家给的内层函数inner
# play_lol()



# def guanjia(game):
#     #         *, **表示接收所有参数, 打包成元组和字典
#     def inner(*args, **kwargs):  # inner添加了参数, args 一定是一个元组  kwargs 一定是字典 (admin, 123456, "大盖伦")
#         print("打开外挂")
#         #    *, ** 表示把args元组和kwargs字典打散成 位置参数以及关键字参数传递进去
#         game(*args, **kwargs)  # 玩起来了  # game('admin', '123456', "大盖伦")
#         print('关闭外挂')
#     return inner
#
#
# @guanjia  # play_dnf = guanjia(play_dnf)
# def play_dnf(username, password):
#     print("我要开始玩儿dnf了. ", username, password)
#     print('你好啊, 我叫赛利亚, 今天又是美好的一天!')
#
#
# @guanjia
# def play_lol(username, password, hero):
#     print("我要开始玩儿lol了. ", username, password, hero)
#     print("德玛西亚!!!!!!")
#
#
# play_dnf("admin", "123465")  # inner
# play_lol("admin", "456789", "大盖伦")



# def guanjia(game):
#     def inner(*args, **kwargs):
#         print("打开外挂")
#         ret = game(*args, **kwargs)  # 这里是目标函数的执行, 这里是能够拿到从目标函数返回的返回值的.
#         print('关闭外挂')
#         return ret
#     return inner
#
#
# @guanjia
# def play_dnf(username, password):
#     print("我要开始玩儿dnf了. ", username, password)
#     print('你好啊, 我叫赛利亚, 今天又是美好的一天!')
#     return "一把屠龙刀"
#
#
# def play_lol(username, password, hero):
#     print("我要开始玩儿lol了. ", username, password, hero)
#     print("德玛西亚!!!!!!")
#
#
# ret = play_dnf("admin", "123465")  # inner
# print(ret)



# def wrapper1(fn):  # fn: wrapper2.inner
#     def inner(*args, **kwargs):
#         print("这里是wrapper1 进入")  # 1
#         ret = fn(*args, **kwargs)  # wrapper2.inner
#         print("这里是wrapper1 出去")  # 5
#         return ret
#     return inner
#
# def wrapper2(fn):  # fn: target
#     def inner(*args, **kwargs):
#         print("这里是wrapper2 进入")  # 2
#         ret = fn(*args, **kwargs)  # taget
#         print("这里是wrapper2 出去")  # 4
#         return ret
#     return inner
#
#
# @wrapper1  # target = wrapper1(wrapper2.inner)   =>  target: wrapp1.inner
# @wrapper2  # target = wrapper2(target)   => target: wrapper2.inner
# def target():
#     print('我是目标')  # 3
#
# target()

"""
这里是wrapper1 进入
这里是wrapper2 进入
我是目标
这里是wrapper2 出去
这里是wrapper1 出去
"""
login_flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag == False:  # ????
            # 这里完成登录校验
            print('还未完成用户登录操作')
            while 1:
                username = input(">>>")
                password = input(">>>")
                if username == "admin" and password == "123":
                    print("登录成功")
                    login_flag = True
                    break
                else:
                    print("登录失败, 用户名或密码错误")
        ret = fn(*args, **kwargs)  # 后续程序的执行
        return ret
    return inner




@login_verify
def add():
    print("添加员工信息")

@login_verify
def delete():
    print("删除信息")

@login_verify
def upd():
    print("修改信息")

@login_verify
def search():
    print("查询员工信息")


add()
upd()
delete()
search()



