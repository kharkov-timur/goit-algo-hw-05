import timeit


# Створення префіксної таблиці
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# Алгоритм пошуку підрядка Кнута-Морріса-Пратта
def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


first_valid_pattern = "логарифмічний"
invalid_pattern = "developer"

with open("article1.txt", "r") as file:
    first_txt = file.read()

first_valid_position = timeit.timeit(
    lambda: kmp_search(first_txt, first_valid_pattern), number=10
)
first_invalid_position = timeit.timeit(
    lambda: kmp_search(first_txt, invalid_pattern), number=10
)

print(f"First valid pattern position: {first_valid_position}")
print(f"First invalid pattern position: {first_invalid_position}")


second_valid_pattern = "ефективності"

with open("article2.txt", "r") as file:
    second_txt = file.read()

second_valid_position = timeit.timeit(
    lambda: kmp_search(second_txt, second_valid_pattern), number=10
)
second_invalid_position = timeit.timeit(
    lambda: kmp_search(second_txt, invalid_pattern), number=10
)

print(f"Second valid pattern position: {second_valid_position}")
print(f"Second invalid pattern position: {second_invalid_position}")
