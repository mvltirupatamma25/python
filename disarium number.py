n=int(input("enter a number: "))
s=0
i=len(str(n))
t=n
while(n>0):
    r=n%10
    s=s+r**i
    n=n//10
    i=i-1
if(s==t):
    print("the number is an disarium number")
else:
    print("the number is not an disarium number")
    

