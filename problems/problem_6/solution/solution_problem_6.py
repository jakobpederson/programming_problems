def find_second_largest(values: list):
    largest = float("-inf")
    second_largest = None
    for i in range(len(values)):
        if values[i] > largest:
            second_largest = largest
            largest = values[i]
    return second_largest if isinstance(second_largest, int) else None
