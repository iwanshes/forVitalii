

import re
from collections import Counter


def test(text: str):
    words = re.findall(r'\w+', text)
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)
    max_value = max(word_counts.values())
    list_result = []
    for key, value in word_counts.items():
        if value == max_value:
            list_result.append(key)

    print(f'{", ".join(list_result)} количество повторений: {max_value}')

test('Hi! How are are you you? Hi! I am okay')
print("*"*20)

# Написать функцию, которая сортирует список с оценками на основе английской системы.
# Всего 5 символов, в порядке убывания: A, B, C, D, F.
#
# Примеры:

# sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
# sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
# sort_grades([]) -> []

def sort_grades(grades: list):
    permitted_grades = ("A", "B", "C", "D", "F", "E")
    final_list = list()
    for item in grades:
        upper_item = item.upper()
        if upper_item not in permitted_grades:
            print(f"Неопознанная отметка: {upper_item}. Символ пропущен.")
        else:
            final_list.append(upper_item)

    print(sorted(final_list, reverse=True))


sort_grades(['b', 'c', 'C', 'f', 'A', 'z'])
print("*"*20)

# Написать функцию, которая проверяет, являются ли две строки анаграммами?
# На вход идут две строки, состоящие из символов английского алфавита.
#
# Примеры:
#
# is_anagram('car', 'tar') -> False
# is_anagram('car', 'cart') -> False
# is_anagram('anagram', 'nagaram') -> True
# is_anagram('beluga', 'begula') -> True

def is_anagram(word_1, word_2):
    print(sorted(word_1) == sorted(word_2))


is_anagram('car', 'tar') # False
is_anagram('car', 'cart') # False
is_anagram('anagram', 'nagaram') # True
is_anagram('beluga', 'begula') # True

print("*"*20)

# Условие:
#
# Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.
#
# Примеры:
#
# sort_array([3, 1]) -> [1, 3]
# sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
# sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]

def sort_array(array):
    dict_even = dict()
    list_not_even = list()
    for pos, item in enumerate(array):
        if item % 2:
            list_not_even.append(item)
        else:
            dict_even[pos] = item

    list_not_even.sort()

    final_list = []
    i = 0
    while i < len(array):
        if i in dict_even.keys():
            final_list.append(dict_even.pop(i))
        else:
            final_list.append(list_not_even.pop(0))
        i += 1
    print(final_list)


sort_array([5, 3, 2, 8, 1, 4])

print("*"*20)


# Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.
#
# Пример:
#
# roman_to_int('XXI') -> 21
# roman_to_int('IV') -> 4
# roman_to_int('I') -> 1

import roman

def roman_to_int(str):
    print(roman.fromRoman(str))


roman_to_int('XXI') # 21
roman_to_int('IV') # 4
roman_to_int('I') # 1