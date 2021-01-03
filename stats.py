import json
import data_manipulation as dm
import re


def get_monthly_subs():
    list = dm.get_data_from_file('sub')
    sum = .0
    for elem in list:
        # print(elem)
        # print(re.match('^\d\d$', elem['date']))
        # print(bool(re.match('^\d\d$', elem['date'])))
        if elem['active'] == True:
            if bool(re.match('^\d\d$', elem['date'])):
                sum += (elem['amount'])
            elif bool(re.match('^\d\d\.\d\d$', elem['date'])):
                sum += (elem['amount'] / 12)
            elif bool(re.match('^Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday$', elem['date'])):
                sum += (elem['amount'] * 4)
    # print('{:.2f}'.format(sum))
    return '{:.2f}'.format(sum)


def get_yearly_subs():
    list = dm.get_data_from_file('sub')
    sum = .0
    for elem in list:
        # print(elem)
        # print(re.match('^\d\d$', elem['date']))
        # print(bool(re.match('^\d\d$', elem['date'])))
        if elem['active'] == True:
            if bool(re.match('^\d\d$', elem['date'])):
                sum += (elem['amount'] * 12)
            elif bool(re.match('^\d\d\.\d\d$', elem['date'])):
                sum += elem['amount']
            elif bool(re.match('^Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday$', elem['date'])):
                sum += (elem['amount'] * 52)
    # print('{:.2f}'.format(sum))
    return '{:.2f}'.format(sum)


def get_expenses(period, place=None, category=None):
    # valid = {'month', 'year'}
    # if period not in valid:
    #     raise ValueError('period argument must be one of %r.' % valid)
    # del valid

    if not bool(re.match('^\d\d\d\d$', period)) | bool(re.match('^\d\d\.\d\d\d\d$', period)):
        raise ValueError('period argument must match one of \'^\d\d\d\d$\' or \'^\d\d.\d\d\d\d$\' pattern')
    if place not in dm.get_data_from_file('plc') and place is not None:
        raise ValueError('place argument must be in places list or equals None')
    if category not in dm.get_data_from_file('cat') and category is not None:
        raise ValueError('category argument must be in categories list or equals None')

    list = dm.get_data_from_file('exp')
    sum = .0

    if place is None and category is None:
        if bool(re.match('^\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.\d\d\.{period}$', elem['date'])):
                    sum += elem['amount']

        if bool(re.match('^\d\d\.\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\.\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d.\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.{period}$', elem['date'])):
                    sum += elem['amount']
    elif place is None:
        if bool(re.match('^\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.\d\d\.{period}$', elem['date'])) and elem['category'] == category:
                    sum += elem['amount']

        if bool(re.match('^\d\d\.\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\.\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d.\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.{period}$', elem['date'])) and elem['category'] == category:
                    sum += elem['amount']
    elif category is None:
        if bool(re.match('^\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.\d\d\.{period}$', elem['date'])) and elem['place'] == place:
                    sum += elem['amount']

        if bool(re.match('^\d\d\.\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\.\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d.\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.{period}$', elem['date'])) and elem['place'] == place:
                    sum += elem['amount']
    else:
        if bool(re.match('^\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.\d\d\.{period}$', elem['date'])) and elem['place'] == place and elem['category'] == category:
                    sum += elem['amount']

        if bool(re.match('^\d\d\.\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\.\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d.\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.{period}$', elem['date'])) and elem['place'] == place and elem['category'] == category:
                    sum += elem['amount']

    # print('{:.2f}'.format(sum))
    return '{:.2f}'.format(sum)
