#10
s1=input("string1:")
s2=input("string2:")
i=0
c=0
if(len(s1),len(s2)<=100000):
   for i in range(len(s1)):
            if(s1[i]!=s2[i]):
                c=c+1
   if(c==1):
        print("yes")
   else:
        print("no")
else:
    print("invalid")
