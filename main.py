from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import cowsay

if __name__ == "__main__":
    print(calculate_salary())
    print(get_employees(), date.today())
