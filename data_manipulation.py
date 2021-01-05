import json
from subscription import subscription
from expense import expense
import re


def get_data_from_file(list_name):
    with open('data.json') as f:
        data = json.load(f)
        # print(data)
    valid = {'sub', 'exp', 'cat', 'plt', 'plc'}
    if list_name not in valid:
        raise ValueError('list_name argument must be one of %r.' % valid)
    del valid

    if list_name == 'sub':
        list = []
        for elem in data['data']['subscriptions']:
            list.append(data['data']['subscriptions'][elem])
        return list

    if list_name == 'exp':
        list = []
        for elem in data['data']['expenses']:
            list.append(data['data']['expenses'][elem])
        return list

    if list_name == 'cat':
        list = []
        for elem in data['data']['lists']['categories']:
            list.append(data['data']['lists']['categories'][elem])
        return list

    if list_name == 'plt':
        list = []
        for elem in data['data']['lists']['platforms']:
            list.append(data['data']['lists']['platforms'][elem])
        return list

    if list_name == 'plc':
        list = []
        for elem in data['data']['lists']['places']:
            list.append(data['data']['lists']['places'][elem])
        return list


def add_element(list_name, element):
    with open('data.json') as f:
        data = json.load(f)
        # print(data)

    valid = {'sub', 'exp', 'cat', 'plt', 'plc'}
    if list_name not in valid:
        raise ValueError('list_name argument must be one of %r.' % valid)
    del valid

    if list_name == 'sub':
        if not isinstance(element, subscription):
            raise ValueError('type of element is {}, but it must be <class \'subscription\'>'.format(type(element)))
        list = get_data_from_file('sub')
        # print(type(element))
        # print(element.__dict__)
        list.append(element.__dict__)
        # print(list)
        # print(len(list))
        # print(data)
        temp = zip(range(1, len(list) + 1), list)
        data['data']['subscriptions'] = dict(temp)
        del temp

    if list_name == 'exp':
        if not isinstance(element, expense):
            raise ValueError('type of element is {}, but it must be <class \'expense\'>'.format(type(element)))
        list = get_data_from_file('exp')
        # print(type(element))
        # print(element.__dict__)
        list.append(element.__dict__)
        # print(list)
        # print(len(list))
        temp = zip(range(1, len(list) + 1), list)
        data['data']['expenses'] = dict(temp)
        del temp

    if list_name == 'cat':
        if not isinstance(element, str):
            raise ValueError('type of element is {}, but it must be <class \'str\'>'.format(type(element)))
        list = get_data_from_file('cat')
        # print(type(element))
        # print(element.__dict__)
        list.append(element)
        # print(list)
        # print(len(list))
        temp = zip(range(1, len(list) + 1), list)
        data['data']['lists']['categories'] = dict(temp)
        del temp

    if list_name == 'plt':
        if not isinstance(element, str):
            raise ValueError('type of element is {}, but it must be <class \'str\'>'.format(type(element)))
        list = get_data_from_file('plt')
        # print(type(element))
        # print(element.__dict__)
        list.append(element)
        # print(list)
        # print(len(list))
        temp = zip(range(1, len(list) + 1), list)
        data['data']['lists']['platforms'] = dict(temp)
        del temp

    if list_name == 'plc':
        if not isinstance(element, str):
            raise ValueError('type of element is {}, but it must be <class \'str\'>'.format(type(element)))
        list = get_data_from_file('plc')
        # print(type(element))
        # print(element.__dict__)
        list.append(element)
        # print(list)
        # print(len(list))
        temp = zip(range(1, len(list) + 1), list)
        data['data']['lists']['places'] = dict(temp)
        del temp

    # data_json = json.dumps(data, indent=2)
    # print(data_json)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=2))


def search(list_name, value):
    list = get_data_from_file(list_name)
    temp = []
    for elem in list:
        # print(type(elem))
        temp_elem = elem.values()
        # print(temp_elem)
        # r = re.compile(f'{value}')
        # if any(r.match(temp_elem)) for item in temp_elem:
        #     temp.append(elem)
        # if bool(re.search(f'{value}', ' ')):
        check = False
        for item in temp_elem:
            # print(str(item))
            # print(type(item))
            # print(item)
            if bool(re.match(f'.*{value}.*', str(item))):
                check = True
        if check is True:
            temp.append(elem)

    return temp

def delete_all(list_name):
    valid = {'sub', 'exp', 'cat', 'plt', 'plc'}
    if list_name not in valid:
        raise ValueError('list_name argument must be one of %r.' % valid)
    del valid
    with open('data.json') as f:
        data = json.load(f)
    if list_name == 'sub':
        data['data']['subscriptions'] = []
    if list_name == 'exp':
        data['data']['expenses'] = []
    if list_name == 'cat':
        data['data']['lists']['categories'] = []
    if list_name == 'plt':
        data['data']['lists']['platforms'] = []
    if list_name == 'plc':
        data['data']['lists']['places'] = []
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=2))




def delete_element(list_name, name):
    valid = {'sub', 'exp', 'cat', 'plt', 'plc'}
    if list_name not in valid:
        raise ValueError('list_name argument must be one of %r.' % valid)
    del valid
    list = get_data_from_file(list_name)
    for i, elem in enumerate(list):
        print(elem['name'])
        if elem['name'] == name:
            del list[i]
            break
    delete_all(list_name)
    for elem in list:
        if list_name == 'sub':
            temp = subscription(elem['name'], elem['date'], elem['amount'],
                                elem['platform'], elem['active'], elem['category'],
                                elem['number_of_payments'], elem['expiration_date'])
        elif list_name == 'exp':
            temp = expense(elem['name'], elem['date'], elem['amount'],
                           elem['place'], elem['category'])
        else:
            temp = name

        add_element(list_name, temp)

