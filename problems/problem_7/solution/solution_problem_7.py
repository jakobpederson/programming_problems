def find_pairs(values, target=10):
    existing_numbers = {i: key for key, i in enumerate(values)}
    result = set()
    for position in range(len(values)):
        number = target - values[position]
        if number in existing_numbers and existing_numbers[number] != position:
            result.add((min(values[position], number), max(values[position], number)))
    return list(result)
