def farm(farm):
    scarecrow = 0
    i = 0
    while i < len(farm):
        if farm[i] == 'C':
            if (i<len(farm)-1 and farm[i+1] == '.'):
                scarecrow += 1
                i += 3
            elif i > 0 and farm[i-1] == '.':
                scarecrow += 1
                i += 2
            else:
                return -1
        else:
            i +=1        
    return scarecrow
farm_1 = 'C..C.C.C..'
print(farm(farm_1))