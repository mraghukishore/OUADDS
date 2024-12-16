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


    
