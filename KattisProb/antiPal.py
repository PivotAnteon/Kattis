import re

text = input()
text = re.sub('[\W_]+','', text).lower()

def checkPalindrome(text):
    ##reverse the string
    reverseText = text[::-1]
    ##check if the entire string is palindrome
    if text == reverseText:
        return True
    
    for i in range(len(text)-1 ):
        check = text[i] + text[i+1]
        for j in range(len(reverseText)-1):
            reverseCheck = reverseText[j] + reverseText[j+1]
            if check == reverseCheck:
                return True
    return False

if checkPalindrome(text):
    print("Palindrome")
else:
    print("Anti-palindrome")





    



