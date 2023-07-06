def quicksort(string):
    if len(string) <= 1:
        return string
    pivot = string[len(string) // 2]
    left = [x for x in string if x < pivot]
    middle = [x for x in string if x == pivot]
    right = [x for x in string if x > pivot]
    return quicksort(left) + middle + quicksort(right)
