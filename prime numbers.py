def prime(n):
    l=[]
    num=2
    while n>0:
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c+=1
        if c==2:
            l.append(num)
            n-=1
        num+=1
    return l
n=int(input('enter n value:'))
r=prime(n)
print('first',n,'prime numbers are ',r)