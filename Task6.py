# Task 6 — Employee Payslip
Employee_name=input("Employee name:")
Basic_salary=float(input("Basic salary:"))
Transport_allowance=float(input("Transport allowance:"))
Food_allowance=float(input("Food allowance:"))
Gross_Salary =Basic_salary + Transport_allowance + Food_allowance
print("\n========================================")
print("          EMPLOYEE PAYSLIP")
print("========================================")

print("Employee:", Employee_name)
print()
print("Basic Salary:",Basic_salary ,"ETB")
print("Transport Allowance:",  Transport_allowance ,"ETB")
print("Food Allowance:", Food_allowance ,"ETB")
print("----------------------------------------")
print("Gross Salary: ",Gross_Salary ,"ETB")

print("========================================")
