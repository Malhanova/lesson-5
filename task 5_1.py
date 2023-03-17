"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
"""

report = []
sum_salaries = 0
with open('task5_3.txt.', 'r', encoding='UTF-8') as file:
    rows = file.readlines()
    print("Оклады сотрудников")
    for row in rows:
        row_items = row.split(' ')
        report.append([row_items[0], int(row_items[1])])
        print(f"{row_items[0]}: {int(row_items[1])} руб.")
        sum_salaries += int(row_items[1])

print("\nСотрудники с окладом менее 20000 руб.")
[print(worker[0]) for worker in report if worker[1] < 20000]

print(f"\nСредний оклад сотрудников {sum_salaries / len(report)} руб.")