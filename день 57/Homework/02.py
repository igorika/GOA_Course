def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalpha() or char.isdigit():
            count += 1
    return count