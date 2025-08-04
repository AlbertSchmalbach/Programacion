from cleaner import cleaning

cleaning()

list1 = [16, 2, 7]
list2 = [4, 3, 5]

# new_lst = [(list1[i] + list2[i]) for i in range(len(list1))]
new_lst = [x+y for x, y in zip(list1, list2)]


print(new_lst)