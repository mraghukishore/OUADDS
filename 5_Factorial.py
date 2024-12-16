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

