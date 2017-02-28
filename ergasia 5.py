a=[1,2,3,4,5,6,7,8,9]
for i in range (10,1000):
    sum=0
    if(i<=100):
        sum=(i/10)+(i%10)
        if(i%sum==0):
            a.append(i)
    else:
        sum=(i/100)+((i/10)%10)+(i%10)
        if(i%sum==0):
            a.append(i)
a.append(1000)
print a
for i in range (1,1000):
    mult=0
    if(a.count(i)!=0):
        if(i<=10):
            print i
        if(i<=100):
            mult=(i/10)*(i%10)
            if(mult!=0):
                if(i%mult==0):
                    print i
        else:
            sum=(i/100)*((i/10)%10)*(i%10)
            if(mult!=0):
                if(i%mult==0):
                    print i
