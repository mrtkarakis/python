"""
.add(x) kümenin sonuna x elemanını ekler.
"""

x = {1,2,3}
x.add(4)
print(x)


"""
x.difference(y) x kümesinde olup y kümesinde olmayan elemanları döndürür.
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
x1_x2=x1.difference(x2)
x2_x1=x2.difference(x1)
print(x1_x2,"\n",x2_x1)


"""
x.difference_update(y) x ve y kümesinde olan elemanı çıkartır ve x kümesini günceller. 
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
x1.difference_update(x2)
x2.difference_update(x1)
print("güncel x1 kümesi : ", x1)
print("güncel x2 kümesi : ", x2)



"""
x.difference_update(y) x ve y kümesinde olan elemanı çıkartır ve x kümesini günceller. 
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
x1.difference_update(x2)
x2.difference_update(x1)
print("güncel x1 kümesi : ", x1)
print("güncel x2 kümesi : ", x2)



"""
x.intersection(y) x ve y kümesinde olan ortak elemanları döndürür. 
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
print(x1.intersection(x2))


"""
x.intersection_update(y) x ve y kümesinin ortak elemanlarını x kümesine kaydeder.
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
x1.intersection_update(x2)
print(x1)


"""
x.isdisjoint(y) x ile y kümesi arasında bir tane bile ortak eleman varsa False yoksa True değeri döndürür.
"""

x1 = {15,12,65,1,2,3,4,5,7}
x2 = {1,2,54,4,5,6,8}
print(x1.isdisjoint(x2))
x3 = {1,2,3}
x4 = {4,5,6}
print(x3.isdisjoint(x4))


"""
x.issubset(y) x kümesi y kümesinin alt elemanı ise True değeri döner.
"""

x1 = {1,2,3}
x2 = {1,2,3,4}
x3 = {5,6,7}
print(x1.issubset(x2))
print(x1.issubset(x3))
print(x2.issubset(x1))


"""
x.union(y) x ve y kümesinin birleşimini döndürür, kümeleri güncellemez. 
"""
x2 = {1,2,3,4}
x3 = {5,6,7}
print("x2+x3 : ",x2.union(x3))
print("x2 kümesi : ", x2)


"""
x.update(y) x kümesi ile y kümesini birleştirir ve bunu x kümesine kaydeder.
"""

x2 = {1,2,3,4}
x3 = {5,6,7}
x2.update(x3)
print("x2 kümesi : ", x2)