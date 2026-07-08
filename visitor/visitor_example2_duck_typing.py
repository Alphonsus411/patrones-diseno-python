

class Computer:
    def accept(self, visitor):
        visitor.visit_computer(self)

class Phone:
    def accept(self, visitor):
        visitor.visit_phone(self)

class TV:
    def accept(self, visitor):
        visitor.visit_tv(self)


class RepairService:
    def visit_tv(self, tv):
        print("Repairing a TV.")

    def visit_phone(self, phone):
        print("Repairing a Phone.")

    def visit_computer(self, computer):
        print("Repairing a Computer.")


tv = TV()
phone = Phone()
computer = Computer()
repair_service = RepairService()

tv.accept(repair_service)
phone.accept(repair_service)
computer.accept(repair_service)