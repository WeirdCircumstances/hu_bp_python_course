from random import randint

def guess():
	x = randint(0,100)
	n = int(raw_input("Rate die Zahl zwischen 0 und 100: "))
	y = 0
	while x != n:
		y = y+1
		if n < x:
			print 'Die gesuchte Zahl ist groesser.'
			n = int(raw_input("Please enter an integer: "))
		elif n > x:
			print 'Die gesuchte Zahl ist kleiner.'
			n = int(raw_input("Please enter an integer: "))
	else:
		print('Treffer, das war die Zahl. \nDu hast {} Versuche gebraucht' .format(y))

guess()
