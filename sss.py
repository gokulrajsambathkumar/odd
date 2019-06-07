x,b=input("").split()
x=int(x)
b=int(b)
for i in range(x,b):
     c=0
     d=i
     while(i!=0):
          r=i%10
          c=c+r*r*r
          i//=10
     if(d==c):
        print(d,end=" ")
