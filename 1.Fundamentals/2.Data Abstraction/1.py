import random

from algs4.Point2D import Point2D

N = 128
point_list = []
min_distance = float('inf')
for i in range(N):
    x = random.random()
    y = random.random()
    point = Point2D(x, y)
    point_list.append(point)
    if i != 0:
        for j in range(i):
            distance = point.distance_to(point_list[j])
            if distance < min_distance:
                min_distance = distance
                print(min_distance)
print(min_distance)
