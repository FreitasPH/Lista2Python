import random
from timeit import default_timer as timer

def share_diagonal(x0, y0, x1, y1):
	dy = abs(y1 - y0) 
	dx = abs(x1 - x0)
	return dx == dy 

def col_clashes(bs, c):
	for i in range(c):
		if share_diagonal(i, bs[i], c, bs[c]):
			return True

	return False  

def has_clashes(the_board):
	for col in range(1,len(the_board)):
		if col_clashes(the_board, col):
			return True
	return False

def main4():
	rng = random.Random()
	times = list(range(10))

	bd = list(range(4))
	num_found = 0
	tries = 0
	begin= timer()
	while num_found < 10:
		rng.shuffle(bd)
		tries += 1
		if not has_clashes(bd):
			end = timer()
			times[num_found] = end - begin
			print("Found solution {0} in {1} tries.".format(bd, tries))
			tries = 0
			num_found += 1
			begin = timer()

	print("Avarage time: {0}.".format(sum(times)/len(times)))

def main16():
	rng = random.Random()
	times = list(range(10))

	bd = list(range(16))
	num_found = 0
	tries = 0
	begin= timer()
	while num_found < 10:
		rng.shuffle(bd)
		tries += 1
		if not has_clashes(bd):
			end = timer()
			times[num_found] = end - begin
			print("Found solution {0} in {1} tries.".format(bd, tries))
			tries = 0
			num_found += 1
			begin = timer()

	print("Avarage time: {0}.".format(sum(times)/len(times)))

def main12():
	rng = random.Random()
	times = list(range(10))

	bd = list(range(12))
	num_found = 0
	tries = 0
	begin= timer()
	while num_found < 10:
		rng.shuffle(bd)
		tries += 1
		if not has_clashes(bd):
			end = timer()
			times[num_found] = end - begin
			print("Found solution {0} in {1} tries.".format(bd, tries))
			tries = 0
			num_found += 1
			begin = timer()

	print("Avarage time: {0}.".format(sum(times)/len(times)))

main4()
main12()
main16()

#The results show the exponencial growth in the time taken.
#Trying to simulate a 20x20 board will take more than a minute
