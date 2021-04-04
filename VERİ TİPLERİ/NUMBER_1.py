"""
abs(x) x değerinin mutlak değerini döndürür
"""
a = -7
print(abs(a))

"""
math.fabs(x) abs(x) metodundan tek farkı sonuç herzaman float şeklinde döner
"""
import math
a = -5
b = -12.5
print(math.fabs(a))
print(math.fabs(b))

"""
math.ceil(x) x değer tam sayı ise kendisini float bir değer ise (14.5,85.005) tam sayı kısmının bir fazlasını döndürür.
"""

import math
b = 5
c = 12.75
d = 15.00005
print(math.ceil(b))
print(math.ceil(c))
print(math.ceil(d))

"""
math.floor(x) x değer tam sayı ise kendisini float bir değer ise (14.5,85.005) tam sayı kısmının bir azına döndürür.
"""

import math
a = -16.57
b = 5
c = 12.75
d = 15.00005
print(math.floor(a))
print(math.floor(b))
print(math.floor(c))
print(math.floor(d))

"""
e sayıyı ==> -e sayısı veya Euler sayısı, matematik, doğal bilimler ve mühendislikte önemli yeri olan sabit bir reel sayı, doğal logaritmanın tabanı.-
e saysının değeri ==> 2.718281828459045
math.exp(x) e üzeri x 
"""

import math
print(math.exp(3)) # 2.718281828459045*2.718281828459045*2.718281828459045 ifadesini kısa gösterilmiş halidir.

"""
math.log(x) x sayısının logaritma e tabınındaki değerini döndürür.
"""

import math
print(math.log(math.e**2))
print(math.log(4))

"""
math.log10(x) x sayısının logaritma 10 tabınındaki değerini döndürür.
"""

import math
print(math.log10(456))
print(math.log10(100))

"""
max(x,y,z) değerleri arasındaki en büyük sayıyı döndürür.
min(x,y,z) değerleri arasındaki en küçük sayıyı döndürür.
"""

"""
math.modf(x) x sayısının virgülden önce ve sonraki kısmını ayırarak döndürür.
"""

import math
a = 12.5
b = 135.4658
c = 19
print(math.modf(a))
print(math.modf(b))
print(math.modf(c))

"""
math.pow(x,y) x üzeri y için kullanılır.
"""
import math
print(math.pow(5,2))
print(math.pow(100,0.5))
print(math.pow(3,3))

"""
round(x,y) x sayısını yuvarlar, y fonksiyonuyla birlikte virgülden sonraki kaç basamağın alınacağı ifade edilir.
"""

print(round(100.64469))
print(round(100.64469,3))
print(round(100.64469,2))

"""
math.sqrt(x) x değerinin karekökünü döndürür.
"""
import math
print(math.sqrt(9))
print(math.sqrt(123))
print(math.sqrt(10.5))

"""
random.choice(x) x elemanlarından rastgele birini döndürür.
"""

import random
print(random.choice(range(100)))
print(random.choice([1,2,3,5,4,6]))
print(random.choice("hello"))

"""
random.randrange(x,y,z) sadece x değeri girersek 0 ile x arası bir sayı döndürür.
x ve y başlangıç ve bitiş sayılarıdır, z ise kaç sayı atlamasını istediğimiz değeri belirtir.
"""
import random
print(random.randrange(500))
print(random.randrange(0,500, 3))

"""
random.random() 0 ile 1 arası bir değer üretir.
"""

import random
print(random.random())


"""
random.shuffle(x) x listesi içindeki elemanları rastgele karıştırır.
"""

import random
liste1=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(liste1)
print(liste1)
random.shuffle(liste1)
print(liste1)
random.shuffle(liste1)
print(liste1)

"""
random.uniform(x,y) x ve y arasında float bir değer üretir.
"""

import random
print(random.uniform(5,6))
print(random.uniform(7,9))