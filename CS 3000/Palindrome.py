import random
import string

memory = {}

def longestPalindromeSubsequence(s:str) -> str:
	# Base cases
	if s in memory:
		return memory[s]
	
	if len(s) == 0:
		result = ""
	elif len(s) == 1:
		# Just return it, as a length 1 is a palindrome
		result = s
	elif len(s) == 2:
		# If they match, then we have a palindrome
		if s[0] == s[1]: 
			result = s
		# No match means no luck
		else:
			result = s[0]
	# Recursive cases
	# Fist and last match - add that to the longest in the middle
	else:
		if s[0] == s[-1]:
			result = s[0] + longestPalindromeSubsequence(s[1:len(s)-1]) + s[-1]
		else:
			# First and last don't match - either keep the first, or keep the last, whichever is larger
			keepFirst = longestPalindromeSubsequence(s[0:len(s)-1])
			keepLast = longestPalindromeSubsequence(s[1:])
			if len(keepFirst) >= len(keepLast):
				result = keepFirst
			else:
				result = keepLast
	memory[s] = result
	return result

# Dr B - I put this together for testing
def generatePalindromeWithAnswer(size):
	aLeftSide = ""
	aRightSide = ""
	pLeftSide = ""
	pRightSide = ""
	for i in range(size):
		c = random.choice(string.ascii_letters)
		if random.random() > .5 or i == size-1:
			aLeftSide += c
			aRightSide = c + aRightSide
			pLeftSide += c
			pRightSide = c + pRightSide
		else:
			pLeftSide += c
	return [aLeftSide+aRightSide, pLeftSide+pRightSide]

if __name__ == "__main__":
	print("Longest palindrome subsequence for 'character' = " + longestPalindromeSubsequence("character"))
	
	for i in range(10,50):
		problem = generatePalindromeWithAnswer(i)
		returned = longestPalindromeSubsequence(problem[1])
		print("Size: " + str(i))
		print("\tProblem : " + str(problem[1]))
		print("\tAnswer  : " + str(problem[0]))
		print("\treturned: " + str(returned))

