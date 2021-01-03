import json
from subscription import subscription
from expense import expense


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
        temp = zip(range(1, len(list)+1), list)
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
        temp = zip(range(1, len(list)+1), list)
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
        temp = zip(range(1, len(list)+1), list)
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
        temp = zip(range(1, len(list)+1), list)
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
        temp = zip(range(1, len(list)+1), list)
        data['data']['lists']['places'] = dict(temp)
        del temp

    
        
        
    # data_json = json.dumps(data, indent=2)
    # print(data_json)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
