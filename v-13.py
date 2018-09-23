#3-the reverse of the number
print("the reverse of the number")
N=int(input("NUMBER="))
rev=0
while N>0:
    re=N%10
    rev=rev*10+re
    N=N//10
print(rev)
