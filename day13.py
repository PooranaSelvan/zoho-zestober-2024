buildingHeights = [3, 1, 5, 2, 6]
horizonPoints = []
maxHeight = -1

for i in range(len(buildingHeights)):
    if buildingHeights[i] > maxHeight:
        horizonPoints.append(i)
        maxHeight = buildingHeights[i]

print(horizonPoints)
