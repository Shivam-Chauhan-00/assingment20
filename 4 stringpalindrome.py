import abc


print("program to check given string is palindrome or not")
def palindrome(s):
    n=s[::-1]

    if(n!=s):
        return "str is not palindrome"
    else:
        return "str is palindrome"


        




st=input("enter a string: ")
print(palindrome(st))
