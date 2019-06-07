x,y=input().split()
x=int(x)
y=int(y)
for i in range(x+1,y):
    if(i%2==0):
        print(i,end=' ')
