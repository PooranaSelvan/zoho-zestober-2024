initial_energy = 20
goods = [5, 10, 15]
travel_energy = [5, 10, 8]
trade_energy = [5, 10, 5]


max_goods = 0
    
for i in range(len(goods)):

     if initial_energy >= travel_energy[i]:

         initial_energy -= travel_energy[i]
         max_goods += goods[i]
         initial_energy += trade_energy[i]
    
print(max_goods)
