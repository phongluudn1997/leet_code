def best_sum(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_path = None
    
    for number in numbers:
        remainder = target_sum - number
        remainderCombination = best_sum(remainder, numbers)
        if remainderCombination is not None:
            combination = remainderCombination + [number]
            shortest_path =  combination if shortest_path is None or len(combination) < len(shortest_path) else shortest_path

    return shortest_path
            

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))