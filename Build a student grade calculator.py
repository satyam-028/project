import statistics

def student_grade():
    var = float(input("Enter a Python number : "))
    var1 = float(input("Enter a Java number : "))
    var2 = float(input("Enter a C++ number : "))
    var3 = float(input("Enter a Rust number : "))

    na = [var, var1, var2, var3]
    n = statistics.mean(na)
     
    if n >= 90:
        print("The student Grade is A ")
    elif n >= 80:
        print("The student Grade is B ")
    elif n >= 70:
        print("The student Grade is C ")
    elif n >= 50:
        print("The student Grade is D ")
    else:
        print("Fail")
        

num = student_grade()