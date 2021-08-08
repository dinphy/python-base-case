# 有趣的正方形螺旋线绘制
import turtle

# 绘制正方形螺旋线
turtle.color('blue') # 线条颜色
for i in range(100):
    turtle.forward(i) # 旋转的步长值，也就是长度，随i的增大而增大
    turtle.left(90) # 旋转的角度,改变角度可以绘制不同的形状
turtle.done()

# 绘制圆
# turtle.circle(60)
# turtle.done()

# 绘制五角星
# for j in range(5):
#     turtle.forward(100)
#     turtle.left(144)
# turtle.done()