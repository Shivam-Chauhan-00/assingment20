print("program to check given number is prime or not by the function")
def check(s):
    for i in range(2,s):

        if s%i==0:
                return False
        
    return True





n=int(input("enter the number :"))
print(check(n))