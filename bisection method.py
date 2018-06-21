import matplotlib.pyplot as plt
from numpy import linspace


def biss(f, x1, x2, tol=0.0001, MIter=100):

    f1 = f(x1)
    f2 = f(x2)

    x3 = (x2 + x1)*0.5

    i = 0

    if f1*f2 > 0:
        print("A raíz não está contida nesse intervalo")

    if x2 - x1 < tol:
        return x2

    while abs(f(x3)) > tol and i <= MIter:
        if f(x3) * f1 > 0:
            x1 = x3
        else:
            x2 = x3

        x3 = (x2+x1) * 0.5
        i += 1


    print('A raíz é {}'.format(x3))
    print('Número de iterações: {}'.format(i))


def f(x):
    #return x**3 - x - 2
    #return (x + 3) * ((x - 1) ** 2)
    return x**3 - 9*x + 5
    #return (x**2) - 5*x + 6

res = biss(f, 1, 3)

res

z = linspace(-5, 5, 100)

plt.plot(z, f(z), '-g')
plt.grid()
plt.show()
