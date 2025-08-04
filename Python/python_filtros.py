countries = ["France", "Uruguay", "Germany", "Netherlands", "Ghana"]



map_filter = map(lambda country: country[0] == 'G', countries)
print(f'Con Map: {map_filter}')
print(type(map_filter)) # class map

filter = filter(lambda country: country[0] == 'G', countries)
print(f'Con filter: {filter}')
print(type(filter)) # class filter

a = [[96], [69]]

print ("".join (list (map (str, a))))

z = ["alpha"," bravo"," charlie"]
new_z = [i[0]*2 for i in z]
print (new_z)