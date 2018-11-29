'''
   calculate time in miliseconds using epoch 

'''
import datetime

def main():
	try:
		epoch = datetime.datetime.utcfromtimestamp(0)
	except:
		epoch = datetime.datetime(1970,1,1)
	i = datetime.datetime.now()

	delta_time = (i - epoch).total_seconds()
	print(int(delta_time), delta_time)

if __name__ == "__main__":
	main()	

