#9-FIND NUMBER OF PRIME NUMBERS BETWEEN 2 INTERVALS
print("FIND NUMBER OF PRIME NUMBERS BETWEEN 2 INTERVALS")
s=int(input("i="))
e=int(input("r="))
if(s,e<=100000):
    flag=0
    c=0
    for x in range(s,e+1):
        flag=0
        for y in range(1,x+1):
            if(x%y==0):
                flag=flag+1
        if(flag==2):
             c=c+1
    print(c)
else:
    print("invalid")
