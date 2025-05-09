    # while 9 /////////////////////




a=int(input())
b=int(input())
s=0
if a<b:
     i=a
     while i<=b:
          s+=i
          i+=1
     print(s,end=' ')
elif a>b:
     i=b
     while i<=a:
          s+=i
          i+=1
     print(s,end=' ')   


   