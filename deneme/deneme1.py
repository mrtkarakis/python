import time
from itertools import permutations
st =time.time()
def isPrime(sayi):
    if sayi == 0:
        return False
    elif sayi == 1:
        return False
    elif sayi == 2 :
        return True
    else:
        if sayi %2==0:
            return False
        else:
            for i in range(3,int((sayi**0.5)+1),2):
                if sayi%i==0:
                    return False
            return True

ans = [1,2,2]

for i in range(1000000,10000000):
    if isPrime(i):
        for t in list(permutations(str(i))):
            if int(str(i)[0]) == int(t[0]) and int(str(i)[1]) == int(t[1]) and int(str(i)[2]) == int(t[2]) and int(str(i)[3]) == int(t[3]) and int(str(i)[4]) == int(t[4]) and i % int(t[0] + t[1] + t[2] + t[3] + t[4]) !=0 and int(t[0] + t[1] + t[2] + t[3] + t[4]+t[5]+t[6]) < i and (int(t[0] + t[1] + t[2] + t[3] + t[4]+ t[5] + t[6]))/(i-1) < ans[2] :
                ans[0] = i
                ans[1] = int(t[0] + t[1] + t[2] + t[3] + t[4]+t[5]+t[6])
                ans[2] = int(t[0] + t[1] + t[2] + t[3] + t[4]+t[5]+t[6])/(i-1)
print(ans)
print(time.time()-st)