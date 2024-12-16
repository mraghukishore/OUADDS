#3Armstrong Number
Ctn = 'Y'
while Ctn == 'Y':
    CheckNum = int(input("Enter number to verify whether it is an armstrong number or not:"))

    order = len(str(CheckNum))
    ItrNum = CheckNum
    Sum = 0
    while ItrNum>0:
        LstDgt = ItrNum % 10
        Sum = Sum + (LstDgt ** order)
        ItrNum = ItrNum//10

    if CheckNum==Sum:
        print(CheckNum," is an armstrong number")
    else:
        print(CheckNum," is not an armstrong number")

    Ctn = input("Do you want to continue, press Y or N: ")


