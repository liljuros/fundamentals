import pytz
from datetime import datetime, timezone

# for tz  in pytz.all_timezones:
#     print(tz)

# tz_chicago = pytz.timezone('America/Chicago')
# tz_utc = pytz.timezone('UTC')
# print(tz_utc)

dt_naive = datetime(2020, 5, 15, 10, 0)
print(dt_naive)
tz_chicago = pytz.timezone('America/Chicago')
dt_chicago = tz_chicago.localize(dt_naive)
print(dt_chicago.tzinfo)
print(pytz.UTC.localize(datetime.utcnow()))