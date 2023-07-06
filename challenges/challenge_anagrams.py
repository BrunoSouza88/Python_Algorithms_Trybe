from challenges.util.selection_sort import quicksort


def is_anagram(first_string, second_string):
    first_string_sorted = "".join(quicksort(first_string.lower()))
    second_string_sorted = "".join(quicksort(second_string.lower()))
    are_anagrams = first_string_sorted == second_string_sorted

    if first_string and second_string:
        return (first_string_sorted, second_string_sorted, are_anagrams)

    if not first_string:
        return (first_string, second_string_sorted, False)

    if not second_string:
        return (first_string_sorted, second_string, False)
