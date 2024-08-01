my_dict = {'Irina': 1975, 'Marina': 1962, 'Igor': 1970, 'Dima': 1992}
print(my_dict)

print(my_dict['Marina'])
my_dict['Gena'] = 1950
print(my_dict['Gena'])
my_dict.update({'Sasha': 1989, 'Lena': 1990})
a = my_dict.pop('Igor')
print(a)
print(my_dict)

my_set = {1, 2, 5, 8, True, 'Oleg', 'Vasya', 8, 2, 5}
print(my_set)
my_set.update([15, 'Olga', False])
my_set.discard(1)
print(my_set)