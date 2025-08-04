itemPrice = [12.3, 14.5, 16]
fruits = ['mango', 'banana', 'apple']

# Con list conprehesion
# fruits = {fruit:price for fruit, price in zip(fruits, itemPrice)}
# print(fruits)

# con dict
print(dict(zip(fruits, itemPrice)))