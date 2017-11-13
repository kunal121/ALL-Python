import time
import calendar
# no of ticks till jan 1970
print time.time()
#time in local parameters
print time.localtime(time.time())
#formatted time
print time.asctime(time.localtime(time.time()))
# getting calendar of a specific month
print calendar.month(2008,1)
# current time like asctime but without arguments
print time.ctime()
