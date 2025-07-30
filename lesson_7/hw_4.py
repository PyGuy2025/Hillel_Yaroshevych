def common_elements() -> set:
    first_set = set(range(0, 101, 3))
    second_set = set(range(0, 101, 5))
    result = first_set.intersection(second_set)
    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}