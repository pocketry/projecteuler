sum = 0
for count in range(1,1000):
	if count % 3 == 0:
		sum += count
	elif count %5 == 0:
		sum += count
	print(str(count) + ' ' + str(sum))

print(sum)