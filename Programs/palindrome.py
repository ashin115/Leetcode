def isPalindrome(num):
    if num == int(str(num)[::-1]):
        print(True)
    else:
        print(False)

num = int(input())
isPalindrome(num)