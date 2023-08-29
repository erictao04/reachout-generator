import csv

from collections import namedtuple
from email_builder import EmailBuilder
from employee import Employees
from template import Template
from utils import get_employee_path
from draft import Draft


class Company:
    def __init__(self, company: str, email_builder: EmailBuilder) -> None:
        self.company = company.lower()
        self.email_builder = email_builder
        self.template = Template(self.company)
        self.employees = Employees(self.company)
        self.draft = Draft(self.company)

    def create_drafts(self):
        for first_name, last_name in self.employees.names:
            email = self.email_builder.build_email(first_name, last_name)
            subject = self.template.subject
            body = self.template.update(first_name)

            self.draft.create_draft(email, subject, body)
