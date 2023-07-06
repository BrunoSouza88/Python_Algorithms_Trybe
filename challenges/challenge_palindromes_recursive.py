def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if low_index >= high_index:
        return True
    first_letter = word[low_index]
    last_letter = word[high_index]
    if first_letter == last_letter:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
