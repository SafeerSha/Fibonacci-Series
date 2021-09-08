n=int(input('Enter The Limit :'))
if n<=0:
    print('Enter Any positive Number\n')
else:
    k=0
    t1,t2=k-1,1
    for i in range(0,n):
        t=t1+t2
        print(t,)
        t1=t2
        t2=t
    
