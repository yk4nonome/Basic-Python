a,b,c==input().split()
a=int(a)
b=int(b)
c=int(c)
if a>=b>=c:
 print(c,b,a)
elif a>=c>=b:
    print(b,c,a)
elif b>=a>=c:
        print(c,a,b) 
elif b>=c>=a:
      print(a,c,b)
elif c>=b>=a:
    print(a,b,c)
else:
 print(b,a,c)
