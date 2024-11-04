def balance_bowing(bowing_pattern):
    down_count = bowing_pattern.count('D')
    up_count = bowing_pattern.count('U')
    
    if down_count == up_count or down_count == up_count + 1 or up_count == down_count + 1:
        return (True, bowing_pattern)
    
    modified_pattern = list(bowing_pattern)
    if down_count > up_count:
        extra_downs = (down_count - up_count) // 2
        changes_made = 0
        
        for i in range(0, len(modified_pattern), 2):
            if modified_pattern[i] == 'D' and changes_made < extra_downs:
                modified_pattern[i] = 'U'
                changes_made += 1
    else:
        extra_ups = (up_count - down_count) // 2
        changes_made = 0
        
        for i in range(1, len(modified_pattern), 2):
            if modified_pattern[i] == 'U' and changes_made < extra_ups:
                modified_pattern[i] = 'D'
                changes_made += 1
    
    new_down_count = modified_pattern.count('D')
    new_up_count = modified_pattern.count('U')
    
    if new_down_count == new_up_count or new_down_count == new_up_count + 1 or new_up_count == new_down_count + 1:
        return (True, ''.join(modified_pattern))
    else:
        return (False, bowing_pattern)

print(balance_bowing("DUDUUUUUD"))
print(balance_bowing("DUDUUDUD")) 