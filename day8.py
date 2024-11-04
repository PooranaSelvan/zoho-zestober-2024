import math

lst = [{'name':'Charlie','salary':70000,'rating':4},{'name':'Alice','salary':50000,'rating':5},{'name':'bob','salary':60000,'rating':3}]

for i in range(len(lst)):
     if lst[i]['rating'] == 5:
          lst[i]['salary'] += math.floor(lst[i]['salary'] * 20 / 100)
     elif lst[i]['rating'] == 4:
          lst[i]['salary'] += math.floor(lst[i]['salary'] * 10 / 100)
     elif lst[i]['rating'] == 3:
          lst[i]['salary'] += math.floor(lst[i]['salary'] * 5 / 100)
     else:
          lst[i]['salary'] = lst[i]['salary']
     lst[i]['rating'] = 0
print(lst)