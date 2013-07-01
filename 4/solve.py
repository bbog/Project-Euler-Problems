'''
URL: http://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def isPalindrome(number):

	reversedNumber = str(number)[::-1]

	if str(number) == reversedNumber:
		return True

	return False


# brute force ftw
def getLargestPalindrome(numberOfDigits):

	first = 10**(numberOfDigits - 1)
	last = 10**numberOfDigits
	
	largestPalindrome = 0

	for num1 in range(last - 1, first, -1):
		for num2 in range(last - 1, first, -1):
			
			product = num1 * num2
			if isPalindrome(product):
				if product > largestPalindrome:
					largestPalindrome = product

	return largestPalindrome
	

def main():

	# test
	# print getLargestPalindrome(2)

	print getLargestPalindrome(3)


	
if __name__ == '__main__':
     main()