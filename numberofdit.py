def Counting(Nb):
    Count = 0
    while(Nb > 0):
        Nb = Nb // 10
        Count = Count + 1
    return Count

Nb = int(input())
Count = Counting(Nb)
print("%d" %Count)
