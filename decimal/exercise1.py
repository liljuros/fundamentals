import csv
import decimal
from decimal import Decimal
from time import perf_counter

with open("transactions.csv") as f:
    t1_start = perf_counter()
    reader = csv.reader(f)
    reader.__next__()
    sales = 0
    for row in reader:
        sales += float(row[2])
    print(type(sales))
    t1_stop = perf_counter()
    print(t1_stop - t1_start)

with open("transactions.csv") as f:
    t2_start  = perf_counter()
    reader = csv.reader(f)
    reader.__next__()
    dec = Decimal()
    for row in reader:
        dec += Decimal(str(row[2]))
    print(type(dec))
    t2_stop = perf_counter()
    print(t2_stop - t2_start)
