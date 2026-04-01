import matplotlib.pyplot as plt
import numpy as np

# График
def f(x):
    return np.where(x <= 0, (x**2 - 2*x**3) * np.cos(x**2), np.exp(np.sin(2*x)))
x1 = np.linspace(-1.5, 0, 400)
x2 = np.linspace(0.001, 1.5, 400)
y1 = f(x1)
y2 = f(x2)
plt.plot(x1, y1, label = 'f(x) при -1.5 <= x <= 0')
plt.plot(x2, y2, label = 'f(x) при 0 < x <= 1.5')

# Касательная
x0 = 1
y0 = np.exp(np.sin(2*x0))
f_shtrih_x0 = np.exp(np.sin(2*x0)) * np.cos(2*x0) * 2
# y = y0 + f`(x0) * (x - x0)
x_kas = np.linspace(-1.5, 1.5, 100)
y_kas = y0 + f_shtrih_x0 * (x_kas - x0)
plt.plot(x_kas, y_kas, 'g--', label = 'Касательная')
plt.plot(x0, y0, 'ro')

# Оформление
plt.title('График неразрывной функции и касательной')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.annotate(f'Точка касания\n({x0}, {round(y0, 2)})',
             xy=(x0, y0), xytext=(x0+0.2, y0+0.5),
             arrowprops=dict(arrowstyle = 'simple', facecolor='g'))

plt.show()