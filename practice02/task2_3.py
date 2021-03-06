# Задача 2.3
def f23(table):
    # Удаление пустых столбцов
    for row in table:
        if row[1] is None:
            del row[1]

    # Преобразование 1-ого столбца
    for row in table:
        row[0] = row[0].split(" ")[2]

    # Преобразование 2-ого столбца
    for row in table:
        row[1] = "1" if row[1] == "Выполнено" else "0"

    # Преобразование 3-его столбца
    for row in table:
        arr = row[2].split("/")
        arr.reverse()
        row[2] = ".".join(arr)

    return table

print(f23([
    ["Дмитрий В. Фаробин", None, "Выполнено", "21/02/2004"],
    ["Григорий Е. Букудман", None, "Выполнено", "18/02/2004"],
    ["Рустам С. Фемский", None, "Выполнено", "07/01/2004"],
    ["Ильдар У. Бомянц", None, "Не выполнено", "08/04/2001"]]
))

print(f23([
    ["Владислав Л. Цумидак", None, "Выполнено", "08/02/2004"],
    ["Михаил Ч. Сочогянц", None, "Выполнено", "18/11/2003"],
    ["Игнат У. Согиди", None, "Выполнено", "05/08/2002"],
    ["Андрей Д. Тугацин", None, "Выполнено", "06/02/2003"]]
))
