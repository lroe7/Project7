# Lauren Roe
# CST-305
# This is my own work

import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=28, b=2.667):   #defines the lorenz system with arguments x, y, z, s, r, b
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s * (y - x)                 # the first given ODE
    y_dot = r * x - y - x * z           # the second given ODE
    z_dot = x * y - b * z               # the last given ODE
    return x_dot, y_dot, z_dot          # returns xdot, ydot, and zdot


dt = 0.01               # change in time
num_steps = 10000       # number of steps taken

# Need one more for the initial values
xs = np.empty(num_steps + 1)                # create an array for x values
ys = np.empty(num_steps + 1)                # creates an array for y values
zs = np.empty(num_steps + 1)                # creates an array for z values

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)        # sets the initial value of all the arrays

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])       # uses the lorenz system equation to return the ODEs
    xs[i + 1] = xs[i] + (x_dot * dt)                        # finds the next value in the x array
    ys[i + 1] = ys[i] + (y_dot * dt)                        # finds the next value in the y array
    zs[i + 1] = zs[i] + (z_dot * dt)                        # finds the next value in the z array

# Plot
fig = plt.figure()                      # plot the Lorenz system
ax = fig.gca(projection='3d')           # defines the projection type

ax.plot(xs, ys, zs, lw=0.5)             # plots the x y and z values
ax.set_xlabel("X Axis")                 # labels x axis
ax.set_ylabel("Y Axis")                 # labels y axis
ax.set_zlabel("Z Axis")                 # labels z axis
ax.set_title("Lorenz Attractor")        # titles the graph

plt.show()                              # shows the plot

ar = []                     # values of the arrival rate
for i in range(1,16):       # number of customers
    ar.append(i)            # adds numbers 1-15 to the arrival rate array

sd = [2.22, 1.76, 2.13, 0.14, 0.76, 0.7, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27]              # service duration values
ss = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]                 # service staring values
exiting = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]      # exiting values
tiq = [0, 1.22, 1.98, 3.11, 2.25, 2.01,	1.71, 1.18,	0.4, 0,	1.41, 0.82, 0.28, 0.65,	0]                      # time in queue values
nis = [0, 1, 2,	2, 2, 3, 4,	3, 2, 0, 1,	2, 1, 1, 0]                 # number in system values
niq = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]                 # number in queue values

# graph 1 customer arrival time as a function of service start time
plt.plot(ss, ar)                                      # plots customer arrival time as a function of service start time
plt.title('customer arrival time as a function of service start time')      # tiles the graph
plt.xlabel('start time')                                                    # labels the x axis
plt.ylabel('arrival rate')                                                  # labels the y axis
plt.show()                                                                  # shows the plot

# graph 2 the customer arrival time as a function of exit time
plt.plot(exiting, ar)                                 # plots the customer arrival time as a function of exit time
plt.title('customer arrival time as a function of exit time')               # tiles the graph
plt.xlabel('exit time')                                                     # labels the x axis
plt.ylabel('customer arrival time')                                         # labels the y axis
plt.show()                                                                  # shows the plot

# graph 3 the customer arrival time as a function of time in queue
plt.plot(tiq, ar)                                     # plots customer arrival time as a function of time in queue
plt.title('customer arrival time as a function of time in queue')           # titles the graphs
plt.xlabel('time in queue')                                                 # labels the x axis
plt.ylabel('customer arrival time')                                         # labels the y axis
plt.show()                                                                  # shows the plot

# graph 4 the customer arrival time as a function of the number of customers in system
plt.plot(nis, ar)                      # plots customer arrival time as a function of the number of customers in system
plt.title('customer arrival time as a function of the number of customers in system')   # titles the graph
plt.xlabel('customers in system')                                           # labels the x axis
plt.ylabel('customer arrival time')                                         # labels the y axis
plt.show()                                                                  # shows the plot

# graph 5 the customer arrival time as a function of number of customers in queue
plt.plot(niq, ar)                        # plots customer arrival time as a function of number of customers in queue
plt.title('customer arrival time as a function of number of customers in queue')        # titles the graph
plt.xlabel('customers in queue')                                                        # labels the x axis
plt.ylabel('customer arrival time')                                                     # labels the y axis
plt.show()                                                                              # shows the plot
