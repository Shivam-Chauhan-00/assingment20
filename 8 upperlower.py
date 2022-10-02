print("program to calculate the number of upper case letters and lower case letters.")

def casechecker(x):
    

    c=0
    d=0
    for e in x:
        if ord(e) in range(65,91,1):
            c=c+1
        if ord(e) in range(97,123,1):
            d=d+1
    
    print("the lower case in",d)
    print("the upper case is",c)
        


st=input("enter a string: ")
casechecker(st)
