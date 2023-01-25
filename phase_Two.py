


import matplotlib.pyplot as plt
import random
import math


x = []
y = []
closest_3_points = []
dist = []
index = []
chunk_index = []
close_point_index = []
unsorted_dist = []
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

     for j in range(0,tot_points,1):
          #print("x1 - ",x[i],"|y1 - ", y[i],"|x2 - ", x[j],"|y2 - ",  y[j])
          dist_calc = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
          print("distance of point ",i+1," from ", j+1, " - ", dist_calc)

          #all the distances of current point to all other points stored in list 'dist'.
          dist.append(dist_calc)

print("list of distances - ",dist)
print("no of elements - ", len(dist))

#take 3 closest distances to another points from current_working_point
unsorted_dist = dist.copy()
dist.sort()      #sorting the list to get the lowest values first in list.


#here we have the sorted and unsorted list both of distances of each element
#we have to divide the unsorted list into 10-10 seperate lists or elements and
#then have next functions run on these consecutive lists/funcs.
#sorted list will be useless right now

for i in range(0, len(unsorted_dist), 10):

    chunk = unsorted_dist[i:i + 10]
    print("chunk ",int((i+10)/10)," - ", chunk)



#------------------------------------------------------------------#

for i in range(0, tot_points):                                          #3rd LOOP
    for j in range(0, 3):
     #appending distance from current_working_point to first 3 elements in the list 'closest_3_points'.
        closest_3_points.append(chunk[j])

#print("\nDistance from CWP to closest points - ",closest_3_points)



#we have all the distances now and we can sort the 3 best distances too
#but now we have to find the index of the 3 best distances in the unsorted list
#so that we can come to know that which point is the closest from current_working_point.


for i in range(0, tot_points):                                          #4th LOOP
    for j in range(0, 3):

     #adding index of closest points to "index".

        close_point_index = unsorted_dist.index(closest_3_points[i])
        close_point_chunk_index = unsorted_dist.index(closest_3_points)
         #print(i,"th closest point index - ",close_point_index)
        index.append(close_point_index)
        chunk_index.append(close_point_chunk_index)

     #we have now got the index of the closest points from original list.
#print("Index of the closest 3 points in array is - ", index)


#plotting lines to 3 closest points from current_working_point.


#line 1
for i in range(0,tot_points):                               #5th LOOP
    for j in range(0, 3):
         a = chunk_index[j]
         plt.plot([x[i],x[a+1]], [y[i],y[a+1]])


# To show the plot

plt.show()

#GG