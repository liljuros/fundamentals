import csv
# with open('actors.csv') as f:
#     for row in f:
#         print(row)

# with open('actors.csv') as f:
#     for row in f:
#         row = row.strip()
#         fields = row.split(',')
#         print(fields)


#
# with open('actors.csv') as f:
#     reader = csv.reader(f,delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
import csv
nasdaq = 'nasdaq.csv'
census = 'st-2001est-01.csv'

# with open(nasdaq) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# def parse_nasdaq(f_name):
#     result = []
#
#     with open(f_name) as f:
#         reader = csv.reader(f)
#
#         headers = next(reader)
#         result.append(headers)
#
#         for row in reader:
#             row[-1] = float(row[-1])
#             result.append(row)
#     return result
#
# print(parse_nasdaq(nasdaq))
# def parse_census_data(file_name):
#     results = []
#     with open(file_name) as f:
#         reader = csv.reader(f)
#
#         headers = next(reader)
#         results.append(headers)
#         for row in reader:
#             area = row[0]
#             data = row[1:]
#             data = [area] + [int(field.replace(',', ''))for field in data]
#             results.append(data)
#     return results
#
# print(parse_census_data(census))

with open('test.csv') as f:
    for row in f:
        print(row, end='')