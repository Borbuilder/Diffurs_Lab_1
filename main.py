from math import *
from matplotlib import pyplot as plt


# функция, задающая правую часть
# дифференциального уравнения y' = f(x, y)
def firstRhs(x, y):
    return y-x**2


def secondRhs(x, y):
    return (x+3-2*y)/2

def thirdRhs(x, y):
    return (((x**2) + (y**2))/2)-1

def forthRhs(x, y):
    return -x + sqrt(x**2 + 2*y)

def fifthRhs(x, y):
    return y/(x*(2*x*y + 1))

# def yetAnotherExampleRhs(x, y):
# return sin(y)

def eulerStep(rhs, step, x0, y0):
    return (y0 + step * rhs(x0, y0))


N = 100 # количество узлов для сетки численного решения
dx = 0.1  # шаг интегрирования по независимой переменной
xPrev = 0.01
yPrev = -0.01
xs = [xPrev]
ys = [yPrev]


rhs = fifthRhs

for i in range(N):
    xNext = xPrev + dx
    yNext = eulerStep(rhs, dx, xPrev, yPrev)
    xs.append(xNext)
    ys.append(yNext)
    print(f'solution({xNext}) = {yNext}')
    xPrev, yPrev = xNext, yNext

plt.plot(xs, ys, marker='.', markersize=2)
plt.savefig('test.pdf')
