def find_uniq(arr):
    # do the magic
    unique = []
    for item in arr:
	    uniqueLetters = []
	    letters = list(item)
	    for letter in letters:
	    	if letter.lower() not in uniqueLetters:
	    		uniqueLetters.append(letter.lower())
	    unique.append(sorted(uniqueLetters))

    for item in unique:
    	if unique.count(item) == 1:
    		return (arr[unique.index(item)])



print (find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))
print (find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))