import numpy as np # terminálba: pip install numpy
import random

tömb = np.array([4, 2, 1, 2, 4, 8])
print(tömb)
print(type(tömb)) # <class 'numpy.ndarray'>

# A tömb tulajdonságai:
# Az elemek száma nem módosítható (nem tudunk törölni/hozzáadni elemet létrehozás után)
# Az elemek típusa ugyan olyan kell, hogy legyen