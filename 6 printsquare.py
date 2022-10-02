from tkinter import S


print("program to print square of 1 to 30 by function")
def square():
    n=30
    s=1
    sq=0
    while s<=n:
        sq=s*s
        print(sq,end=" ")
        s+=1




square()