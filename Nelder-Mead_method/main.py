
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)

    def get_points(self):
        return (self.x, self.y)

    def get_x(self):
        return(self.x)

    def get_y(self):
        return(self.y)


def f(point):
    x, y = point
    return (x - 1) ** 2 + (y - 2) ** 2


alpha = 1
beta = 2
gamma = 0.5
i = 0
v1 = Vector(0, 0)
v2 = Vector(1.0, 0)
v3 = Vector(0, 1.0)
exp = 0.000001
print("Итерация                 X              Y                   Погрешность")

v = max(abs(v1.get_x() - v2.get_x()), abs(v1.get_y() - v2.get_y()), abs(v1.get_x() - v3.get_x()), abs(v1.get_x() - v3.get_x()))

while v > exp:
    i = i + 1
    addValue = {v1: f(v1.get_points()), v2: f(v2.get_points()), v3: f(v3.get_points())}
    sort = sorted(addValue.items(), key=lambda x: x[1]) #сортировка точек
        # print(adict)
    first = sort[0][0]
    second = sort[1][0]
    xh = sort[2][0]
    xc = (second + first) / 2
    # print("   {0.center(8)}{1}                                         {2}".format(i, first, v))
    print(str(i).center(8),str(first).center(50),str(v).ljust(10))

        # print(mid)

        # отражение
    xr = xc - alpha * (xh - xc)
    if f(xr.get_points()) < f(second.get_points()):
        xh = xr
    else:
        if f(xr.get_points()) < f(xh.get_points()):
            xh = xr
        c = (xh + xc) / 2
        if f(c.get_points()) < f(xh.get_points()):
            xh = c
    if f(xr.get_points()) < f(first.get_points()):   # fe < f1

            # растяжение
        xe = xc + beta * (xr - xc)
        if f(xe.get_points()) < f(xr.get_points()):
            xh = xe
        else:
            xh = xr
    if f(xr.get_points()) > f(second.get_points()):

            # сжатие
        xs = xc + gamma * (xh - xc)
        if f(xs.get_points()) < f(xh.get_points()):
            xh = xs

    #обновление точек
    v1 = xh
    v2 = second
    v3 = first
    v = min(abs(v1.get_x() - v2.get_x()), abs(v1.get_y() - v2.get_y()), abs(v1.get_x() - v3.get_x()),
            abs(v1.get_x() - v3.get_x()))

    # print(first)
    # print(second)
    # print(xh)

print("\nПриближенное значение минимума функции:", first)

