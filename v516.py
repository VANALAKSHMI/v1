#co-prime
n=int(input())
m=int(input())
c=0
d=0
for x in range(1,n+1):
    s=n%x
    if(s==0):
        c=c+1
for x in range(1,m+1):
    s=m%x
    if(s==0):
        d=d+1
if(c==2)&(d==2):
    print("1")
else:
    print("0")
 
