#2Calculator
while True:
    print("Enter '+' for addition")
    print("Enter '-' for substraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for dicision")
    print("Enter 'quit' to close ")

    user_input = input(":")

    if  user_input == "quit":
        break
    elif user_input in ["+","-","*","/"]:
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter first number"))
    
        if user_input =="+":
            print(num1,"+",num2,"=",num1+num2)
        elif user_input =="/":
            print(num1,"/",num2,"=",num1/num2)
        elif user_input =="*":
            print(num1,"*",num2,"=",num1*num2)
        elif user_input =="-":
            print(num1,"-",num2,"=",num1-num2)
        else:
            print("Invalid  Input")