"""
Task 1. Please write code to create a new list of company names by each of these methods:
    Using for loops
    Using list comprehensions

companies = [
     {'name': 'Apple', 'hq': 'Cupertino, California'},
     {'name': 'Google', 'hq': 'Mountain View, California'},
     {'name': 'Netflix', 'hq': 'Los Gatos, California'}
]
"""

companies_name = []
companies = [
     {'name': 'Apple', 'hq': 'Cupertino, California'},
     {'name': 'Google', 'hq': 'Mountain View, California'},
     {'name': 'Netflix', 'hq': 'Los Gatos, California'}
]

for company in companies:
    companies_name.append(company['name'])

print(companies_name)

new_companies_name = [company['name'] for company in companies]

print(new_companies_name)

"""
Task 2.
companies = ['netflix', 'apple', 'apple', 'google']

1.Order should be the same
2.list(set(companies)) is not allowed 😀
3.Make time complexity better than O(n^2)
"""
companies2 = ['netflix', 'apple', 'apple', 'google']

def remove_duplicates(values_to_filter):
    unique_values = []
    values_to_track = {}

    for value in values_to_filter:
        if value not in values_to_track:
            unique_values.append(value)
            values_to_track[value] = True

    return unique_values

print(remove_duplicates(companies2))

"""
Task 3.
keys = ['name', 'hq', 'no_employees', 'established']
values = ['Apple', 'Cupertino, California', 161000, 1976]
"""
keys = ['name', 'hq', 'no_employees', 'established']
values = ['Apple', 'Cupertino, California', 161000, 1976]
def create_dict(list1, list2):
    return dict(zip(list1, list2))

print(create_dict(keys, values))