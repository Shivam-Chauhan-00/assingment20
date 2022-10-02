print("program to access a function inside a function.")
def add(x,y):
    m=x+y
    return m


def entervalue():
    a=int(input("enter 1st value:"))
    b=int(input("enter 2nd valude:"))
    i=add(a,b)
    return i
        

n=entervalue()
print(n)