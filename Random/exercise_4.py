import random

face_value = ['9', '10', 'J', 'Q', 'K', 'A']

def simulate_throws(n):
    return [tuple(random.choices(face_value, k=2)) for _ in range(n)]

sample = simulate_throws(10)
frequincies = {}
for row in sample:
    print(row)
    for value in row:
        print(value)
        frequincies[value] = frequincies.get(value, 0) + 1

#print(frequincies)