scene = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
factor = 3

res = []

for i in scene:
    row = []
    for j in i:
        print(j)
        row.append(j * factor)
    res.append(row)

print(res)
