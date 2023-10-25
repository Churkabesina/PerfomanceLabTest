import json


def recursion(tests_file, values_file):
    for some_dict in tests_file:

        walking(tests_file[some_dict], values_file)

    with open('report.json', 'w', encoding='UTF-8') as file_out:
        json.dump(tests_file, file_out)
    return None


def walking(tests_file, values_file):

    for file_dict in tests_file:

        file_dict['value'] = ''.join([x.get('value') for x in values_file if file_dict['id'] == x['id']])
        if 'values' in file_dict:
            walking(file_dict['values'], values_file)
    return None


with open('tests.json') as f_test:
    tests: dict = json.load(f_test)

    with open('values.json') as f_values:
        values: dict = json.load(f_values)
        recursion(tests, values['values'])