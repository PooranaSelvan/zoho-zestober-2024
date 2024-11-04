trail = [1, 3, 2, 5, 4, 7]


energy = 0

for i in range(1, len(trail)):
     if trail[i] > trail[i - 1]:
          energy += trail[i] - trail[i - 1]
print(energy)