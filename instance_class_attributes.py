class Employee:
    company = "Google"
    salary = 100

neeraj = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# neeraj.salary = 300
# rajni.salary = 400
neeraj.salary = 45
print(neeraj.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 