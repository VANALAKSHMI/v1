#5
n=(input("N="))
if(len(n)<=20):
    i=len(n)-1
    rev=""
    a=0
    while(i>=0):
        rev=n[i]
        l={"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10}
        a=a+l[rev]
        i=i-1
    print(a)
   
