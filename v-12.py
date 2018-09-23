#2-FIND FACTORIAL OF A NUMBER
print("FIND FACTORIAL OF A NUMBER")
n=int(input("N="))
if(n<=20):
        m=1
        for x in range(n,0,-1):
         m=m*x
        print(m)
else:
 print("invalid input")
