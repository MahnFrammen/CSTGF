#Zach Pedersen
#This is my work!
#Prof Citro
#CST-305

#Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import warnings
def fxn():
    warnings.warn("deprecated", DeprecationWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

#Greens Function
#Initial Conditions applied
#Sets all equal to zero
x = 0
y0 = 0
y1 = 0

#Initial models for given ODEs
def dU0_dx(U, x):
    return [U[1], -2 * U[1] + 2 * x - 2]
def dU1_dx(U, x):
    return [U[1], 4 - U[0]]
#Results from Part 1
def FirstRes(x):
    return (0.5 * pow(x, 2)) - (1.5 * x) - (0.75 * np.exp(-2 * x)) + 0.75
def SecondRes(x):
    return 4 - (4 * np.cos(x))

#ODEINT
#Vectors for values of y and y'
U0 = [0, 0]
xsp0 = np.linspace(0, 10, 250)
ysp0 = odeint(dU0_dx, U0, xsp0)
ysp0 = ysp0[:,0]
U1 = [0, 0]
xsp1 = np.linspace(0, 10, 250)
ysp1 = odeint(dU1_dx, U1, xsp1)
ysp1 = ysp1[:,0]

#Data arrays
xsp2 = []
ysp2 = []
xsp3 = []
ysp3 = []

#Function to run loop 250 times
#Adds Values to x and y space and updates Values
for i in range(0, 250):
    xsp2.append(x)
    ysp2.append(y0)
    xsp3.append(x)
    ysp3.append(y1)
    y0 = FirstRes(x)
    y1 = SecondRes(x)
    x += 0.1

#Plotting Section
#First ODE
plt.plot(xsp0,ysp0,'g-',label = "ODEint 1",linewidth = 3)
plt.plot(xsp2,ysp2,'b:',label = "First Function",linewidth = 2)
plt.suptitle("First ODE")
plt.legend()
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

#Second ODE
plt.plot(xsp1,ysp1,'g-',label = "ODEint 2",linewidth = 3)
plt.plot(xsp3,ysp3,'b:',label = "Second Function",linewidth = 2)
plt.suptitle("Second ODE")
plt.legend()
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

#Function for plotting the difference graph
diff = [] #array to store difference
for i in range(len(xsp0)):
    diff.append(xsp0[i]-ysp0[i])
plt.plot(ysp0,diff)
plt.suptitle("Difference")
plt.xlabel("x Points")
plt.ylabel("Difference between ODE and Green's")
plt.show()