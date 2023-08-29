import csv

from collections import namedtuple
from email_builder import EmailBuilder
from template import Template
from utils import get_employee_path
from draft import Draft


class Company:
    def __init__(self, company: str, email_builder: EmailBuilder) -> None:
        self.company = company.lower()
        self.email_builder = email_builder
        self.template = Template(self.company)
        self.employees = self.read_names()
        self.draft = Draft(self.company)

    def read_names(self):
        Employee = namedtuple('Employee', ('first_name', 'last_name'))

        employee_path = get_employee_path(self.company)
        employees = []

        with open(employee_path) as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                first_name, last_name = [name.lower() for name in row]
                employees.append(Employee(first_name, last_name))

        return employees

    def create_drafts(self):
        for first_name, last_name in self.employees:
            email = self.email_builder.build_email(first_name, last_name)
            subject = self.template.subject
            body = self.template.update(first_name)

            self.draft.create_draft(email, subject, body)
