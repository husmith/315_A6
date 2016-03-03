import fileinput

DICTIONARY = []

def in_dict(string):
	return string in DICTIONARY

def prepare_dictionary(dictfile):
	with fileinput.input(dictfile) as dfile:
		for line in dfile:
			DICTIONARY.append(line.rstrip('\n'))
	fileinput.close()
	
def stringSplitIter(phrase):
	SPLIT_ITER = []
	cansplit = splitIter(phrase, 0, SPLIT_ITER)
	if not cansplit:
		print("NO, cannot be split.",end="\n\n")
		return None
	else:
		print("YES, can be split.")
		return SPLIT_ITER

def splitIter(x, i, result):
	if in_dict(x[i:]):
		result.append(x[i:])
		return True
	for j in range(i,len(x)):
		if in_dict(x[i:j+1]):
			if splitIter(x,j+1,result):
				result.append(x[i:j+1])
				return True
	return False

def splitMemo(x, i, memo):
	if in_dict(x[i:]):
		memo[-1] = x[i:]
		return True
	if memo[i] == -1:
		return False
	for j in range(i,len(x)):
		if in_dict(x[i:j+1]):
			if splitMemo(x,j+1,memo):
				memo[j+1] = x[i:j+1]
				return True
	memo[i] = -1
	return False

def stringSplitMemo(phrase):
	SPLIT_MEMO = [0] * len(phrase)
	cansplit = splitMemo(phrase, 0, SPLIT_MEMO)
	if not cansplit:
		print("NO, cannot be split.",end="\n\n")
		return None
	else:
		print("YES, can be split.")
		result = []
		[result.append(string) for string in SPLIT_MEMO if isinstance(string,str)]
		return result

def main():
	with fileinput.input() as f:
			numStrings = int(f.readline().rstrip('\n'))
			phrases = []
			for s in range(numStrings):
				phrase = f.readline().rstrip('\n')
				phrases.append(phrase)
			for index, p in enumerate(phrases):
				print("phrase number: "+str(index+1))
				print(p)
				print("MEMOIZED: ")
				memo_result = stringSplitMemo(p)
				if memo_result != None:
					[print(el,end=' ') for el in memo_result]
					print('\n')
				print("ITERATIVE: ")
				iter_result = stringSplitIter(p)
				if iter_result != None:
					[print(el,end=' ') for el in reversed(iter_result)]
					print('\n')


if __name__ == '__main__':
	prepare_dictionary('diction10k.txt')
	main()
