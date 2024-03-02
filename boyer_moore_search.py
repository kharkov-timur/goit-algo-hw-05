import timeit


# Створення таблиці зсувів для алгоритму Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table


# Алгоритм пошуку підрядка Боєра-Мура
def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


first_valid_pattern = "логарифмічний"
invalid_pattern = "developer"

with open("article1.txt", "r") as file:
    first_txt = file.read()

first_valid_position = timeit.timeit(
    lambda: boyer_moore_search(first_txt, first_valid_pattern), number=10
)
first_invalid_position = timeit.timeit(
    lambda: boyer_moore_search(first_txt, invalid_pattern), number=10
)

print(f"First valid pattern position: {first_valid_position}")
print(f"First invalid pattern position: {first_invalid_position}")


second_valid_pattern = "ефективності"

with open("article2.txt", "r") as file:
    second_txt = file.read()

second_valid_position = timeit.timeit(
    lambda: boyer_moore_search(second_txt, second_valid_pattern), number=10
)
second_invalid_position = timeit.timeit(
    lambda: boyer_moore_search(second_txt, invalid_pattern), number=10
)

print(f"Second valid pattern position: {second_valid_position}")
print(f"Second invalid pattern position: {second_invalid_position}")
