from numpy import linspace
import matplotlib.pyplot as plt


def brent(f, x1, x2, MIter=500, tol=0.0001):

    f1 = f(x1)
    f2 = f(x2)
    x3 = x1
    f3 = f1
    i = 0

    if abs(f3) < abs(f2):
        x1 = x2
        x2 = x3
        x3 = x1
        f1 = f2
        f2 = f3
        f3 = f1

    m = 0.5 * (x3 - x2)

    while abs(m) > tol and f2 != 0 and i <= MIter:

        # Inicia pelo método da bisseção

        if abs(x2 - x1) < tol or abs(f1) <= abs(f2):

            m = 0.5 * (x3 - x2)
            d = m

        if x1 == x3:
                                        #Interpolação Linear
            p = 2 * m * (f2 / f1)
            q = 1 - (f2 / f1)

        else:
                                        #interpolação quadrática inversa

            p = (f2 / f1) * (2 * 0.5 * (x3 - x2) * f1 / f3 * (f1 / f3 - f2 / f3) - (x2 - x3) * (f2 / f3 - 1))
            q = (f1 / f3 - 1) * (f2 / f3 - 1) * ((f2 / f1) - 1)

        if p > 0:
            q = -q

        else:
            p = -p

        s = (x2 - x1)
        m = 0.5 * (x3 - x2)

        if 2 * p < 3 * m * q - abs(tol * q) or p < abs(0.5 * s * q):
            d = p / q

        else:

            m = 0.5 * (x3 - x2)
            d = s = m

        x1 = x2
        f1 = f2

        if abs(d) > tol:

            x2 += d

        elif m > 0:

            x2 += tol

        else:

            x2 += -tol

        f2 = f(x2)

        if f2 * f3 > 0:

            x3 = x1
            f3 = f1
            d = x2 - x1

        if abs(f3) < abs(f2):

            x1 = x2
            x2 = x3
            x3 = x1
            f1 = f2
            f2 = f3
            f3 = f1

        m = 0.5 * (x3 - x2)
        i += 1
        print(x2)

    print('Número de iterações feitas: {}'.format(i))
    print('A raiz encontrada é: {}'.format(x2))



def f(x):
    #return x**3 - x - 2
    #return (x + 3) * ((x - 1) ** 2)
    return x**3 - 9*x + 5
    #return (x**2) - 5*x + 6

res = brent(f, 1, 5)

res

z = linspace(-5, 5, 100)
y = f(z)

plt.figure(1)
plt.plot(z, y, '-g')
plt.grid()
plt.show()

