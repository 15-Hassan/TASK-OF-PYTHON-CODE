
def selectionSort(sbhp, size):
	
	for i in range(size):
		min_index = i

		for j in range(i + 1, size):
			
			if sbhp[j] < sbhp[min_index]:
				min_index = j
	
		(sbhp[i], sbhp[min_index]) = (sbhp[min_index], sbhp[i])

sbhp = [644, 977, 112, 341, 681, 97, 55]
size = len(sbhp)
selectionSort(sbhp, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(sbhp)
