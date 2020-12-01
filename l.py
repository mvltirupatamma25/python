num=int(input("enter a number"))
d=num
s=0
while num>0:
    r=num%10
    s=s+r^3
    num=num//10
if s==d:
    print("the number is amstrong")
else:
    print("the number is not an amstrong number")
