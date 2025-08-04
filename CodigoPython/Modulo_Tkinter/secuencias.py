def skip_elements(elements):
	# code goes here
	chars = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			chars.append(element)

	return chars

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']