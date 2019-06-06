ak1=input()
ak1=ak1.split()
bk1=int(ak1[1])
ck1=input()
ck1=ck1.split()
dk1=0
ck1=list(map(int,ck1))
for i in range(0,bk1):
    dk1=dk1+ck1[i]
print(dk1)
