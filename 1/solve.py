'''
URL: http://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


# Determines if a number is a multiple of a given list of divisors
def isMultipleOf(number, *divisors):

	for divisor in divisors:
		if number % divisor == 0:
			return True
	return False


def getSumOfMultiplesBelowLimit(limit, *divisors):
	
	totalSum = 0

	for number in range(1, limit):
		if isMultipleOf(number, *divisors):
			totalSum += number
	return totalSum


def main():
	# test case
	#print getSumOfMultiplesBelowLimit(10, 3, 5)

	print getSumOfMultiplesBelowLimit(1000, 3, 5)


if __name__ == '__main__':
     main()