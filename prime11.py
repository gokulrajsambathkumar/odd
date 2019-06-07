i= int(input())
for p in range(2,i):
	if i % p == 0:
		print("no")
		break
else:
	print("yes")
