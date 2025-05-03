import random

# Ha egy változót konstansnak szánunk (nem változik az értéke),
# akkor azt illendő csupa nagybetűvel elnevezni
TARGET = "Ez itt a genetikus algoritmus programja."
POPULATION_SIZE = 100
MUTATION_RATE = 0.01 # Egy egyed egy karaktere ennyi eséllyel mutálódik
GENERATIONS = 1000
CHARS = "öüóqwertzuiopőúűasdfghjkléáíyxcvbnmÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁÍYXCVBNM ,.?!"

def random_egyed():
    """Létrehoz egy a TARGET hosszával megegyező random stringet (egyedet)"""
    egyed = ""
    while len(egyed) != len(TARGET):
        egyed += random.choice(CHARS)
    return egyed

def fitness(egyed):
    """Visszaadja egy egyednek a rátermettségi értékét (hány karakter egyezik meg a TARGET-hez képest)"""
    pass

def keresztezés(szülő1, szülő2):
    """2 szülő alapján létrehoz egy új egyedet"""
    pass

def mutáció(egyed):
    """A MUTATION_RATE alapján mutálja az egyes értékeit az egyednek és visszaadja a mutált egyedet"""
    pass

def kiválasztás(populáció):
    """Kiválaszt 5 random egyedet a megadott populációból, és eközül az 5 egyed közül visszaadja a legjobbat"""
    pass

def genetic_algorithm():
    """Futtatja a genetikus algoritmust"""
    pass

genetic_algorithm()
