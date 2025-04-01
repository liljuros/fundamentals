# # import math
# # from functools import lru_cache
# # target_file= "output.txt"
# # # with open(target_file, 'w') as f:
# # #     f.write('i, fibonaci_i, factorial_i, gcd_fibonaci_i_factorial_i\n')
# # @lru_cache
# # def Fibonacci(n):
# #     if n<0:
# #         print("Incorrect input")
# #     # First Fibonacci number is 0
# #     elif n==0:
# #         return (0)
# #     # Second Fibonacci number is 1
# #     elif n==1:
# #         return (1)
# #     else:
# #         return (Fibonacci(n-1)+Fibonacci(n-2))
# # def fibonacci(n):
# #     if n <= 0:
# #         return "Positionen måste vara ett positivt heltal."
# #     elif n == 1:
# #         return 0
# #     elif n == 2:
# #         return 1
# #     else:
# #         a, b = 0, 1
# #         for _ in range(2, n):
# #             a, b = b, a + b
# #         return b
# #
# #
# # for i in range(10):
# #     print(i, fibonacci(i), math.factorial(i), math.gcd(fibonacci(i), math.factorial(i)))
#
# import math
# from functools import lru_cache
#
# @lru_cache
# def fibonacci(n):
#     if n < 0:
#         raise ValueError("Positionen måste vara ett positivt heltal eller noll.")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Skriv resultat till fil
# target_file = "output.txt"
# with open(target_file, 'w') as f:
#     f.write('i, fibonacci_i, factorial_i, gcd_fibonacci_i_factorial_i\n')
#     for i in range(10):
#         fib_i = fibonacci(i)
#         fact_i = math.factorial(i)
#         gcd = math.gcd(fib_i, fact_i)
#         f.write(f'{i}, {fib_i}, {fact_i}, {gcd}\n')
#         print(i, fib_i, fact_i, gcd)

with open('output.txt') as f:
    next(f)
    data = [row.strip().split(',') for row in f]

print(data)