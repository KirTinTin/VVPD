def compare_arrays(array1, array2):
    return array1 == array2


def find_element(array, element):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == element:
                return i, j
    return -1, -1


def find_largest_elements(array):
    flat_array = [element for row in array for element in row]
    sorted_array = sorted(flat_array, reverse=True)
    return sorted_array[:3]


def sum_main_diagonal(array):
    return sum(array[i][i] for i in range(len(array)))


def sum_secondary_diagonal(array):
    return sum(array[i][len(array) - 1 - i] for i in range(len(array)))


def sum_elements_with_even_indices_sum(array):
    return sum(array[i][j] for i in range(len(array)) for j in range(len(array[i])) if (i + j) % 2 == 0)


def reflect_array_vertically(array):
    return [row[::-1] for row in array]


if __name__ == '__main__':
    try:
        rows = int(input("Введите количество строк массива: "))
    except ValueError:
        rows = int(input("Некорректный ввод! Введите число: "))

    try:
        cols = int(input("Введите количество столбцов массива: "))
    except ValueError:
        cols = int(input("Некорректный ввод! Введите число: "))

    array = []
    choice = ""

    for i in range(rows):
        row = []
        for j in range(cols):
            try:
                value = int(input(f"Введите значение элемента [{i}][{j}]: "))
            except ValueError:
                value = int(input("Некорректный ввод! Введите число: "))
            row.append(value)
        array.append(row)

    print("Введенный двумерный массив: ")
    for row in array:
        print(row)

    while True:
        print("\nВыберите операцию:")
        print("1. Сравнение двух массивов")
        print("2. Поиск элемента в массиве")
        print("3. Поиск трех наибольших элементов")
        print("4. Суммирование элементов главной и побочной диагоналей")
        print("5. Вычисление суммы элементов с четной суммой индексов")
        print("6. Отражение элементов массива по вертикали")
        print("n. Выход")
        choice = input("Введите номер операции: ")

        if choice == "n":
            break
        if choice == "1":
            compare_array = []
            try:
                rows = int(input("Введите количество строк второго массива: "))
            except ValueError:
                rows = int(input("Некорректный ввод! Введите число: "))

            try:
                cols = int(input("Введите количество столбцов второго массива: "))
            except ValueError:
                cols = int(input("Некорректный ввод! Введите число: "))

            for i in range(rows):
                row = []
                for j in range(cols):
                    try:
                        value = int(input(f"Введите значение элемента [{i}][{j}]: "))
                    except ValueError:
                        value = int(input("Некорректный ввод! Введите число: "))
                    row.append(value)
                compare_array.append(row)
            result = compare_arrays(array, compare_array)
            print("Результат сравнения массивов:", result)

        elif choice == "2":
            try:
                element = int(input("Введите искомый элемент: "))
            except ValueError:
                element = int(input("Некорректный ввод! Введите число: "))
            row, col = find_element(array, element)
            if row == -1 and col == -1:
                print("Элемент не найден")
            else:
                print(f"Элемент найден в позиции [{row}][{col}]")

        elif choice == "3":
            largest_elements = find_largest_elements(array)
            print("Три наибольших элемента в массиве:", largest_elements)

        elif choice == "4":
            main_diagonal_sum = sum_main_diagonal(array)
            secondary_diagonal_sum = sum_secondary_diagonal(array)
            print("Сумма элементов главной диагонали:", main_diagonal_sum)
            print("Сумма элементов побочной диагонали:", secondary_diagonal_sum)

        elif choice == "5":
            even_indices_sum = sum_elements_with_even_indices_sum(array)
            print("Сумма элементов с четной суммой индексов:", even_indices_sum)

        elif choice == "6":
            reflected_array = reflect_array_vertically(array)
            print("Отраженный массив:")
            for row in reflected_array:
                print(row)
        else:
            print("Некорректный выбор операции")
