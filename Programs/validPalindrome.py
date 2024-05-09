def validPalindrome(text):
    toCheck = ""
    for i in text:
        if i.isalnum():
            toCheck+=i.lower()
    return (toCheck == toCheck[::-1])

def isalphaNum(s):
    return (ord('A') <= ord(s) <= ord('Z') and ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) and ord('9'))

def validPalindromeTwoPointer(s):
    l,r = 0, len(s) -1 

    while l < r:
        while l < r and not isalphaNum(s[l]):
            l+=1 
        while r>l and not isalphaNum(s[r]):
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l+1, r-1
    return True





print(validPalindrome(input())) 



