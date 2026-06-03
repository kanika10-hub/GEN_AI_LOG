class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Manager:

    def __init__(self, name):
        self.name = name
        self.team = []

    def add(self, employee):
        self.team.append(employee)

    def show(self):

        print(self.name)

        for emp in self.team:
            emp.show()


manager = Manager("Team Lead")

manager.add(Employee("Alice"))
manager.add(Employee("Bob"))

manager.show()
