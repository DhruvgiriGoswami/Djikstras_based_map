

import matplotlib.pyplot as plt
import random
import math


x = []
y = []


dist = []
unsorted_dist = []
closest_4_Points = []
color = ['b','g','r','c','m',y,'k','w','b','g']

tot_points = 10


#taking random inputs from machine for co-ordinates.
for i in range(1,tot_points+1,1):                                     #1st LOOP
     x.append(random.randint(1,100))
     y.append(random.randint(1,100))
     plt.text(x[i-1],y[i-1],i)

print("x - ",x,"\n","y - ",y)
print("\n\n")


plt.scatter(x, y, c="blue")

#plt.plot(x,y,marker="*")


for i in range(0,tot_points,1):                                      #2nd LOOP
     dist.clear()
     closest_4_Points.clear()
     unsorted_dist.clear()
     for j in range(0,tot_points,1):

         #print("x1 - ",x[i],"|y1 - ", y[i],"|x2 - ", x[j],"|y2 - ",  y[j])
         dist_calc = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
         print("distance of point ",i+1," from ", j+1, " - ", dist_calc)

         #all the distances of current point to all other points stored in list 'dist'.
         dist.append(dist_calc)
         unsorted_dist = dist.copy()

     dist.sort()



     for k in range(0,4):
         closest_4_Points.append(dist[k])
         #print("dist list - ",dist)
         #print("list closest 4 points - ",closest_4_Points)
         index = unsorted_dist.index(closest_4_Points[k])
         print(index)
         plt.plot([x[i],x[index]], [y[i],y[index]])

     print("closest point distances for ",i," - ",closest_4_Points)


print("\nno of elements - ", len(dist),"\n")

plt.show()