def is_par(num):
    if(num % 2 == 0):
        return f'{num} is a par number'
    return None

my_list = [1, 3, 2, 5, 6, 7, 9, 10, 16, 4]

# for num in my_list:
#     num_is_par = is_par(num)
#     if num_is_par is not None:
#         print(num_is_par)

# for num in my_list:
#     if(num_is_par := is_par(num)) is not None:
#         print(num_is_par)



if status:= input('Codigo de estado: ') == '200':
    print('Ok')
else:
    print('Error 403')