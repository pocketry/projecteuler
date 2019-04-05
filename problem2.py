sum = 0

def genfib(last, last2, sum):
	next = last + last2
	print(next)
	if next <= 4000000:
		if next % 2 == 0:
			sum += next	
		genfib(next, last, sum)
	else:
		print(sum)

genfib(1,1, sum)