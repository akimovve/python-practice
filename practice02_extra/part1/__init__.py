from tasks import *

if __name__ == '__main__':
    # Задача 1
    assert conv_to_int(["2", "13", "1", "0"]) == [2, 13, 1, 0]
    # Задача 2
    assert distinct_el_num(["python", "hello", "world", "python"]) == 3
    # Задача 3
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    # Задача 4
    assert find_idx(4, [0, 4, 1, 4, 4, 2, 4]) == [1, 3, 4, 6]
    # Задача 5
    assert sum_on_even_idx([2, -1, -7, 4, 2, 8, 9, 1]) == 6
    # Задача 6
    assert find_longest_str(["java", "python", "c++", "sql"]) == "python"
    # Задача про 24 символа
    assert shorter() == "much"
    # Задача про генерацию названий групп
    assert generate_groups("ИКБО-01-19") == "К1"
    # Задача, связанная с работой с zip
    assert zip_work() == [
        (77, 3.5, "java"),
        (44, 0.0, "python"),
        (5, -1.0, "kotlin")
    ]
    # Задача о переменном числе параметров в функции
    assert mul_digits(-1, 3, 5, 7, 9) == -945
    # Задача о транспонировании матрицы
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    # Задача о генерациии докладов по цифровой экономике
    for _ in range(5):
        print(digital_economy_report_generator())
    # Задача о реализации своего print()
    print("print():", "java", [1, 2], None, True, sep="\t->\t", end="%\n")
    my_print("my_print():", "java", [1, 2], None, True, sep="\t->\t", end="%\n")
    # Задача о только именованных аргументах
    assert only_named_args(
            group="ИКБО-01-19",
            university="РТУ МИРЭА",
            year=2021) == {
               "group": "ИКБО-01-19",
               "university": "РТУ МИРЭА",
               "year": 2021
           }
    # Задача о генерации многомерного массива
    assert generate_array([1, 2], [3, 4], [5, 6]) == [[1, 2], [3, 4], [5, 6]]

    print("\nAll tests passed")
