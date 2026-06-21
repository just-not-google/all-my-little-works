# 1 -------------------------------------------------
def the_sum_of_two_numbers(a: float, b:float):
    try:
        return a + b
    except Exception as e:
        return e

print(the_sum_of_two_numbers(1, 2))


# 2 -------------------------------------------------
def maximum_of_two_numbers(a: float, b:float):
    try:
        return max(a, b)
    except Exception as e:
        return e

print(maximum_of_two_numbers(4, 2))


# 3 -------------------------------------------------
def the_factorial_of_a_number(a:int):
    try:
        i = 0
        fact_orial = 1
        lst = []
        for i in range(a):
            i += 1
            lst.append(i)

        for i in lst:
            fact_orial *= i
        return fact_orial
    except Exception as e:
        return e

print(the_factorial_of_a_number(5))


# 4 -------------------------------------------------
def even_or_odd(n:int):
    try:
        if n % 2 == 0:
            return True
        elif n % 2 != 0:
            return False
    except Exception as e:
        return e

print(even_or_odd(2))


# 5 -------------------------------------------------
def the_sum_of_the_numbers_from_1_to_n(n: int):
    try:
        lst = []
        for i in range(1, n):
            lst.append(i)
        return sum(lst)
    except Exception as e:
        return e

print(the_sum_of_the_numbers_from_1_to_n(5))


# 6 -------------------------------------------------
def find_the_minimum_in_the_list(lst: list[int]):
    try:
        return min(lst)
    except Exception as e:
        return e

print(find_the_minimum_in_the_list([1, 3, 5]))


# 7 -------------------------------------------------
def counting_characters_in_a_string(s: str):
    try:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    except Exception as e:
        return e

print(counting_characters_in_a_string("Ddd"))


# 8 -------------------------------------------------
def line_reversal(s: str):
    try:
        return s[::-1]
    except Exception as e:
        return e

print(line_reversal("Ddd"))


# 9 -------------------------------------------------
def checking_for_a_palindrome(s: str):
    try:
        if s == s[::-1]:
            return True
        elif s != s[::-1]:
            return False
    except Exception as e:
        return e

print(checking_for_a_palindrome("madam"))


# 10 -------------------------------------------------
def squares_of_numbers(n: int):
    try:
        lst = []

        for i in range(1, n+1):
            lst.append(i ** 2)
        return lst
    except Exception as e:
        return e

print(squares_of_numbers(4))


# 11 -------------------------------------------------
def counting_vowels(s: str):
    try:
        y = s.lower().replace("", " ").split()
        vow = ["a", "e", "i", "o", "u"]
        j = 0
        for i in y:
            if i in vow:
                j += 1
        return j
    except Exception as e:
        return e

print(counting_vowels("hello"))


# 12 -------------------------------------------------
def the_average_value_of_the_list(lst: list[int]):
    try:
        return sum(lst) / 2
    except Exception as e:
        return e

print(the_average_value_of_the_list([1, 2, 3]))


# 13 -------------------------------------------------
def filtering_even_numbers(lst: list[int]):
    try:
        y = []
        for i in lst:
            if i % 2 == 0:
                y.append(i)
        return y
    except Exception as e:
        return e

print(filtering_even_numbers([1, 2, 3, 4]))


# 14 -------------------------------------------------
def checking_a_prime_number(n: int):
    try:
        if n <= 1:
            return False
        for d in range(2, n):
            if n % d == 0:
                return False
        return True
    except Exception as e:
        return e

print(checking_a_prime_number(5))


# 15 -------------------------------------------------
def combining_two_lists(lst_1: list, lst_2: list):
    try:
        return lst_1 + lst_2
    except Exception as e:
        return e

print(combining_two_lists([1, 2], [3, 4]))


# 16 -------------------------------------------------
def searching_for_the_element_index(lst: list[int], x: int):
    try:
        if x in lst:
            for i in range(len(lst)):
                if lst[i] == x:
                    return i
        else:
            return -1
    except Exception as e:
        return e

print(searching_for_the_element_index([1, 2, 4], 4))


# 17 -------------------------------------------------
def removing_duplicates(lst: list):
    try:
        return list(set(lst))
    except Exception as e:
        return e

print(removing_duplicates([1, 2, 2, 3, 3]))


# 18 -------------------------------------------------
def counting_words_per_line(s: str):
    try:
        return len(s.split())
    except Exception as e:
        return e

print(counting_words_per_line("Hello world"))


# 19 -------------------------------------------------
def substring_replacement(s: str, old: str, new: str):
    try:
        return s.replace(old, new)
    except Exception as e:
        return e

print(substring_replacement("hello world", "hello", "hi"))


# 20 -------------------------------------------------
def checking_for_anagram(s_1: str, s_2: str):
    try:
        y = sorted(s_1.lower().replace("", " ").split())
        x = sorted(s_2.lower().replace("", " ").split())
        if y == x:
            return True
        elif y != x:
            return False
    except Exception as e:
        return e

print(checking_for_anagram("silent", "listen"))


# 21 -------------------------------------------------
def list_reversal(lst: list):
    try:
        return lst[::-1]
    except Exception as e:
        return e

print(list_reversal([1, 2, 3]))


# 22 -------------------------------------------------
def counting_element_occurrences(lst: list[int], x: int):
    try:
        j = 0
        for i in lst:
            if x == i:
                j += 1
        return j
    except Exception as e:
        return e

print(counting_element_occurrences([1, 2, 3, 4, 4], 4))


# 23 -------------------------------------------------
def string_concatenation(s_1: str, s_2: str):
    try:
        return s_1 + " " + s_2
    except Exception as e:
        return e

print(string_concatenation("Hello", "world"))


# 24 -------------------------------------------------
def node_search(a: int, b: int):
    try:
        while b != 0:
            a, b = b, a % b
        return a
    except Exception as e:
        return e

print(node_search(2, 4))


# 25 -------------------------------------------------
def fibonacci_numbers(n: int):
    try:
        if n <= 1:
            return n
        return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)
    except Exception as e:
        return e

print(fibonacci_numbers(4))


# 26 -------------------------------------------------
def the_sum_of_the_digits_of_a_number(n: int):
    try:
        y = str(n).replace("", " ").split()
        x = []
        for i in y:
            i = int(i)
            x.append(i)
        return sum(x)
    except Exception as e:
        return e

print(the_sum_of_the_digits_of_a_number(123))


# 27 -------------------------------------------------
def checking_the_power_of_two(n: int):
    try:
        if n <= 0:
            return False
        elif n & (n-1) == 0:
            return True
        else:
            return False
    except Exception as e:
        return e

print(checking_the_power_of_two(128))


# 28 -------------------------------------------------
def generating_prime_numbers(n: int):
    try:
        primes = []
        num = 2
        while len(primes) < n:
            if checking_a_prime_number(num):
                primes.append(num)
            num += 1
        return primes
    except Exception as e:
        return e

print(generating_prime_numbers(14))


# 29 -------------------------------------------------
def searching_for_a_missing_number(lst: list[int], n: int):
    try:
        y = [x for x in range(1, n+1)]
        if len(y) > len(lst):
            return sum(y) - sum(lst)
        elif len(y) == len(lst):
            return 0
        else:
            return False
    except Exception as e:
        return e

print(searching_for_a_missing_number([1, 2, 4], 4))


# 30 -------------------------------------------------
def checking_for_an_ascending_list(lst: list[int]):
    try:
        if len(lst) == 1:
            return True
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                return False
        return True
    except Exception as e:
        return e

print(checking_for_an_ascending_list([1, 2, 3]))
