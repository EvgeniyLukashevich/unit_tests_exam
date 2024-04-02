"""Модуль с unit-тестами для класса ListComparator"""

import pytest
from list_utils import ListComparator


def test_compare_averages_list1_greater():
    """Ожидаемый результат: μ первого списка больше"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 4]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_averages() == \
           "Первый список имеет большее среднее значение: 3.0 > 2.8"


def test_compare_averages_list2_greater():
    """Ожидаемый результат: μ второго списка больше"""
    list1 = [1, 2, 3, 4, 4]
    list2 = [1, 2, 3, 4, 5]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_averages() == \
           "Второй список имеет большее среднее значение: 2.8 < 3.0"


def test_compare_averages_lists_equal():
    """Ожидаемый результат: μ списков равны"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_averages() == "Средние значения равны: 3.0 = 3.0"


def test_non_list_argument1():
    """Ожидаемый результат:
    TypeError по причине 'не списка' в качестве первого аргумента"""
    with pytest.raises(TypeError):
        ListComparator(1, [2, 3, 4])


def test_non_list_argument2():
    """Ожидаемый результат:
    TypeError по причине 'не списка' в качестве второго аргумента"""
    with pytest.raises(TypeError):
        ListComparator([1, 2, 3], 4)


def test_non_numbers_list_argument1():
    """Ожидаемый результат:
    TypeError по причине 'не чисел' в качестве элементов первого аргумента"""
    with pytest.raises(TypeError):
        ListComparator([2, 'a', 4], [2, 3, 4])


def test_non_numbers_list_argument2():
    """Ожидаемый результат:
    TypeError по причине 'не чисел' в качестве элементов второго аргумента"""
    with pytest.raises(TypeError):
        ListComparator([2, 3, 4], [2, None, 4])


def test_boolean_lists():
    """Ожидаемый результат: μ второго списка больше"""
    list1 = [False, False, False]
    list2 = [True, True, True]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_averages() == \
           "Второй список имеет большее среднее значение: 0.0 < 1.0"
