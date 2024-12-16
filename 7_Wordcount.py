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
