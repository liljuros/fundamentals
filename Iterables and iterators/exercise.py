# l = [10, 'abc', 3.14, True]
# for i in l:
#     print(f'Values is: {i} position is {l.index(i)}')

from time import perf_counter

start = perf_counter()
# g = (i ** i for i in range(1, 10_001))
g = [i ** i for i in range(1, 10_001)]
for i in range(10):
    for value in g[:5]:
        print(value)
    # print(next(g))
end = perf_counter()
print('elapsed:', end - start)

