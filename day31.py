import math

landmarks = [(1, 2), (4, 6), (8, 10)]
distance = 0

for i in range(len(landmarks) - 1):
    x1, y1 = landmarks[i]
    x2, y2 = landmarks[i + 1]
    distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(round(distance, 2))
