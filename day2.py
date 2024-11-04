def newEle(caves,knowElements):
  res = []
  
  for i in caves:
    for j in i:
      if j not in knowElements:
        if j not in res:
          res.append(j)
  return res
  
caves = [["gold", "silver", "emerald"], ["emerald", "diamond", "ruby"], ["sapphire", "silver", "platinum"]]
knowElements = ["gold", "silver", "platinum"]
response = newEle(caves,knowElements)
print(response)