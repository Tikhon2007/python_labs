"""
Программа lab5
Пример по теме линейные алгоритмы
Вычисление выражений
Программист: Галкин Т.С., гр. Ш31
Проверил: Дмитреева П.А.
Дата написания: 29.01.2023
Переменные:
    ---
"""
print('1 - cos (0) \n2 - cos (Pi/6) ')
print('3 - cos (Pi/4) \n4 - cos (Pi/3) ')
print('3 - cos (Pi/2)')
match input('code: '):
    case '1':
        print('1')
    case '2':
        print('SQRT(3)/2')
    case '3':
        print('SQRT(2)/2')
    case '4':
        print('1/2')
    case _:
        print('ERROR')