#print(chr(97))
s = 'Π, ύ, θ, ω, ν'
data = "".join(s.split())
# print(data)
# print(ord(data[0]))
for i in data:
    if i != ',':
        print(f"For letter: {i}")
        print(i.upper())
        print(i.lower())
        print(hex(ord(i)))