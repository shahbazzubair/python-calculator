print("Welcome to my Calculator!")
print("Our Calculator allows following operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:

 choice= int(input("Select your desired option:"))
 print("You selcted option", choice ,". Now enter values.")
 first_number= float(input("Enter the first value:"))
 second_number= float(input("Enter the second value:"))

 if choice==1:
    print("Result:", round(first_number + second_number, 3))
 elif choice==2:
    print("Result:" ,round(first_number - second_number, 3))
 elif choice==3:
    print("Result:" ,round(first_number * second_number, 3))
 elif choice==4:
    if second_number== 0:
        print("Dividing by 0 is not possible.Error!")
    else :
        print("Result:" ,round(first_number / second_number, 3))
 else :
    print("You selected invalid option.")

 cont= input("Do you wish you want to continue?(y/n)").lower()
 if cont!= "y":
    break
 else:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")