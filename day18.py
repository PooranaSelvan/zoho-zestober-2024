# distance = 400
# fuel = 17
distance = 900
fuel = 90


res = distance / 30

if distance <= 30:
     print(True)
else:
     if int(res) * 2 <= fuel:
          print(True)
     else:
          print(False)