def mult(a, b, c):
    return a*b*c

mult = mult(8,5,6)
# print(mult)

def mult(*args):
    res = 1
    for i in args:
        res*=i
    return res

mult = mult(8,5,6)
print(mult)