from decimal import *

pi_100 = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def pi_vs_100():
# Take user input for the value of pi.  This will be loaded as a string.
	pi = raw_input("You're a mathematician, eh?  What is the value of pi?")
	
# Check to see if the user entered more than 100 digits of pi; if they did, round their answer to 100 digits and compare it to the actual first 100 digits of pi.
	if len(pi) >= 101:
		pi = Decimal(pi)
		pi_rounded_to_100 = Context(prec=101).create_decimal(pi)
		if pi_rounded_to_100 == pi_100:
			print 'You are rediculous...'
		else:
			print 'LOL, nice try...'
# If the user entered less than 100 digits of pi, round pi_100 to the number of digits specified by the user and test against their input.
	else:
		pi_100_rounded = Context(prec=len(pi)-1).create_decimal(pi_100)
		#print pi_100_rounded
		if pi_100_rounded == Decimal(pi):
			print 'Close enough...'
		else:
			print 'LOL, try again silly mathematician...'

pi_vs_100()
