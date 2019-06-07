n,x,y=input().split()
n=int(n)
x=int(x)
y=int(y)
sum=0
for i in range(n):
    sum=sum+x
    x=x+y
print(sum)
