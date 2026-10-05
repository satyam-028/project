print("       Students informations       ")

def student_information():
    info = []

    while True:
        # print("Enter the Student name : ")
        # print("Enter the Student school name : ")
        # print("Enter the Student subject name : ")
        # print("Enter the Student marks : ")
        choice = input("""Enter a number
           1. Name
           2. School Name 
           3. Subject Name
           4. Student Marks
          (press q for quit) : """)

        # choice = input("choice a option : ")
        
        if choice == "q":
            print("Final result show ")
            return info

        elif choice == "1":
            name = (input("Enter a Name : "))
            info.append(name)
            
        elif choice == "2":
            school = (input("Enter a School Name : "))
            info.append(school)
            
        elif choice == "3":
            subject = (input("Enter a Subject Name : "))
            info.append(subject)
            
    
        elif choice == "4":
            marks = (float(input("Enter a Marks : ")))
            info.append(marks)
            
        else:
            print("Enter a valid number")

var = student_information()
print(var)