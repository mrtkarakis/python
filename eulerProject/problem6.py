import time
st = time.time()
kareleri = 0
toplamlar─▒ =0
for i in range(1,101):
    kareleri = kareleri + (i**2)
for i in range(1,101):
    toplamlar─▒+=i
sonuc = (toplamlar─▒**2)-kareleri
print(sonuc)
print(time.time()-st)


# 25164150  0.0