import random

data = ['9', '10', 'J', 'Q', 'K', 'A']

def make_sample_space():
    sample = []
    for i in range(len(data)):
        for j in range(len(data)):
            sample.append((data[i], data[j]))
    return sample
sample_space = make_sample_space()

def simulate_throws_from_sample_space(number, samples):
    throws = []
    for _ in range(number):
        throws.append(random.choice(samples))
    return throws

print(simulate_throws_from_sample_space(5, sample_space))

# def make_sample_space(space):
#     sample = []
#     for _ in range(space):
#         sample.append(tuple(random.sample(data, 2)))
#     return sample
#
# print(make_sample_space(10))