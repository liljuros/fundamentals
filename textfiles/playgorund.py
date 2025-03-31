file_name = "DEXUSEU.csv"

# file = open(file_name, 'r')
#
# print(next(file))

data = []

with open(file_name) as f:
    headers = next(f)

    for row in f:
        row = row.strip()
        date, value_str = row.split(',')
        try:
            value = float(value_str)
            data.append((date, value))

        except ValueError:
            pass

print(data)

