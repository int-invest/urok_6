class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker = Position('Mark', 'Kraken', 'Manager', 50000, 10000)
print(worker.get_full_name())
print(worker.position)
print(worker.get_full_income())


