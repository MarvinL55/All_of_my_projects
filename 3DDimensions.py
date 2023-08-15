from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.axes(projection = '3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
ax.scatter(x,y,z,c = c)

ax.set_title('3d Scatter plot marvin')
plt.show()