"""
    1. 字符集和编码
    0 1  <=> 1010101010 => 二进制转化成十进制 <=> 88
    电脑如何进行存储文字信息
    1000000  <=> a

    ascii => 编排了128个文字符号. 只需要7个0和1就可以表示了. 01111111  => 1 byte => 8bit

    ANSI => 一套标准, 每个字符 16bit, 2byte  => 65536
    00000000 01111111

    到了中国, gb2312编码, gbk编码(windows 默认的就是这个)
    01000000 01010101  =>  中
    到了日本, JIS编码
    01000000 01010101  =>  え

    Unicode: 万国码.  中文
    早期Unicode没有意识到这个问题. UCS-2 2个字节.
    进行了扩充, UCS-4 4个字节
    00000000 00000000 00000000 01111111

    utf: 是可变长度的unicode. 可以进行数据的传输和存储 -> 行书, 草书, 隶书
    utf-8:   最短的字节长度8
        英文: 8bit, 1byte
        欧洲文字: 16bit, 2byte
        中文: 24bit, 3byte

    utf-16:  最短的字节长度16

    总结:
        1. ascii: 8bit, 1byte
        2. gbk: 16bit,  2byte  windows默认
        3. unicode: 32bit, 4byte(没法用, 只是一个标准)
        4. utf-8:       mac默认
            英文: 8bit, 1byte
            欧洲: 16bit, 2byte
            中文: 24bit, 3byte

        gbk和utf-8不能直接就进行转化.
        我军密码本  -> 文字 -> 敌军密码本
    2. bytes
        程序员平时遇见的所有的数据最终单位都是字节byte

"""

# s = "周杰伦"
# bs1 = s.encode("gbk")  # b'xxxx' bytes类型
# bs2 = s.encode("utf-8")
# print(bs1)
# print(bs2)

# 怎么把一个gbk的字节转化成utf-8的字节
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
# 先变成文字符号(字符串)
s = bs.decode("gbk")   # 解码
bs2 = s.encode("utf-8")  # 重新编码
# print(bs2)

# 1. str.encode("编码")  进行编码
# 2. bytes.decode("编码") 进行解码

s = "abcdefg"
print(s.encode("gbk"))
