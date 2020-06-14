
l = [1,2,3,4,5]
print(type(l))

new_l = [x**2 for x in l if x%2 == 0]
print(new_l)
print(type(new_l))

list = [1,5,3,2,4,6,7,66,5,22,3,12,4,1,13,77,8,9,80,99]
n_l = [y*1 for y in list if y%2 == 0]
print(n_l)
