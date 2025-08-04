stream = open('text.txt', 'rt', encoding='utf-8')

# read()
# print(stream.read(10))

# readline()
# print(stream.readline())

# readlines()
# print(stream.readlines())

# write()
file = open('newtext.txt', 'wt')
for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
file.close()
	
# lectura de nuevo txt
arch = open('newtext.txt', 'rt')
print(arch.read())
arch.close()
