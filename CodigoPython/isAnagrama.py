text1 = input('Palabra1: ').lower()
text2 = input('palabra2: ').lower()

anagrama = []
notAnagrama = []


for l in text1:
    if l in text2:
        anagrama.append(l)
    else:
        notAnagrama.append(l)

if len(notAnagrama) == 0:
    print('Anagramas')
else:
    print('No son anagramas')
        