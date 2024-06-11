import random

# generowanie liczb pesudolosowcyh

print(random)

print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int 1 do 99
print(random.randrange(7))  # int 0..6
print(random.random())  # 0 do 0.99999
print(random.random() * 10)  # 0 do 9.99999

lista = [6, 12, 34, 56, 67, 89, 120]
print(random.choice(lista)) # losowanie z listy

lisa_kule = list(range(1,50))
print(lisa_kule)

wyn = random.choice(lisa_kule)
lisa_kule.remove(wyn)
print(wyn)
wyn = random.choice(lisa_kule)
lisa_kule.remove(wyn)
print(wyn)
wyn = random.choice(lisa_kule)
lisa_kule.remove(wyn)
print(wyn)
wyn = random.choice(lisa_kule)
lisa_kule.remove(wyn)
print(wyn)
wyn = random.choice(lisa_kule)
lisa_kule.remove(wyn)
print(wyn)

print(random.choices(lisa_kule,k=6))
print(random.sample(lisa_kule, k=6))
print(random.sample(lisa_kule, k=6))

print(lisa_kule)