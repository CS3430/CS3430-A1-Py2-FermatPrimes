##################################################
## module: newton_sqrt_py3.py
## author: Misty Jenkins
## A#: A01489174
## tests numbers using Fermat's Little Theorem
## 09/07/2016
##################################################

def average(x, y):
	return (x+y)/2.0
	
def next_guess(n, g):
	return average(g, float(n)/g)
	
def is_good_enough(n, g, error):
	return abs(g**2 - n) <= error

def newton_square_root(n, g, error):
	if is_good_enough(n, g, error):
		return g
	else:
		ng = next_guess(n, g)
		return newton_square_root(n, ng, error)

def newton_sqrt(n):
	return newton_square_root(n, 1, 0.0001)
