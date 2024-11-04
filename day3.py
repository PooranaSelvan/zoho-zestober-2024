trail = [3, 2, 1]
boots = [4, 5, 3]
res = 0
rem = 0
x = 0
for i in range(len(trail)):
  if trail[i] * 2 == boots[i]:
    pass
  elif trail[i] * 2 < boots[i]:
    rem += boots[i] - trail[i] * 2
  elif trail[i] * 2 > boots[i]:
    x += trail[i] * 2 - boots[i]
if rem > x:
  res = rem - x
else:
  res = x - rem
if res == 0:
  print(rem)
else:
  print(-1)