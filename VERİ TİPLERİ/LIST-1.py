"""
len(x) x listesinin uzunluğunu döndürür.
"""
liste1 = ["mavi","sarı","beyaz","yeşil","kırmızı"]
liste2 = [1,2,3,4,5,6,7]
print(len(liste1))
print(len(liste2))


"""
max(x)\
.   ----> listedeki en büyük/küçük değeri döndürür.
min(x)/
"""
liste1 = ["mavi","sarı","beyaz","yeşil","kırmızı"]
liste2 = [1,2,3,4,5,6,7]
print(max(liste1))
print(max(liste2))
print("-----------")
print(min(liste1))
print(min(liste2))


"""
list(x) x demetini liste veri tipine çevirir.
"""
demet1=("ali","mehmet","murat")
demet2=(1,2,3,4,5,6)
print(list(demet1))
print(list(demet2))


"""
.count(x) x değerinin listede kaç defa geçtiğini döndürür.
"""

liste3 = ["abc","def","135","abc"]
print(liste3.count("abc"))
print(liste3.count("def"))


"""
y.extend(x) y listesinin sonuna x listesini ekler. 
"""

liste1 = ["mavi","sarı","beyaz","yeşil","kırmızı"]
liste2 = [1,2,3,4,5,6,7]
liste1.extend(liste2)
print(liste1)


"""
.index("x") "x" elemanın kaçıncı indexte olduğunu döndürür.
"""

liste1 = ["mavi","sarı","beyaz","yeşil","kırmızı"]
print(liste1.index("yeşil"))


"""
.insert(x,y) listenin x'inci indexine y değerini ekler.
"""

liste2 = [1,2,3,4,5,6,7]
liste2.insert(5,9)
print(liste2)


"""
.pop(x) listeden çıkartmak istediğimiz elemanın index değerini x olarak yazarız, hiç bir değer girmezsek sonuncu elemanı çıakrtır.
"""

liste2 = [1,2,3,4,5,6,7]
print(liste2.pop())
print(liste2.pop(3))
print(liste2)


"""
.remove("x") listeden çıkartmak istediğimiz elemanın adını yazarak listeden çıkartabiliriz.
"""

liste2 = [1,2,3,4,5,6,7]
liste2.remove(6)
print(liste2)


"""
.reverse() listeyi ters çevirir.
"""

liste1 = ["mavi","sarı","beyaz","yeşil","kırmızı"]
liste1.reverse()
print(liste1)


"""
.sort() liste elemanlarını küçükten büyüğe sıralar.
"""

liste2 = [1,2,3,4,5,6,7]
liste2.reverse()
print("reverse edilmiş liste2 : ", liste2)
liste2.sort()
print("küçükten büyüğe sıralama komudu ile liste2 : ", liste2)