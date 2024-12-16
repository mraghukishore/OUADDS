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