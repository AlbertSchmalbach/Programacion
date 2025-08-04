import random

# # f_name = input('Type the file name: ')
# f_name = "petnames.txt"
# f = open(f_name)
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(f_content_list)
# # print(random.choice(f_content_list))

frutas = ['manzana', 'piña', 'uva']
frutas_reves = []
for frutas in reversed(frutas):
    frutas_reves.append(frutas)
print(frutas_reves)