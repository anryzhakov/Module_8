# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Try и Except"

import random


def add_everything_up(a, b):
    try:
        s = a + b
        return s
    except TypeError:
        print('Переменные разных типов функция сложения не поддерживает')
        print('Программа вынуждена привести переменные к типу string')
        a1 = str(a)
        b1 = str(b)
        s = a1 + b1
        return s
    else:
        print('Тип, используемых переменных позволяет провести сложение без ошибки')
    finally:
        pass


items = [1, 7, 22, 3.95, 7.87, 4.03, 'apple', 'string', 'float', 'grep']
a = random.choice(items)
b = random.choice(items)
print('Тип переменной а:', type(a), 'Тип переменной b:', type(b))
result = add_everything_up(a, b)
print('Ответ:', result)
