"""
Задание 5 .  Создать (программно) текстовый файл,
записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.}
"""

import random

with open('task5_5_rus.txt', 'w', encoding='UTF-8') as file:
    glue = ''
    for _ in range(5):
        file.write(glue + str(random.randint(0, 10)))
        glue = ' '

with open('task5_5_rus.txt', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")

