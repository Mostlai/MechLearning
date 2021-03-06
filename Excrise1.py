import numpy as np
import matplotlib.pyplot as plt

w = 1
b = 1
# 生成数据集的x对应函数
def fun1(x):
    return 3*x+2
# 生成初始函数
def fun_p(x):
    global w
    global b
    return w*x+b
# 画图
def plot_thetahist():
    plt.scatter(x,y,marker='x',label='Dataset')
    plt.plot(x, fun_p(x),'r',label='Fit line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gradient Descent')
    plt.legend()
    plt.show()
# 损失函数
def J(count,all_count):
    a = 0
    while count < all_count:
        a = a + pow(fun_p(x[count]) - y[count], 2)
        count = count + 1
    Jth = a/(2*all_count)
    return Jth
# 拟合w
def GD():
    global w
    step = 1
    now_Jth = 9999999
    last_Jth = 10
    v = 0
    while v <800:
        if now_Jth - last_Jth < 0:
            now_Jth = 999999999
            step = 0.1 * step
            step = -step
            continue
        Jth = J(0, 300)
        now_Jth = Jth
        # print(now_Jth)
        w = w + step
        Jth = J(0, 300)
        last_Jth = Jth
        # print(last_Jth)
        v = v + 1
        # print('__________', now_Jth, last_Jth, w)
				
# 拟合b
def BGD():
    global b
    step = 1
    now_Jth = 9999999
    last_Jth = 10
    v = 0
    while v <300:
        if now_Jth - last_Jth < 0:
            now_Jth = 999999999
            step = 0.1 * step
            step = -step
            continue
        Jth = J(0, 300)
        now_Jth = Jth
        b = b+step
        Jth = J(0, 300)
        last_Jth = Jth
        v = v + 1
        # print('__________', now_Jth, last_Jth, b)

x = np.linspace(-5, 5, 300)
y = fun1(x) + np.random.randn(len(x))
# xy =zip(x,y)
GD()
BGD()
print('y = ',w,'x +',b)
# print(list(xy))
plot_thetahist()
