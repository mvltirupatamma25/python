n=int(input('enter a number:'))
d_n=n
s=0
while(n>0):
    r=n%10
    s=s+r
    n=n//10
if d_n%s==0:
    print(d_n,"is a harshad number")
else:
    print(d_n,"is not an harshad number")
        
