class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

neeraj = Employee()
neeraj.salary = 100000
neeraj.getSalary() # Employee.getSalary(neeraj)