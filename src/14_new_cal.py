import sys
import calendar
from datetime import datetime

today = datetime.today()
print(today)

month, year = today.month, today.year

cal = calendar.TextCalendar(firstweekday=6)
# print(calendar.month(today.year, today.month))
# or
# cal.prmonth(2020, 5)
#or

if len(sys.argv) == 1:
    calendar.prmonth(today.year, today.month)

elif len(sys.argv) == 2:
    calendar.prmonth(today.year, int(sys.argv[1]))

elif len(sys.argv) == 3:
    calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))

else:
  print("usage: filename month year")
  sys.exit(1)

# def parent(args):
#     script_name, *args = sys.argv
#     if not args:
#         rend_cal()
#     elif len(args) == 1:
#         month = int(args[0])
#         rend_cal(month)
#     elif len(args) == 2:
#         month, year = map(int, args)
#         rend_cal(month, year)
#     else:
#         print(utilization())