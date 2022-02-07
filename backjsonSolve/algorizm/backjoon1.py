# 파보나치 수열
pabocount = []
n = int(input())
pabocount.append(0)
pabocount.append(1)
if n >= 2:
    for i in range(2, n+1):
        pabo = pabocount[i-1] + pabocount[i-2]
        pabocount.append(pabo)
print(pabocount[n])
