class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

neeraj = Employee()
neeraj.salary = 100000
neeraj.getSalary("Thanks!") # Employee.getSalary(neeraj)
neeraj.greet() # Employee.greet()
neeraj.time()

