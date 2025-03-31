# file_name = "DEXUSEU.csv"
#
# # file = open(file_name, 'r')
# #
# # print(next(file))
#
# data = []
#
# with open(file_name) as f:
#     headers = next(f)
#
#     for row in f:
#         row = row.strip()
#         date, value_str = row.split(',')
#         try:
#             value = float(value_str)
#             data.append((date, value))
#
#         except ValueError:
#             pass
#
# print(data)

# # f = open('test.csv', 'w')
# # print(f.write('abc'))
# # print(f.write('123456'))
# # print(f.close())
# data = ['line 1', 'line 2', 'line 3']
# # with open('test.csv', 'r') as f:
# #     for line in f:
# #         print(line.strip())
# with open('test.csv', 'a') as f:
#     f.write('line4\n')
#     f.write('line5\n')

def split_date(dt_str):
    return dt_str[:4], dt_str[5:7], dt_str[8:]

def transform_row_for_output(row):
    row = row.strip()
    dt_str, rate = row.split(',')
    year, month, day = split_date(dt_str)
    try:
        float(rate)
    except ValueError:
        return ""
    month = str(int(month))
    day = str(int(day))
    result = ','.join([year, month, day, rate])
    result += '\n'
    return result

def transform_file_batch(source_file, target_file):
    with open(source_file) as f:
        data = f.readlines()
    del data[0]

    with open(target_file, 'w') as f:
        f.write('YEAR, MONTH, DAY, EXCH\n')
        for row in data:
            f.write(transform_row_for_output(row))

source_file = 'DEXUSEU.csv'
target_file = 'output.csv'
# with open(source_file) as f:
#     for _ in range(5):
#         print(next(f).strip())
with open(source_file) as f:
    data = f.readlines()

del data[0]
# data = [line.strip() for line in data]
# data = [line.split(',') for line in data]

with open(target_file, 'w') as f:
    f.write('YEAR, MONTH, DAY, EXCH\n')
    for row in data:
        f.write(transform_row_for_output(row))






#print(transform_row_for_output('2015-04-03,1.0990'))

