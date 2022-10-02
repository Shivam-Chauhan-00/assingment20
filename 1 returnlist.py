print("program to craete a function that takes a list and returns a new list with original list unique elemnts")
def  uniquelist(x):
    l3=[]
    for e in x:
        if e>0:
            l3.append(e)
    return l3



l1=[-1,-2,-13,6,7,2,7,3,-10]
l2=uniquelist(l1)
print(l2)