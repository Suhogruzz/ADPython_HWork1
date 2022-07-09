import application.salary as salary
import application.db.people as people
import datetime


def main():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Время подсчета заработной платы: {date}')
    pass


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    main()
