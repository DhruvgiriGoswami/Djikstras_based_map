

import matplotlib.pyplot as plt
import random

x = []
y = []
closest_3_points = []


for i in range(1,21,1):
     x.append(random.randint(1,100))
     y.append(random.randint(1,100))

     plt.text(x[i-1],y[i-1],i)


plt.scatter(x, y, c="blue")
plt.plot(x,y,marker="*")

#take 3 closest distances to another points from active point


# To show the plot
plt.show()