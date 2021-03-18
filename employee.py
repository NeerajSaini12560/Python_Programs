class Employee:
    company = "Google"
    salary = 100

neeraj = Employee()
rajni = Employee()
neeraj.salary = 300
rajni.salary = 400

print(neeraj.company)
print(rajni.company)
Employee.company = "YouTube"
print(neeraj.company)
print(rajni.company)
print(neeraj.salary)
print(rajni.salary)