rust_grid = [
[1, 3, 5, 2],
[4, 6, 8, 3],
[7, 2, 1, 5],
[3, 4, 6, 2]
]
max_allowable_rust = 4

count = 0

for i in rust_grid:
     for j in i:
          if j > max_allowable_rust:
               count += 1
print(count)