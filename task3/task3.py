import json
from sys import argv

# не указано в каком порядке идут аргументы
tests_path = ''.join([x for x in argv[1:] if 'tests.json' in x])  # tests.json
values_path = ''.join([x for x in argv[1:] if 'values.json' in x])  # values.json


def recursion(tests_file, values_file):
    for some_dict in tests_file:

        walking(tests_file[some_dict], values_file)

    with open('report.json', 'w', encoding='UTF-8') as file_out:
        json.dump(tests_file, file_out)
    return None


def walking(tests_file, values_file):

    for file_dict in tests_file:
        if 'value' in file_dict:
            file_dict['value'] = ''.join([x.get('value') for x in values_file if file_dict['id'] == x['id']])
        if 'values' in file_dict:
            walking(file_dict['values'], values_file)
    return None


with open(tests_path) as f_test:
    tests: dict = json.load(f_test)

    with open(values_path) as f_values:
        values: dict = json.load(f_values)
        recursion(tests, values['values'])
