class Applicant:
    def __init__(self, name, application_date, application_type):
        self.name = name
        self.application_date = application_date
        self.application_type = application_type

    def get_name(self):
        return self.name

    def get_application_date(self):
        return self.application_date

    def get_application_type(self):
        return self.application_type

    # Other methods and attributes...


class Lawyer:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.cases_count = 0

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_cases_count(self):
        return self.cases_count

    # Other methods and attributes...
