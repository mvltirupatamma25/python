for i in range(1900,2101):
    if((i%400==0 or i%4==0) and i%100!=0):
        print(i)
