import random

# for _ in range(5):
#     print(random.randint(5, 25))

#print(random.randrange(1,600))
# s = 'abcdefg'
# print(s.ljust(10, '*'))

random.seed(0)

data = [random.randint(1,10) for _ in range(5)]

freq = {}

for el in data:
    freq[el] = freq.get(el, 0) + 1

def freq_dist(data):
    freq = {}
    for el in data:
        freq[el] = freq.get(el, 0) + 1

    return freq

freq = freq_dist(data)

sum_freq = sum(freq.values())

relative_freq = freq.copy()

for k in relative_freq:
    relative_freq[k] = relative_freq[k] / sum_freq * 100

print(relative_freq)