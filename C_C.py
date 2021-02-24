class Employee:
    no_of_leavs = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} salary is {self.salary} and role is{self.role}"

davide = Employee("davide",400,"Instructor")

print(davide.salary)



