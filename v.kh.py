    # while 7 /////////////////////




a=int(input())
b=int(input())
s=0
if a<b:
     i=a
     while i<=b:
          s+=1
          i+=1
     print(s,end=' ')
elif a>b:
     i=b
     while i<=a:
          s+=1
          i+=1
     print(s,end=' ')


   