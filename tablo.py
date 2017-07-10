def flap_display(lines, rotors):
	result = []
	arr = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789')
	for k in range(0, len(lines)):
		word = lines[k]
		newLines = []
		for i in range(0, len(word)):
			index = arr.index(word[i])
			newIndex = index + rotors[k][i]

			for j in range(0, i):
				newIndex += rotors[k][j]
			
			while newIndex >= len(arr):
				newIndex -= len(arr)
				
			newLines.append(arr[newIndex])


		result.append(''.join(newLines))
	return result

print (flap_display(["CODE"], [[20,20,28,0]]))