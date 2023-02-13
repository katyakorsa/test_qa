from typing import Any, Final

INPUT_LIST: Final[list[dict[str, int]]] = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 5},
    {'c': 4, 'a': 3},
    {'a': 1, 'd': 6},
    {'a': 2, 'b': 2, 'd': 5},
    {'e': 0}
]

REFERENCE_DICT: Final[dict[str, int | list[int]]] = {'a': [1, 2, 3], 'b': 2, 'c': [3, 4], 'd': [5, 6], 'e': 0}

DICT = {'a': 1, 'b': 55, 'c': 39, 'd': -1, 'e': 0, 'f': 12}


def compare(value1: Any, value2: Any) -> str:
    return 'PASS' if value1 == value2 else 'FAIL'


def association(data: list[dict[str, int]]) -> dict[str, int | list[int]]:
    """ Функция для объединения словарей

    :param data: Список словарей
    :return: Объединенный словарь

    """

    merged_dict = {}

    for i in data:
        for key, value in i.items():
            merged_dict[key] = value if key not in merged_dict else [merged_dict[key], value] if isinstance(
                merged_dict[key], int) and value != merged_dict[key] else [*{*merged_dict[key], value}] if isinstance(
                merged_dict[key], list) else merged_dict[key]

    return merged_dict


def min_key(data: dict[str, int]) -> str:
    """ Функция для поиска ключа с минимальным значением """
    min_result = min(data, key=data.get)

    return min_result


def max_key(data: dict[str, int]) -> str:
    """ Функция для поиска ключа с максимальным значением """
    max_result = max(data, key=data.get)

    return max_result


# Тест задачи 1
result_one = association(INPUT_LIST)
print(f"Задача 1: {compare(result_one, REFERENCE_DICT)}")

# Тест задачи 2
result_max_key = max_key(DICT)
print(f"Задача 2 max: {compare(result_max_key, 'b')}")
result_min_key = min_key(DICT)
print(f"Задача 2 min: {compare(result_min_key, 'd')}")
