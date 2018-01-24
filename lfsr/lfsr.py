'''
LFSR - Linear Feedback Shift Registers
XOR = 
XNOR = AND which returns 1 with either all 0 or all 1
'''
import sys

def main():
	#all bits together (0+1+1+0 etc.) % 2 (wenn rest 1 then 1 else 0)
	tapstring = sys.argv[1]
	taps = [int(x) for x in tapstring.split(',')]
	method = sys.argv[2]
	seq = [int(x) for x in sys.argv[3]]
	clock = int(sys.argv[4])

	print("0\t"+str(seq))

	#if method == 'XOR':
	for x in range(1,clock+1):
		xorsum = sum([seq[k] for k in taps])
		trash = seq.pop()
		if method == 'XOR':
			seq.insert(0,xorsum%2)
		elif method == 'XNOR':
			if (xorsum == 0 or xorsum == len(taps)):
				seq.insert(0,1)
			else:
				seq.insert(0,0)
		print("%s\t%s" % (x, str(seq)))


if __name__ == '__main__':
	main()