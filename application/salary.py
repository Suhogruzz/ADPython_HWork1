def calculate_salary():
    salary = int(input('Введите количество отработанных дней: ')) * int(input('Введите размер оклада: '))
    salary = int(input('Введите размер премии в процентах: ')) / 100 * salary + salary
    return print(f'Выплатить зарплату: {salary}')
