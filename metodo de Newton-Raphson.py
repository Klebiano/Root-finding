from numpy import exp, linspace
import matplotlib.pyplot as plt


def f(x): # função
    # return x**3 - x - 2
    # return (x + 3) * ((x - 1) ** 2)
    #return x ** 3 - 9 * x + 5
    # return (x**2) - 5*x + 6
    return 10 - x - (1e3)*(0.1e-6)*((exp(x/(26e-3))) - 1)


def fder(x): # derivada da função
    #return 3*(x**2) - 1
    #return (x-1)**2+(x+3)*(2x-2)
    #return 3*(x**2) - 9
    #return 2*x - 5
    return -((exp((500 * x) / 13) / 260) - 1)


def newton(f, fder, x1, x2, tol=0.0001, MIter=100):

    i = 0

    xInicio = (x2+x1)*0.5

    if abs(f(xInicio)) < tol:
        print('A raíz é {}'.format(xInicio))
        print('Número de iterações necessárias: {}'.format(i))
        return

    while abs(f(xInicio)) > tol and i <= MIter: #loop
        xProx = xInicio - f(xInicio) / fder(xInicio)
        xInicio = xProx
        i += 1

    if i >= MIter:
        print('Excedido o número de iterações máximo')

    print('A raíz é: {}'.format(xInicio))
    print('Número de iterações necessárias: {}'.format(i))


res = newton(f, fder, 1, 3)

res

z = linspace(-5, 5, 100)

plt.plot(z, f(z), '-g')
plt.grid()
plt.show()