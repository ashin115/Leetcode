def isPalindrome(num):
    if str(num)[::-1] == str(num):
        return True
    else:
        return False


num = int(input())
print(isPalindrome(num))
