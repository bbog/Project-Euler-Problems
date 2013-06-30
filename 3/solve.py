'''
URL: http://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''



def getLargestPrimeFactor(number):

	# first version was slow as hell, so... let's cheat a little : D
	# credits: http://primes.utm.edu/lists/small/100000.txt
	for line in reversed(open('primes.txt').readlines()):
		line = line.rstrip()
		line = ' '.join(line.split())
		if line:
			for prime in line.split(' '):
				if number % int(prime) == 0:
					return prime

	return 1

def main():

	# test
	# print getLargestPrimeFactor(13195)

	print getLargestPrimeFactor(600851475143)


	
if __name__ == '__main__':
     main()