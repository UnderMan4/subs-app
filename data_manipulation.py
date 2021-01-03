import json
from subscription import subscription
import expense


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
        # for i in range(1, len(list)):
        #     data['data']['subscriptions'][i] = list[i - 1]

        # data['data']['subscriptions'] = {i: list[i-1] for i in range(1, len(list))}
        # print(data)
        temp = zip(range(1, len(list)+1), list)
        data['data']['subscriptions'] = dict(temp)
        del temp
        data_json = json.dumps(data, indent=2)
        # print(data_json)
        with open('data.json', 'w') as f:
            f.write(json.dumps(data, indent=2))
