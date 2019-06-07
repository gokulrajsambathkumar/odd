num,x,y=input().split()
num=int(num)
x=int(x)
y=int(y)
sum=0
for i in range(num):
    sum=sum+x
    x=x+y
print(sum)
