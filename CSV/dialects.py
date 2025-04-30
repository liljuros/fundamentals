import csv

#print(csv.list_dialects())

# with open('actors.pdv') as f:
#     for row in f:
#         print(row.strip())

# with open('actors.pdv') as f:
#     reader = csv.reader(
#         f,
#         delimiter='|',
#         quotechar="'",
#         escapechar="\\",
#         skipinitialspace=True
#         )
#     for row in reader:
#         print(row)

csv.register_dialect(
    'pdv',
    delimiter='|',
    quotechar="'",
    escapechar="\\",
    skipinitialspace=True

)

print(csv.list_dialects())

with open('actors.pdv') as f:
    reader = csv.reader(f, dialect='pdv')
    for row in reader:
        print(row)