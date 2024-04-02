"""Модуль, содержащий класс ListComparator,
предназначенный для вычисления среднего арифметического
всех элементов двух массивов и их сравнения"""

class ListComparator:
    """Класс, предназначенный для вычисления среднего арифметического
    всех элементов двух массивов и их сравнения"""
    def __init__(self, list1: list[int | float], list2: list[int | float]):
        """
        Инициализатор класса ListComparator,
        принимающий два списка чисел в качестве аргументов.

        :param list1: Первый массив чисел
        :param list2: Второй массив чисел
        """
        if not all(isinstance(lst, list) for lst in [list1, list2]):
            raise TypeError("Оба аргумента должны быть списками.")
        if not all(isinstance(num, (int, float)) for num in list1):
            raise TypeError(f"Все элементы списка должны быть числами: {list1}")
        if not all(isinstance(num, (int, float)) for num in list2):
            raise TypeError(f"Все элементы списка должны быть числами: : {list2}")
        self.list1 = list1
        self.list2 = list2

    def __calculate_average(self, list_obj: list):
        """
        Метод вычисления среднего значения всех элементов списка

        :param list_obj: Массив чисел
        """
        return sum(list_obj) / len(list_obj)

    def compare_averages(self) -> str:
        """
        Метод сравнения среднего значения всех элементов двух списков чисел,
        возвращающий соответствующий результат

        return: Строка с результатом сравнения среднего арифметического двух массивов
        """
        avg_list1 = self.__calculate_average(self.list1)
        avg_list2 = self.__calculate_average(self.list2)
        if avg_list1 > avg_list2:
            return f"Первый список имеет большее среднее значение: {avg_list1} > {avg_list2}"
        if avg_list1 < avg_list2:
            return f"Второй список имеет большее среднее значение: {avg_list1} < {avg_list2}"
        return f"Средние значения равны: {avg_list1} = {avg_list2}"
