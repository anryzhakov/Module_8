# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"


def personal_sum(numbers):
    res = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            res = res + numbers[i]
        except TypeError:
            incorrect_data += 1
            print('Некорректный тип данных для подсчёта суммы -', numbers[i])
    return res, incorrect_data


def calculate_average(numbers):
    try:
        _sum = personal_sum(numbers)
        res_aver = _sum[0] / (len(numbers) - _sum[1])
        return res_aver
    except ZeroDivisionError:
        res_aver = 0
        print(f'Допущено деление на ноль.')
        return res_aver
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')