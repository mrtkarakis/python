"""
cmp(x,y) x ve y değerlerini karşılaştırır.
x>y 1
x=y 0
x<y -1 değeri döner.
"""

a,b = (123,"abc"),(456,"def")
print(cmp(a,b))


"""
tuple(x) x listesini demete çevirir.
"""

liste1 = [1,2,3,4,5]
demet1 = tuple(liste1)
print(type(demet1))


"""
len(x) x demetinin uzunluğunu döndürür.
max(x) x demetindeki en büyük değeri döndürür.
min(x) x demetindeki en küçük değeri döndürür.
"""