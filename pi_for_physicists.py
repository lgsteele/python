#This is a program that determines if you know the value of pi.  It assumes you are a physicist.
# To run (F5) enter the following command C:\Python27\Lib\idlelib\idle.py "$(FULL_CURRENT_PATH)"

def pi():
	a = raw_input("You are a physicist, eh?  What is the value of pi?\n")
	a = float(a)
	if a <= 5 and a >= 1:
		print "Eh, close enough..."
	else:
		print "*facepalm*"

pi()
