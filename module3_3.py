def print_params(*args, **kwargs):
    print(args, kwargs)


print_params(1, 2, 3, 'gfddf', (5464, 'dtert', 785))
print_params(None, True, 35.8)
print_params()

values_list = [15, True, 'num']
values_dict = {'a': 18, 'b': 'run', 'c': False}

print_params(*values_list, **values_dict)

values_list_2 = ['buble', 25.4]

print_params(*values_list_2, 45)
