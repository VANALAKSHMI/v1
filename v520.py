#palindrome-count
x=int(input())
c=0
for n in range(1,x+1):
    t=n
    re=0
    while(n>0):
        r=n%10
        re=re*10+r
        n=n//10
    if(re==t):
        c=c+1
print(c)
