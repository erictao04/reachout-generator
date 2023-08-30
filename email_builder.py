from abc import abstractmethod


class EmailBuilder:
    @abstractmethod
    def build_email(self, first_name: str, last_name: str) -> str:
        pass


class FirstLastEmailBuilder(EmailBuilder):
    '''
    Eric Tao, @splunk.com --> eric.tao@splunk.com
    '''

    def __init__(self, domain: str) -> None:
        self.domain = domain

    def build_email(self, first_name: str, last_name: str) -> str:
        return f'{first_name}.{last_name}{self.domain}'


class FirstEmailBuilder(EmailBuilder):
    '''
    Eric Tao, @splunk.com --> eric@splunk.com
    '''

    def __init__(self, domain) -> None:
        self.domain = domain

    def build_email(self, first_name: str, last_name: str) -> str:
        return f'{first_name}{self.domain}'


class FirstInitialLastEmailBuilder(EmailBuilder):
    '''
    Eric Tao, @splunk.com --> etao@splunk.com
    '''

    def __init__(self, domain) -> None:
        self.domain = domain

    def build_email(self, first_name: str, last_name: str) -> str:
        return f'{first_name[0]}{last_name}{self.domain}'
