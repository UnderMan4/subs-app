import json
import re
import matplotlib.pyplot as plt
import data_manipulation as dm
from datetime import date


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
                if bool(re.match(f'^\d\d\.\d\d\.{period}$', elem['date'])) and elem['place'] == place and elem[
                    'category'] == category:
                    sum += elem['amount']

        if bool(re.match('^\d\d\.\d\d\d\d$', period)):
            # if not bool(re.match('^\d\d\.\d\d\d\d$', value)):
            #     raise ValueError('argument value do not match \'^\d\d.\d\d\d\d$\' pattern')
            for elem in list:
                if bool(re.match(f'^\d\d\.{period}$', elem['date'])) and elem['place'] == place and elem[
                    'category'] == category:
                    sum += elem['amount']

    # print('{:.2f}'.format(sum))
    return '{:.2f}'.format(sum)


def plot_stats_subscriptions():
    today = date.today().strftime('%d.%m.%Y')
    # print(today)
    list = dm.get_data_from_file('sub')
    # print(list)
    fig = plt.figure(figsize=(17, 8))
    fig.suptitle(f'Subscriptions {today}', fontsize=23)
    # fig.tight_layout()
    by_category_pie_all = fig.add_subplot(231)
    by_platform_pie_all = fig.add_subplot(232)
    active_inactive_pie = fig.add_subplot(233)
    by_category_pie_active = fig.add_subplot(234)
    by_platform_pie_active = fig.add_subplot(235)

    explode_low = .3
    explode_high = .04

    #######################################################
    by_category_amount = []

    for elem in dm.get_data_from_file('cat'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['category'])
            if sub_elem['category'] == elem:
                amount += 1
        # print(amount)
        by_category_amount.append(amount)
    # print(by_category_amount)
    by_category_amount_copy = []
    categories_list = []
    explode = []
    for i, val in enumerate(by_category_amount):
        if by_category_amount[i] != 0:
            by_category_amount_copy.append(by_category_amount[i])
            categories_list.append(dm.get_data_from_file('cat')[i])
            print(val / sum(by_category_amount))
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    print(explode)
    print(categories_list)
    print(by_category_amount_copy)
    by_category_pie_all.pie(by_category_amount_copy, labels=by_category_amount_copy,
                            shadow=False, textprops={'alpha': 1}, explode=explode,
                            labeldistance=.5, center=([10, 10]))
    # by_category_pie_all.
    # by_category_pie_all.margins(200, 200)
    by_category_pie_all.legend(categories_list, loc=[-.45, 0])
    by_category_pie_all.set_title('by category (all)')
    # by_category_pie_all.tight_layout()
    #########################################################

    by_platform_amount = []

    for elem in dm.get_data_from_file('plt'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['platform'])
            if sub_elem['platform'] == elem:
                amount += 1
        # print(amount)
        by_platform_amount.append(amount)
    # print(by_platform_amount)
    by_platform_amount_copy = []
    platforms_list = []
    explode = []
    for i, val in enumerate(by_platform_amount):
        if by_platform_amount[i] != 0:
            by_platform_amount_copy.append(by_platform_amount[i])
            platforms_list.append(dm.get_data_from_file('plt')[i])
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    print(platforms_list)
    print(by_platform_amount_copy)
    by_platform_pie_all.pie(by_platform_amount_copy, labels=by_platform_amount_copy,
                            shadow=False, textprops={'alpha': 1}, explode=explode,
                            labeldistance=.5)
    by_platform_pie_all.legend(platforms_list, loc=[-.60, 0])
    by_platform_pie_all.set_title('by platform (all)')
    # by_platform_pie_all.tight_layout()
    ##################################################################

    active_inactive_label = ['active', 'inactive']
    explode = [.04, .04]
    active = 0
    inactive = 0
    for elem in dm.get_data_from_file('sub'):
        # print(elem['active'])
        if elem['active'] is True:
            active += 1
            print(True)
        else:
            inactive += 1
            print(False)
    active_inactive_amount = [active, inactive]

    active_inactive_pie.pie(active_inactive_amount, labels=active_inactive_amount,
                            shadow=False, textprops={'alpha': 1}, explode=explode,
                            labeldistance=.5)
    active_inactive_pie.legend(active_inactive_label, loc=[-.45, 0])
    active_inactive_pie.set_title('active / inactive')

    #######################################################
    by_category_amount = []

    for elem in dm.get_data_from_file('cat'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['category'])
            if sub_elem['category'] == elem and sub_elem['active'] == True:
                amount += 1
        # print(amount)
        by_category_amount.append(amount)
    # print(by_category_amount)
    by_category_amount_copy = []
    categories_list = []
    explode = []
    for i, val in enumerate(by_category_amount):
        if by_category_amount[i] != 0:
            by_category_amount_copy.append(by_category_amount[i])
            categories_list.append(dm.get_data_from_file('cat')[i])
            print(val / sum(by_category_amount))
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    print(explode)
    print(categories_list)
    print(by_category_amount_copy)
    by_category_pie_active.pie(by_category_amount_copy, labels=by_category_amount_copy,
                               shadow=False, textprops={'alpha': 1}, explode=explode,
                               labeldistance=.5, center=([10, 10]))
    # by_category_pie_active.
    # by_category_pie_active.margins(200, 200)
    by_category_pie_active.legend(categories_list, loc=[-.45, 0])
    by_category_pie_active.set_title('by category (active)')
    # by_category_pie_active.tight_layout()
    #########################################################

    by_platform_amount = []

    for elem in dm.get_data_from_file('plt'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['platform'])
            if sub_elem['platform'] == elem and sub_elem['active'] == True:
                amount += 1
        # print(amount)
        by_platform_amount.append(amount)
    # print(by_platform_amount)
    by_platform_amount_copy = []
    platforms_list = []
    explode = []
    for i, val in enumerate(by_platform_amount):
        if by_platform_amount[i] != 0:
            by_platform_amount_copy.append(by_platform_amount[i])
            platforms_list.append(dm.get_data_from_file('plt')[i])
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    print(platforms_list)
    print(by_platform_amount_copy)
    by_platform_pie_active.pie(by_platform_amount_copy, labels=by_platform_amount_copy,
                               shadow=False, textprops={'alpha': 1}, explode=explode,
                               labeldistance=.5)
    by_platform_pie_active.legend(platforms_list, loc=[-.60, 0])
    by_platform_pie_active.set_title('by platform (active)')
    # by_platform_pie_active.tight_layout()
    ##################################################################

    # fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    plt.show()
