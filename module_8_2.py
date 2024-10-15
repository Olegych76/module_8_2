def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы: {type(number)} - {number}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        return personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
    except TypeError:
        print(f"{numbers} - некорректный тип данных")
        return None
    except ZeroDivisionError:
        print("В списке нет элементов")
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
