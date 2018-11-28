from datetime import datetime

try:

	epoch = datetime.datetime.utcfromtimestamp(0)
except
	epoch = datetime.datetime(1970,1,1)

i = datetime.now()

delta_time = (i - epoch).total_seconds()
print(delta_time)
