from numpy import abs


def func(x):
    return x*x+-2


def proizv(x):
    return 2*x


eps = 0.00000000000001
x = -10
x1 = x - (func(x) / proizv(x))
i = 0
k = 0
print('\n       Корни      | Итерации | Оценка погрешности')
while i < 2:
    while abs(x-x1) > eps:
       x = x1
       x1 = x - (func(x) / proizv(x))
       k = k + 1
    print('%-18.14f|    %-6d| %-25.24f ' % (x, k, abs(x-x1)))
    k = 0
    x = 10
    x1 = x - (func(x) / proizv(x))
    i = i+1




