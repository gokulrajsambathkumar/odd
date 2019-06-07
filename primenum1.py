x,y=input().split()
c=int(x)
d=int(y)
for i in range(c+1,d): 
  s=0
  for j in range(1,d):
    if(i%j==0):
      s=s+1
  if(s==2):
    print(i,end=" ")
