from numpy import linspace
import matplotlib.pyplot as plt


def pontosf(f, x1, x2, tol= 0.0001, Miter= 100):

    f1 = f(x1)
    f2 = f(x2)
    i = 0

    x3 = (x1 + x2)*0.5
    f3 = f(x3)

    while i <= Miter:

        i += 1

        if min(abs(x3 - x2), abs(x3 - x2)) < tol:
            print('A raíz é {}'.format(x3))
            print('Número de iterações necessárias: {}'.format(i))
            return

        if abs(f3) < tol:
            print('A raíz é {}'.format(x3))
            print('Número de iterações necessárias: {}'.format(i))
            return

        x3 = g(x3)
        f3 = f(x3)

def g(x):


     return ((x**3) + 5)/9
    # return (6+x**2)/5


def f(x):
    # return x**3 - x - 2
    # return (x + 3) * ((x - 1) ** 2)
     return x ** 3 - 9 * x + 5
    # return (x**2) - 5*x + 6

res = pontosf(f, 0.5, 1)

res

z = linspace(-5, 5, 100)

plt.plot(z, f(z), '-g')
plt.grid()
plt.show()