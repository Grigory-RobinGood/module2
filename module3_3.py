def print_params(*args, **kwargs):
    print(args, kwargs)


values_list = [15, True, 'num']
values_dict = {'a': 18, 'b': 'run', 'c': False}

print_params(*values_list, **values_dict)

values_list_2 = ['buble', 25.4]

print_params(*values_list_2, 45)