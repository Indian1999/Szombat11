import numpy as np # terminálba: pip install numpy
import random

tömb = np.array([4, 2, 1, 2, 4, 8])
print(tömb)
print(type(tömb)) # <class 'numpy.ndarray'>
print(tömb.shape)
# A tömb tulajdonságai:
# Az elemek száma nem módosítható (nem tudunk törölni/hozzáadni elemet létrehozás után)
# Az elemek típusa ugyan olyan kell, hogy legyen

matrix = np.array([[1,2,3], [4,5,6]])
print(matrix)
print(matrix.shape)

zeros = np.zeros((5,8)) # 5*8-as mátrix, tele 0-val
print(zeros)
ones = np.ones((10,)) # 10 elemű 1 dimenziós tömb, tele 1-esekkel
print(ones)
sevens = np.full((3, 6), 7)
print(sevens)

print(np.random.randint(1, 5)) # 5 az már nincs benne
print(random.randint(1,5)) # 5 is benne lehet

random_matrix = [[random.randint(-100, 200) for j in range(10)] for i in range(5)]
print(random_matrix)

random_array = np.random.randint(-100, 201, (3, 5, 2, 4))
print(random_array)
print(random_array.shape)

range_array = np.arange(3, 100, 6)
print(range_array)

szamok = np.linspace(0, 2, 101)
print(szamok)

print(szamok[3])
print(szamok[4:10])

matrix = np.random.randint(1, 10, (5, 6))
print(matrix)
print(matrix[3][2])
print(matrix[3, 2])
print(matrix[2, :])

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2) # [1, 2, 3, 4, 5, 6]
print(lista1 * 2)

tömb1 = np.array([1,2,3])
tömb2 = np.array([4,5,6])
print(tömb1 + tömb2) # [5 7 9]
print(tömb1 * 5)
print(tömb1 ** 2)