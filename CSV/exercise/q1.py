import csv
# with open('file1.csv') as f:
#     next(f)
#     reader = csv.reader(f)
#     result = []
#     for row in reader:
#         for i in row:
#             result.append(int(i))
#
#     print(f"The min is {min(result)} and the max is {max(result)}")

# with open('file2.csv') as f:
# #    next(f)
#     reader = csv.reader(f)
#     result = []
#     for row in reader:
#         for i in row:
#             result.append(float(i))
#
#     print(f"The min is {min(result)} and the max is {max(result)}")

# with open('file3.tsv') as f:
#     next(f)
#     reader = csv.reader(f, delimiter="\t")
#     result = []
#     for row in reader:
#         for i in row:
#             result.append(int(i))
#
#     print(f"The min is {min(result)} and the max is {max(result)}")

with open('file4.csv') as f:
    next(f)
    reader = csv.reader(f, delimiter='|')
    result = []
    for row in reader:
        for i in row:
            result.append(i.rstrip('-').replace('---', '-'))

    print(f"The min is {min(result)} and the max is {max(result)}")