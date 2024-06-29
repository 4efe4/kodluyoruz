import math  

points = [(1, 2), (3, 4), (6, 8), (2, 1)]


def euclideanDistance(point1, point2):
    
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]
        distance = euclideanDistance(point1, point2)
        distances.append(distance)

minimum_distance = min(distances)
print("Minimum mesafe:", minimum_distance)
