#All OU AD DS Programs

#2 Calculator 
while True:
    inp = input("Enter operation do you want to perform \n + for addition, - for substraction, * for multiplicationl, / for division \n :")
    if inp in ["+","-","*","/"]:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        if inp == "+":
            print(num1,inp,num2,"=",num1+num2)
        elif inp == "*":
            print(num1,inp,num2,"=",num1*num2)
        elif inp == "/":
            print(num1,inp,num2,"=",num1/num2)
        elif inp == "-":
            print(num1,inp,num2,"=",num1-num2)
    else:
        print("invalid input")
    cnt = input("Do you want to continue Y or N \n :")
    if cnt not in ['Y','y']:
        break

#3Armstrong number
while True:
    nbr = int(input("enter a number to validate whether it is an armstrong number or not \n:"))
    order =len(str(nbr))
    sum = 0
    itrnbr = nbr
    while itrnbr>0:
        muldgt = itrnbr%10
        sum += muldgt**order
        itrnbr//=10
    if(sum==nbr):
        print(nbr," is an armstring number")
    else:
        print(nbr," is NOT an armstring number")
    if(input("Enter Y if you want to continue, otherwise enter N \n :") not in ['Y','y']):
        break


#4Primenumbers between 2 numbebrs
while True:
    lowlmt=int(input("Enter lower limit to search Prime numbers\n :"))
    uprlmt=int(input("Enter upper limit to search Prime numbers\n :"))
    for i in range(lowlmt,uprlmt):
        p=0
        for j in range(2,i):
            if(i%j==0):
                p=1
                break
        if(p==0):
            print(i)
    cnt=input("Press Y to continue, otherise press n\n :")
    if(cnt not in ["Y","y"]):
        break
        
        
#5Factorial
def recur(n):
    if n==1:
        return n
    else:
        return n*recur(n-1)
while True:
    nbr = int(input("Enter a numer to find factorial \n :"))
    if nbr<0:
        print("factorial is for positive numbers only")
    elif nbr==0:
        print("factorial of 0 is 1")
    else:
        print(recur(nbr))
    cnt=input("Press Y to continue, otherise press n\n :")
    if(cnt not in ["Y","y"]):
        break

#6Palindrome
def palindrome(s):
    return s == s[::-1]
while True:
    wr = input("Enter word to verify palindrome \n :")
    if palindrome((wr.upper())):
        print(wr," is palindrome")
    else:
        print(wr," is not a palindrome")
    if(input("Press Y to continue, otherise press n\n :") not in ["Y","y"]):
        break
        
#7Wordcount
while True:
    str = input("Enter input string \n : ")
    char =0
    word =1
    for i in str:
        char +=1
        if i==' ':
            word+=1
    print("number of chars are ",char," number of words are",word)
    if(input("Press Y to continue, otherise press N\n :") not in ["Y","y"]):
        break

