#Zach Pedersen, Rylan Casanova
#This is our work!
#CST-305
#Prof. Citro

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def dudx1(u, x):
    return [u[1], -2 * u[1] - u[0] + 2 * x]
def dudx2(u, x):
    return [u[1], 0 * u[1] - u[0] + x ** 2]
def green1(x):
    return 2 * ((x + 2) * np.exp(-x) + x - 2)
def green2(x):
    return (x ** 2 - 2) * np.sin(x) ** 2 + (x ** 2 - 2) * np.cos(x) ** 2 + 2 * np.cos(x)


# number of points
r = 101
# start conditions
x = np.linspace(0, r - 1, r)
u = [0, 0]

# Calculates with Odeint
uy = odeint(dudx1, u, x)
y = uy[:, 0]


# Plot results (Odeint1)
plt.title('Odeint1')
plt.plot(x, y, label="Odeint1")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# number of points
r = 101
# start conditions
x3 = np.linspace(0, r - 1, r)

# Calculates with Odeint
y3 = green1(x3)

# Plot results (Green1)
plt.title('Green1')
plt.plot(x3, y3, label="Green1", linestyle=":")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Show Odeint and Green together
plt.plot(x, y, label="Odeint1")
plt.plot(x3, y3, label="Green1", linestyle=":")
plt.legend()
plt.show()

# number of points
r = 101
# start conditions
x2 = np.linspace(0, r - 1, r)
u2 = [0, 0]

# Calculates with Odeint
uy2 = odeint(dudx2, u2, x2)
y2 = uy2[:, 0]

# Plot results (Odeint2)
plt.title('Odeint2')
plt.plot(x2, y2, label="Odeint2")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# number of points
r = 101
# start conditions
x4 = np.linspace(0, r - 1, r)

# Calculates with Odeint
y4 = green2(x4)

# Plot results (Green2)
plt.title('Green2')
plt.plot(x4, y4, label="Green2", linestyle=":")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Show Odeint and Green together
plt.plot(x2, y2, label="Odeint2")
plt.plot(x4, y4, label="Green2", linestyle=":")
plt.legend()
plt.show()
