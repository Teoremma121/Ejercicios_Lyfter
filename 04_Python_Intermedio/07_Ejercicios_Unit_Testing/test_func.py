# Ejercicios de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de pruebas:

import pytest
import func
from random import shuffle

def test_bubble_sort_with_small_list():
    input_list = [7,4,8,2,6,1,5,3]
    result = func.bubble_sort(input_list)
    assert result == list(range(1,9))

def test_bubble_sort_with_large_list():
    input_list = list(range(1,101))
    shuffle(input_list)
    result = func.bubble_sort(input_list)
    assert result == list(range(1,101))

def test_bubble_sort_with_empty_list():
    input_list = []
    result = func.bubble_sort(input_list)
    assert result == []

def test_buble_sort_with_no_list():
    input_list = "Esto no es una lista"
    with pytest.raises(Exception):
        func.bubble_sort(input_list)

def test_sum_all_numbers_with_all_positive_numbers():
    input_list = [4, 6, 2, 28]
    result = func.sum_all_numbers(input_list)
    assert result == 40

def test_sum_all_numbers_with_some_negative_numbers():
    input_list = [-6, 6, 2, 28, -2]
    result = func.sum_all_numbers(input_list)
    assert result == 28

def test_sum_all_numbers_with_empty_list():
    input_list = []
    result = func.sum_all_numbers(input_list)
    assert result == 0

def test_reverse_text_with_string_1():
    input_string = "romA"
    result = func.reverse_text(input_string)
    assert result == "Amor"

def test_reverse_text_with_string_2():
    input_string = "stnaPerauqS boBegnopS"
    result = func.reverse_text(input_string)
    assert result == "SpongeBob SquarePants"

def test_reverse_text_with_string_3():
    input_string = "ReconoceR"
    result = func.reverse_text(input_string)
    assert result == input_string

def test_count_capital_or_lower_with_all_letters():
    input_string = "Jhon Doe hace Unit Testing"
    result = func.count_capital_or_lower(input_string)
    assert result == (4, 18)

def test_count_capital_or_lower_with_some_numbers():
    input_string = "T0T0r0.C4lc1f3r"
    result = func.count_capital_or_lower(input_string)
    assert result == (3, 5)

def test_count_capital_or_lower_with_empty_string():
    input_string = ""
    result = func.count_capital_or_lower(input_string)
    assert result == (0, 0)

def test_order_alphabetically_with_all_lowers():
    input_string = "python-variable-funcion-computadora-monitor"
    result = func.order_alphabetically(input_string)
    assert result == "computadora-funcion-monitor-python-variable"

def test_order_alphabetically_with_some_capitals():
    input_string = "pineapple-Watermelon-straWberry-Banana-papaya-leMon"
    result = func.order_alphabetically(input_string)
    assert result == "Banana-leMon-papaya-pineapple-straWberry-Watermelon"

def test_order_alphabetically_with_empty_string():
    input_string = ""
    result = func.order_alphabetically(input_string)
    assert result == ""

def test_check_list_for_primes_with_no_primes():
    input_list = [1, 4, 6, 8, 12]
    result = func.check_list_for_primes(input_list)
    assert result == []

def test_check_list_for_primes_with_some_primes():
    input_list = [1, 43, 6, 8, 29, 12, 11]
    result = func.check_list_for_primes(input_list)
    assert sorted(result) == sorted([43, 29, 11])

def test_check_list_for_primes_with_empty_list():
    input_list = []
    result = func.check_list_for_primes(input_list)
    assert result == []


