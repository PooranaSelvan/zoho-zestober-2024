def find_combinations(snacks, target_spiciness, current_combination=[], start_index=0):
    if target_spiciness == 0:
        return [current_combination]
    if target_spiciness < 0:
        return []

    combinations = []
    for i in range(start_index, len(snacks)):
        snack_name, spiciness = snacks[i]
        combinations += find_combinations(snacks, target_spiciness - spiciness, current_combination + [snack_name], i)
    return combinations


snacks = [("Samosa", 5), ("Ketchup", 2), ("Chips", 3), ("Spicy Nuts", 4)]
target_spiciness = 7

result = find_combinations(snacks, target_spiciness)
print(len(result))