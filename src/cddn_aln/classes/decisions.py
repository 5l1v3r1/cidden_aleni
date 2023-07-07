class Decision:
    def __init__(self, decision_number, application_date, decision_date):
        self.decision_number = decision_number
        self.application_date = application_date
        self.decision_date = decision_date

    def get_decision_number(self):
        return self.decision_number

    def get_application_date(self):
        return self.application_date

    def get_decision_date(self):
        return self.decision_date

    # Other methods and attributes...


class CourtPanel:
    def __init__(self, president):
        self.president = president
        self.members = []

    def get_president(self):
        return self.president

    def get_members(self):
        return self.members

    def get_total_judges(self):
        return len(self.members) + 1

    # Other methods and attributes...


class ConstitutionalCase:
    def __init__(self, case_number, issue_date):
        self.case_number = case_number
        self.related_decisions = []
        self.issue_date = issue_date

    def get_case_number(self):
        return self.case_number

    def get_related_decisions(self):
        return self.related_decisions

    def get_issue_date(self):
        return self.issue_date

    # Other methods and attributes...
