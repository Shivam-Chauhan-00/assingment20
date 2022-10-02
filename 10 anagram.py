print("program to check whether a string is anagram or not")
def anagram(a,b):
    print(a,b)
    j=list(a)
    k=list(b)

    
    if sorted(j)==sorted(k):
        print("its a anagram")
    else:
        print("its not a anagram")

x="shivam"
print("try to enter the anagram of...: ",x)
y=input("enter the string: ")
anagram(x,y)