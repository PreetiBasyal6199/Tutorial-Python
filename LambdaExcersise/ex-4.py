#Write a Python program to sort a list of dictionaries using Lambda

dict_1 = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
        ]

print(sorted(dict_1, key = lambda x: x['model']))

#[{'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#  {'make': 'Nokia', 'model': 216, 'color': 'Black'}]