'''
The rabbit problem
Input: Male_Rabbits, Female_rabbits, Rabbits_needed_alive
Output: Number of months until world domination

2 possibilities:
- dict with index = month and value = amountofbunnies (one dict for each gender) 
'''
from collections import defaultdict
import sys

def age(males, females):
	newMales = {}
	newFemales = {}
	total = 0
	for k, v in males.items():
		if k == 0:
			newMales[k] = v
			total += v
		elif k != 95:
			newMales[k+1] = v
			total += v

	for k, v in females.items():
		if k == 0:
			newFemales[k] = v
			total += v
		elif k != 95:
			newFemales[k+1] = v
			total += v


	return newMales, newFemales, total

	#[x+1 for x in list if not 0]
def offspring(males,females):
	fertile = 0
	for k,v in females.items():
		if k >= 4:
			fertile += v
	try:
		exM = males[0]
		exF = females[0]
	except KeyError:
		exM = 0
		exF = 0
	males[0] = exM + (fertile*5)
	females[0] = exF + (fertile*9)


def main():
	male_R = int(sys.argv[1])
	fem_R = int(sys.argv[2])
	needed = int(sys.argv[3])
	total = male_R + fem_R
	monthspassed = 0

	female = {}
	male = {}

	female[2] = fem_R
	male[2] = male_R

	while total < needed:
		offspring(male,female)
		male,female,total = age(male,female)
		monthspassed += 1

	print(monthspassed)


if __name__ == '__main__':
	main()