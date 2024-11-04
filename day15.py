n = int(input("Enter The Number Of Strings:"))
res = []
for i in range(n):
     inp = input(f"Enter The {i + 1} String:")
     res.append(inp)
     res.sort()
print(res)