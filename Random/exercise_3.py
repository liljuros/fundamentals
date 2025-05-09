import random

face_value = ['9', '10', 'J', 'Q', 'K', 'A']

def simulate_throws(n):
    return [tuple(random.choices(face_value, k=2)) for _ in range(n)]

print(simulate_throws(10))