    # for 9 /////////////////////




a=int(input())
b=int(input())
k=0
if a<b:
    for i in range(a,b+1):
        k+=i
    print(k)
elif a>b:
    for i in range(b,a+1):
        k+=i
    print(k)


   