def get_employee_path(company: str):
    return f'data\\{company}-employee.csv'


def get_template_path(company: str):
    return f'data\\{company}-template.txt'


def get_resume_name(company: str):
    return "Eric Tao Resume.pdf"


def get_resume_path(company: str):
    return 'resume\\' + get_resume_name(company)
