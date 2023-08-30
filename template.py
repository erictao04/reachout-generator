from utils import get_template_path


class Template:
    def __init__(self, company: str) -> None:
        self.company = company
        self.subject, self.body = self.parse()

    def parse(self):
        path = get_template_path(self.company)

        with open(path, encoding="utf8") as file:
            subject = file.readline()
            body = '<html><body>'

            file.readline()  # skip empty line

            for line in file.readlines():
                if line == "": continue

                body += f"<p>{line}</p>"

            body += "</body></html>"

        return (subject, body)

    def update(self, first_name: str) -> str:
        return self.body.replace(r"${FIRST}", first_name.capitalize())
