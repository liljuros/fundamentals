# #print(chr(97))
# s = 'Π, ύ, θ, ω, ν'
# data = "".join(s.split())
# # print(data)
# # print(ord(data[0]))
# for i in data:
#     if i != ',':
#         print(f"For letter: {i}")
#         print(i.upper())
#         print(i.lower())
#         print(hex(ord(i)))

# a = input("Give me a number: ")
# if int(a)%2 == 0:
#     print(f"The number {a} is even")
# else:
#     print(f"The number {a} is uneven")

a, b = input("Give me two numbers, non-zero: ").split()
print(f"a /b = {(int(a)/int(b)):.2f}")