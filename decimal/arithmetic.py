import decimal
from decimal import Decimal

ctx = decimal.getcontext()
ctx.prec = 5
print(decimal.getcontext())
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(decimal.getcontext())