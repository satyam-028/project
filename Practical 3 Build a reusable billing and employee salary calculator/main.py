from calculator import calculate_bill, calculate_salary


price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

bill = calculate_bill(price, quantity)

print("Total Bill:", bill)


basic_salary = float(input("\nEnter basic salary: "))
bonus = float(input("Enter bonus: "))
deduction = float(input("Enter deduction: "))

salary = calculate_salary(basic_salary, bonus, deduction)

print("Final Salary:", salary)