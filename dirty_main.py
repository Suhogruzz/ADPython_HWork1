from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def main():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Время подсчета заработной платы: {date}')
    pass


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    main()
