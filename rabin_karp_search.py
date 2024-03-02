import timeit


# Створюємо поліноміальний хеш рядка
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


# Алгоритм Рабіна-Карпа
def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


first_valid_pattern = "логарифмічний"
invalid_pattern = "developer"

with open("article1.txt", "r") as file:
    first_txt = file.read()

first_valid_position = timeit.timeit(
    lambda: rabin_karp_search(first_txt, first_valid_pattern), number=10
)
first_invalid_position = timeit.timeit(
    lambda: rabin_karp_search(first_txt, invalid_pattern), number=10
)

print(f"First valid pattern position: {first_valid_position}")
print(f"First invalid pattern position: {first_invalid_position}")


second_valid_pattern = "ефективності"

with open("article2.txt", "r") as file:
    second_txt = file.read()

second_valid_position = timeit.timeit(
    lambda: rabin_karp_search(second_txt, second_valid_pattern), number=10
)
second_invalid_position = timeit.timeit(
    lambda: rabin_karp_search(second_txt, invalid_pattern), number=10
)

print(f"Second valid pattern position: {second_valid_position}")
print(f"Second invalid pattern position: {second_invalid_position}")
