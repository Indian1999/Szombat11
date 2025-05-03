import random

# Ha egy változót konstansnak szánunk (nem változik az értéke),
# akkor azt illendő csupa nagybetűvel elnevezni
TARGET = "Hello World!"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01 # Egy egyed egy karaktere ennyi eséllyel mutálódik
GENERATIONS = 1000
CHARS = "öüóqwertzuiopőúűasdfghjkléáíyxcvbnmÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁÍYXCVBNM ,.?!"

def population_to_file(populáció, file_path):
    with open(file_path, "w", encoding = "utf-8") as f:
        for egyed in populáció:
            f.write(egyed + "\n")
            
def random_egyed():
    """Létrehoz egy a TARGET hosszával megegyező random stringet (egyedet)"""
    egyed = ""
    while len(egyed) != len(TARGET):
        egyed += random.choice(CHARS)
    return egyed

def fitness(egyed):
    """Visszaadja egy egyednek a rátermettségi értékét (hány karakter egyezik meg a TARGET-hez képest)"""
    fitness_score = 0
    for i in range(len(TARGET)):
        if TARGET[i] == egyed[i]:
            fitness_score += 1
    return fitness_score

def keresztezés(szülő1, szülő2):
    """2 szülő alapján létrehoz egy új egyedet"""
    index = random.randint(2, len(TARGET) - 2)
    gyermek = szülő1[:index] + szülő2[index:]
    return gyermek

def mutáció(egyed):
    """A MUTATION_RATE alapján mutálja az egyes értékeit az egyednek és visszaadja a mutált egyedet"""
    mutált_egyed = ""
    for char in egyed:
        if random.random() < MUTATION_RATE:
            mutált_egyed += random.choice(CHARS)
        else:
            mutált_egyed += char
    return mutált_egyed

def kiválasztás(populáció, k = 5):
    """Kiválaszt k (alapból 5) random egyedet a megadott populációból, és eközül az 5 egyed közül visszaadja a legjobbat"""
    egyedek = random.choices(populáció, k = k)
    return max(egyedek, key = fitness)

def legjobb(populáció):
    """Az adott populációból visszaadja a legrátermetteb egyedet"""
    return max(populáció, key = fitness)

def genetic_algorithm():
    """Futtatja a genetikus algoritmust"""
    populáció = [random_egyed() for i in range(POPULATION_SIZE)]
    for generation in range(GENERATIONS):
        best = legjobb(populáció)
        print(f"{generation + 1}. generáció: {best} (Rátermettség: {fitness(best)})")
        population_to_file(populáció, f"generations/generation{generation+1}.txt")
        
        if best == TARGET:
            print("Optimális megoldás megtalálva!")
            break
        
        új_populáció = [best]
        while len(új_populáció) != POPULATION_SIZE:
            egyed = keresztezés(kiválasztás(populáció), kiválasztás(populáció))
            egyed = mutáció(egyed)
            új_populáció.append(egyed)
        populáció = új_populáció[:]
        
genetic_algorithm()
