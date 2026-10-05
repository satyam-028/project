def number():

        num1 = float(input("Enter a number for find the largest number : "))
        num2 = float(input("Enter a number for find the largest number : "))
        num3 = float(input("Enter a number for find the largest number : "))
        if num1>num2 and num1>num3:
            print(f"This number largest number : {num1}")
        elif num2>num1 and num2>num3:
            print(f"This number largest number : {num2}")
        else:
            print(f"This number largest number : {num3}")

numbers = number()