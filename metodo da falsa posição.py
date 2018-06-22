from numpy import linspace
import matplotlib.pyplot as plt


def falsa(f, x1, x2, tol=0.0001, MIter=100):

    f1 = f(x1)
    f2 = f(x2)
    i = 0


    if f1 * f2 > 0.0:
        print('A raíz não esta contida no intervalo dado')

    while i <= MIter:

        x3 = x2 - f2 * (x2 - x1) / (f2 - f1)
        if min(abs(x3 - x2), abs(x3 - x2)) < tol:
            print('A raíz é {}'.format(x3))
            print('Número de iterações necessárias: {}'.format(i))
            return

        f3 = f(x3)

        if abs(f3) < tol:
            print('A raíz é {}'.format(x3))
            print('Número de iterações necessárias: {}'.format(i))
            return

        if f1 * f3 > 0:

            x1 = x3
            f1 = f3

        else:
            x2 = x3
            f2 = f3

        i += 1



def f(x):
    #return x**3 - x - 2
    #return (x + 3) * ((x - 1) ** 2)
    return x**3 - 9*x + 5
    #return (x**2) - 5*x + 6

res = falsa(f, 1, 3)

res

z = linspace(-5, 5, 100)

plt.plot(z, f(z), '-g')
plt.grid()
plt.show()