from math import *
from matplotlib import pyplot as plt


# функция, задающая правую часть
# дифференциального уравнения y' = f(x, y)
def firstRhs(x, y):
    return (y ** 2 - y) / x


def secondRhs(x, y):
    return cos(y - x) - 1


# def yetAnotherExampleRhs(x, y):
# return sin(y)

def eulerStep(rhs, step, x0, y0):
    return y0 + step * rhs(x0, y0)


N = 40  # количество узлов для сетки численного решения
dx = 1  # шаг интегрирования по независимой переменной
xPrev = 1
yPrev = 0.1
xs = [xPrev]
ys = [yPrev]

# rhs = secondRhs
rhs = secondRhs

for i in range(N):
    xNext = xPrev + dx
    yNext = eulerStep(rhs, dx, xPrev, yPrev)
    xs.append(xNext)
    ys.append(yNext)
    print(f'solution({xNext}) = {yNext}')
    xPrev, yPrev = xNext, yNext

plt.plot(xs, ys, marker='.', markersize=2)
plt.savefig('test.pdf')
