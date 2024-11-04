panels = [
    {"max_capacity": 100, "efficiency_factor": 0.8},
    {"max_capacity": 150, "efficiency_factor": 0.6},
    {"max_capacity": 200, "efficiency_factor": 0.75}
]

total_energy = 0
    
for i in panels:
    max_capacity = i['max_capacity']
    efficiency_factor = i['efficiency_factor'] 
     

    energyPerPanel = max_capacity * efficiency_factor
     
    total_energy += energyPerPanel
    
print(int(total_energy))