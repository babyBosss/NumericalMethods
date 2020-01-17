import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return A * x ** 2 + B * x


# интервал отрисовки графика
xmin = -10.0
xmax = 10.0

# свободные параметры функции
A = 1
B = -1

# область поиска
a = -2
b = 2

x = np.linspace(xmin, xmax, 1000)

k = "0"
while abs(a - b) > 0.000001:
    c = (a + b) / 2.0
    c1 = (a + c) / 2.0
    c2 = (c + b) / 2.0
    if k == "0":
        fc = func(c)
        fc1 = func(c1)
        fc2 = func(c2)
        if fc < fc1:
            # c1 = c
            a = c
            k = "fc1"
        elif fc < fc2:
            # c2 = c
            b = c
            k = "fc2"
        else:
            a = c1
            b = c2
            k = "1"
    else:
        if k == "fc1":
            fc1 = fc
            fc = func(c)
            fc2 = func(c2)
        elif k == "fc2":
            fc2 = fc
            fc = func(c)
            fc1 = func(c1)
        else:
            fc = func(c)
            fc1 = func(c1)
            fc2 = func(c2)

        if fc < fc1:
            a = c
            k = "fc1"
        elif fc < fc2:
            b = c
            k = "fc2"
        else:
            a = c1
            b = c2
            k = "1"

    plt.axvline(a, color='blue', linewidth=1)
    plt.axvline(b, color='blue', linewidth=1)

print('A = ' + str(a), 'B = ' + str(b))
plt.text(0.5, 0.5, '', fontsize=12)
plt.xlabel('x')
plt.ylabel('y')
s = 'Метод дихотомии, Xmin = ' + str(round(a + (a - b) / 2, 6))
plt.title(s)
plt.plot(x, func(x), color='black')
plt.show()