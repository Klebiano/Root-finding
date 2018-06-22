import matplotlib.pyplot as plt
from numpy import linspace



def secante(f, x1, x2, tol=0.0001, MIter=100):
    i = 0

    f1 = f(x1)
    f2 = f(x2)

    x3 = x2 - ((f2)*(x2-x1))/(f2-f1)


    if f1*f2 > 0:
        print('A raíz não está presente no intervalo dado.')

    if abs(f(x3)) < tol:
        print(f'A raíz é: {x3}')

    while abs(f(x3)) > tol and i <= MIter:

        x3 = x2 - ((f2) * (x2 - x1)) / (f2 - f1)

        x1 = x2
        x2 = x3
        f1 = f(x1)
        f2 = f(x2)
        i += 1

    print(f'A raíz é: {x3}')
    print(f'Iterações realizadas: {i}')


def f(x): # função
    #return x**3 - x - 2
    #return (x + 3) * ((x - 1) ** 2)
    return x ** 3 - 9 * x + 5
    #return (x**2) - 5*x + 6
    #return 10 - x - (1e3)*(0.1e-6)*((exp(x/(26e-3))) - 1)


res = secante(f, 1, 3)

res

z = linspace(-5, 5, 100)

plt.plot(z, f(z), '-g')
plt.grid()
plt.show()