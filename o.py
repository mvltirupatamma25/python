n=int(input("enter a number: "))
s=0
i=len(str(n))
while(n>0):
    r=n%10
    s=s+r*10**(i-1)
    n=n//10
    i=i-1
print(s)
