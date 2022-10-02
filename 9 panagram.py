print("program to check wheather a string is a panagram or not")
def panagram(x):

    k="abcdefghijklmnopqrstuvwxyz "
    m=0
    for e in k:
        if e in x:
            m=m+1
        


    

    if m>=26:
        print("its a panagram")
    else:
        print("its not panagram")



    

st=input("enter the string: ")
st.lower
print(st)
panagram(st)