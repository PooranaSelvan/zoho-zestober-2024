remote_position = (2, 3)
remote_range = 4
tv_position = (2, 6)

remote_row, remote_col = remote_position
tv_row, tv_col = tv_position

if remote_row == tv_row:
    distance = abs(remote_col - tv_col)
    res = distance <= remote_range
elif remote_col == tv_col:
    distance = abs(remote_row - tv_row)
    res = distance <= remote_range
else:
    res = False

print(res)