from collections import namedtuple
import csv

from utils import get_employee_path


Name = namedtuple('Name', ('first_name', 'last_name'))


class Employees:
    def __init__(self, company) -> None:
        self.company = company
        self.names = self.get_names()

    def get_names(self):
        employee_path = get_employee_path(self.company)
        names = []

        with open(employee_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=" ")

            for row in csv_reader:
                if row[-1] == "":
                    row = row[:-1]  # strip trailing space

                first_name, last_name = [name.lower() for name in row]
                names.append(Name(first_name, last_name))

        return names
