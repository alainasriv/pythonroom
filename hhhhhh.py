x = 0
y = 1
z = 0

while y < 1000:
	z = y
	y = x + y
	x = z
	
	print x
	
	