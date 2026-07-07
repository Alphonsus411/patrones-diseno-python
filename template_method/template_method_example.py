from abc import ABC, abstractmethod


class HiringProcess(ABC):
    def hire_candidate(self):
        self.receive_cv()
        self.conduct_interview()
        self.conduct_skill_test()
        self.issue_offer()

    @abstractmethod
    def receive_cv(self):
        pass

    @abstractmethod
    def conduct_interview(self):
        pass

    def conduct_skill_test(self):
        pass

    @abstractmethod
    def issue_offer(self):
        pass


class Bank(HiringProcess):
    def receive_cv(self):
        print("Receiving CV for Bank.")

    def conduct_interview(self):
        print("Conducting interview about banking knowledge.")

    def issue_offer(self):
        print("Issuing job offer.")


class SoftwareCompany(HiringProcess):
    def receive_cv(self):
        print("Receiving CV for Software Company.")

    def conduct_interview(self):
        print("Conducting technical interview.")

    def conduct_skill_test(self):
        print("Conducting coding test.")

    def issue_offer(self):
        print("Issuing job offer.")


software_company = SoftwareCompany()
software_company.hire_candidate()

bank = Bank()
bank.hire_candidate()





