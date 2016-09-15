##################################################
## module: fermat_primes_py2.py
## author: Misty Jenkins
## A#: A01489174
## tests numbers using Fermat's Little Theorem
## 09/07/2016
##################################################

#!/usr/bin/python

from random import randint
from newton_sqrt_py2 import newton_sqrt

def is_even(e):
	return not bool(e%2)
	
def remainder(a, b):
	return a%b

def expmod(b, e, m):
	if (e == 0):
		return 1
	elif ( is_even(e) ):
		x = expmod(b, e/2, m);
		return remainder(x*x, m)
	else:
		return remainder(b * expmod(b, e-1, m), m)
		
def fermat_test(n):
	if (n<2):
		return False
	elif (n==2):
		return True
		
	a = randint(2, n-1)
	return expmod(a,n,n) == a
	
def is_fermat_prime(n, num_times):
	if ( num_times == 0 ):
		return True;
	elif ( fermat_test(n) ):
		return is_fermat_prime(n, num_times-1);
	else:
		return False;
		
def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for d in xrange(2, int(newton_sqrt(n))+1):
			if n % d == 0:
				return False
		return True

def sum_of_fermat_primes(start, end, num_times):
	rslt = 0
	for i in xrange(start, end):
		if is_fermat_prime(i, num_times):
			rslt += i
	return rslt

def sum_of_primes(start, end):
	rslt = 0
	for i in xrange(start, end):
		if is_prime(i):
			rslt += i
	return rslt

def test_sum_diff_in_range(n):
	sp = sum_of_primes(0, n)
	sfp = sum_of_fermat_primes(0, n, 10)
	print 'sum of primes = ', sp
	print 'sum of fermat primes = ', sfp
	print 'sum diff = ', sfp - sp
