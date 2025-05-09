    # while 8 /////////////////////




a=int(input())
k=0
n=1
while n<=a:
    r=0
    i=n
    while i>0:
        r=r*10+i%10
        i//=10
    if n==r :
        k+=1
    n+=1
print(k)

   