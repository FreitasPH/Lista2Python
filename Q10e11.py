#This is the resolution of both questions 10 and 11
import time

def calculate_time(func):
	def wrapper(*args, **kwargs):
		
		begin = time.time()
		func(*args, **kwargs)
		end = time.time()

		print("Execution time: {0}".format(end - begin))
	
	return wrapper

@calculate_time
def plusOperator(*args, **kwargs):
	result = args[0]
	for i in args[1:]:
		result = result + i
	print("Using the + operator with the folowing elements: ({0}) results in: {1}".format(kwargs, result))

plusOperator(10,20,30, first = 10, second = 20, third = 30)

plusOperator("CES","-","22",first = "CES", second = "-", third = "22")
