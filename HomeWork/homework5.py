immutable_var = ("green", "blue", True, 15)
print(immutable_var)

#immutable_var[1] = "black"     #TypeError: 'tuple' object does not support item assignment
#print(immutable_var)      Кортеж не поддерживает обращение по элементам

mutable_list = [10, 'apple', 'banana', False]
print(mutable_list)
mutable_list[2] = 'chery'
print(mutable_list)


