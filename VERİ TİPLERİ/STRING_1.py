"""
.capitalize() sadece ilk harfi büyük yapar. Diğer harfleri küçük yapar.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.capitalize())

""" 
.center(x,"y") stringin uzunluğunu x kadar yapar ve yazıyı ortalar, y yerine bir değer vermezsek boşlukla doldurur.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.center(90,"-"))

"""
.count("x",y,z) stringde kaç adet "x" değeri olduğunu döndürür. 
y ve z fonkisyonularını eklersek y indexinden başlar z indexine kadar kısımı arara
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.count("e",2,21))

"""
.endswith("x",y,z) stringin sonunda "x" değeri olup olmadığına bakar "x" değeri ile bitiyorsa True değerini döner.
y ve z fonksiyonlarını kullanırsak y indexinden başlar ve z-1 indexinde "x" değeri olup olmadığını döndürür.
.startswith("x",y,z) stringin "x" değeri başlamasına göre True değeri döner.

"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.endswith("."))
print(string.endswith("m",0,4))
print(string.startswith("n"))

"""
.expandtabs(x) \t ile belirtilen yere eğer x<=8 ise 1 boşluk bırakır.
x'in 8'den büyük olduğu her bir değer için 1 tane boşluk bırakır
"""
str1 ="tab bos\tlugu bırakır"
print(str1.expandtabs(4))
print(str1.expandtabs(8))
print(str1.expandtabs(9))

"""
.find(x,y) stringde "x" elemanının hangi indexte olduğunu söyler, "x" elemanı indexte yoksa HATA verir.
y fonksiyonunu kullanırsak y indexinden itibaren "x" elemanını arar.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.index("T"))
print(string.index("T",10))
print(string.index("o"))

"""
.index(x,y) stringde "x" elemanının hangi indexte olduğunu söyler, "x" elemanı indexte yoksa HATA verir.
y fonksiyonunu kullanırsak y indexinden itibaren "x" elemanını arar.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.index("T"))
print(string.index("T",10))
print(string.index("o"))

"""
.isalnum() string boşluk bırakılmadan birleşik bir şekilde yazıldıysa True değerini döner.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.isalnum())
str2 = "12meko35"
print(str2.isalnum())

"""
.isalpha() string boşluk bırakılmadan ve sayısal bir değer içermeden yazıldıysa True değerini döner.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.isalpha())
str2 = "12meko35"
print(str2.isalpha())
str3 = "meko"
print(str3.isalpha())

"""
.isdigit() stringte sadece sayısal değer varsa True değerini döner.
.isnumeric() ile farkı ise, .isnumeric() çince sayısal değerler girildiğindede True değeri döner fakat .isdigit() sadece digital sayısal değerlerde True değerini döndürür.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.isdigit())
str2 = "12meko35 "
print(str2.isdigit())
str4 = "1912"
print(str4.isdigit())

"""
.islower() stringte sadece küçük harfler kullanılmışsa True değerini döner.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.islower())
str2 = "12meko35"
print(str2.islower())

"""
.isspace() string sadece boşluktan oluştuysa True değerini döner.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.isspace())
str5 = "    "
print(str5.isspace())

"""
.istitle() stringdeki kelimelerin sadece ilk harfi büyük ise True değeri döner.

.isupper() stringdeki kelimelerin hepsi büyük harfle yazılmış ise True değeri döner.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.istitle())
str6 = "Ne Mutlu Türküm Diyene. >> Mustafa Kemal Atatürk"
print(str6.istitle())

"""
"x".join(str) str stringindeki/listesindeki her bir elemanın arasına "x" işaretini koyar.
"""

str7 = "KSK"
print(".".join(str7))
liste1 = ["01","11","1912"]
print("/".join(liste1))

"""
len(str) str içindeki elemanların sayısını veriri.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(len(string))

"""
.ljust(x,"y") stringin uzunluğunu x değerine tamamlayana kadar "y" karakterini girer.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.ljust(50,"*"))

"""
.lower() stringdeki tüm harfleri küçük harfe çevirir.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.lower())

"""
.lstrip("x") stringin başındaki "x" elemanını siler
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.lstrip("ne"))

"""
x = "abcd"
y = "1234"
.maketrans(x,y) stringdeki x değerlerini index sırasına göre y değerleriyle değiştirir.
kullanabilmek için string.translate(string.maketrans(x,y)) veya,
xy = string.maketrans(x,y)
string.translate(xy)

"""

string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
bunu = "emtd"
bunla = "1234"
print(string)
print(string.translate(string.maketrans(bunu,bunla)))

"""
max(x) alfabetik olarak x stringindeki en büyük değeri döndürür.(makine diline göre)

min(x) alfabetik olarak x stringindeki en küçük değeri döndürür.(makine diline göre)
"""
str8 = "kaz"
print(max(str8))
print(min(str8))

"""
.replace("x","y") stringdeki "x" değerini "y" değeri ile değiştirir.
"""
str2 = "12meko35"
print(str2.replace("12","COR"))

"""
.split("x",y) stringeki elemanlı "x" elemanından "x" elemanına kadar olan kısmını listeye tek eleman halinde ekler,
"x" değeri girmezsek default olarak boşlukların arasını ayırır.
y fonksiyonun kullanırsak, y defa ayırmak istediğimizi belirtmiş oluruz.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.split())
print(string.split("e"))
print(string.split("e",2))
liste2 = string.split()
print(type(liste2))

"""
.splitlines() stringdeki satırları listeye eleman olarak atar.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.splitlines())

"""
.sprit("x") stringin başındaki ve sonundaki "x" karakterlerini siler.
"""

str9 = "--- MUSTAFA KEMAL -- ATATÜRK----"
print(str9.strip("-"))

"""
.swapcase() stringdeki büyük harfleri küçük, küçük harfleri ise büyük harfe çevirir.
"""
print(string.swapcase())

"""
.title() stringdeki bütün kelimelerin baş harflerini büyük harfe çevirir
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.title())

"""
.upper() stringdeki bütün harfleri büyük harfe çevirir.
"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print(string.upper())

"""
.zfill(x) stringi x değerinde index sayısı oluncaya kadar başına 0 değerini ekler.

"""
string = "ne mutlu Türküm diyene.\nMUSTAFA KEMAL ATATÜRK."
print("string uzunluğu : " + str(len(string)))
print(string.zfill(47))
print(string.zfill(52))