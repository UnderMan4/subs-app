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
                            labeldistance=.7, center=([10, 10]))
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
                            labeldistance=.7)
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
                            labeldistance=.7)
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
                               labeldistance=.7, center=([10, 10]))
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
                               labeldistance=.7)
    by_platform_pie_active.legend(platforms_list, loc=[-.60, 0])
    by_platform_pie_active.set_title('by platform (active)')
    # by_platform_pie_active.tight_layout()
    ##################################################################

    # fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    plt.show()


def plot_period_stats_expenses(start, end, place=None, category=None):
    if not ((bool(re.match('\d\d\d\d', start)) and bool(re.match('\d\d\d\d', end))) or
            (bool(re.match('\d\d\.\d\d\d\d', start)) and bool(re.match('\d\d\.\d\d\d\d', end)))):
        raise ValueError('start and stop argument must both match same pattern '
                         '\'\d\d\d\d\' or \'\d\d\.\d\d\d\d\'')
    if place not in dm.get_data_from_file('plc') and place is not None:
        raise ValueError('place argument must be in places list or equals None')
    if category not in dm.get_data_from_file('cat') and category is not None:
        raise ValueError('category argument must be in categories list or equals None')

    fig = plt.figure(figsize=(17, 8))
    dates_f = []
    dates = []
    values = []

    if bool(re.match('\d\d\d\d', start)):
        if (int(start) > int(end)):
            raise ValueError('start year must be earlier than end year ')
        for i in range(int(start), int(end)):
            dates.append(str(i))
        for elem in dates:
            dates_f.append(elem + '     ')

        if place is None and category is None:
            fig.suptitle(f'Expenses yearly from {start} to {end}', fontsize=20)
        elif place is None:
            fig.suptitle(f'Expenses yearly from {start} to {end} for {category} category', fontsize=20)
        elif category is None:
            fig.suptitle(f'Expenses yearly from {start} to {end} in {place}', fontsize=20)
        else:
            fig.suptitle(f'Expenses yearly from {start} to {end} for {category} category in {place}', fontsize=20)

        # for i, elem in enumerate(dates):
        #     values.append(float(get_expenses(dates[i], place, category)))



    if bool(re.match('\d\d\.\d\d\d\d', start)):
        start_d = re.split('\.', start)
        end_d = re.split('\.', end)
        # print(start_d)
        # print(end_d)
        if int(start_d[1]) > int(end_d[1]):
            raise ValueError('start month must be earlier than end month ')
        elif int(start_d[1]) == int(end_d[1]) and int(start_d[0]) > int(end_d[0]):
            raise ValueError('start month must be earlier than end month ')

        month = int(start_d[0])
        year = int(start_d[1])
        # print(start_d)
        # print(end_d)
        while month != int(end_d[0]) or year != int(end_d[1]):
            dates.append('{:02d}.{:04d}'.format(month, year))
            # print('{:02d}.{:04d}'.format(month, year))
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        for elem in dates:
            dates_f.append(elem + '          ')
            # print(str(month) + '  ' + str(year))
        if place is None and category is None:
            fig.suptitle(f'Expenses monthly from {start} to {end}', fontsize=20)
        elif place is None:
            fig.suptitle(f'Expenses monthly from {start} to {end} for {category} category', fontsize=20)
        elif category is None:
            fig.suptitle(f'Expenses monthly from {start} to {end} in {place}', fontsize=20)
        else:
            fig.suptitle(f'Expenses monthly from {start} to {end} for {category} category in {place}', fontsize=20)

    for i, elem in enumerate(dates):
        values.append(float(get_expenses(dates[i], place, category)))


    # print(dates)
    # print(values)
    plot = fig.add_subplot(111)
    plot.bar(dates, values, zorder=3)
    plt.minorticks_on()
    for i, dat in enumerate(dates):
        # plot.text(dat, 100, 'qwer', zorder=4)
        # plot.annotate('{:.2f}'.format(values[i]) + '\n\n\n', (str(dat), 0), zorder=4, ha='center')
        # plot.annotate('{:.2f}'.format(values[i]), (str(dat), float(values[i])), zorder=4,
        #               ha='center', va='bottom', rotation='vertical',
        #               textcoords='offset points', xytext=(0, 50))
        plot.annotate('{:.2f}'.format(values[i]), (str(dat), float(values[i])), zorder=2,
                      ha='center', va='center', rotation='horizontal',
                      textcoords='offset points', xytext=(0, 7), backgroundcolor='w',
                      color='#1F77B4', weight='bold', fontsize=8)
    plot.grid(which='major', axis='y', zorder=0)
    plot.grid(which='minor', axis='y', alpha=.3, zorder=0)
    plot.set_xticks(dates)
    plot.set_xticklabels(dates_f, rotation=45, ha='center', va='bottom', position=(10, -.08))

    plt.show()

def plot_stats_expenses(start, end):

    if not ((bool(re.match('\d\d\d\d', start)) and bool(re.match('\d\d\d\d', end))) or
            (bool(re.match('\d\d\.\d\d\d\d', start)) and bool(re.match('\d\d\.\d\d\d\d', end))) or
            (bool(re.match('\d\d\.\d\d\.\d\d\d\d', start)) and bool(re.match('\d\d\.\d\d\.\d\d\d\d', end)))):
        raise ValueError('start and stop argument must both match same pattern '
                         '\'\d\d\d\d\', \'\d\d\.\d\d\d\d\' or \'\d\d\.\d\d\.\d\d\d\d\'')

    today = date.today().strftime('%d.%m.%Y')
    # print(today)
    list = dm.get_data_from_file('exp')
    # print(list)
    fig = plt.figure(figsize=(13, 8))
    fig.suptitle(f'Expenses from {start} to {end}', fontsize=23)
    # fig.tight_layout()
    by_category_pie_all = fig.add_subplot(221)
    by_place_pie_all = fig.add_subplot(222)
    # active_inactive_pie = fig.add_subplot(222)
    by_category_pie_sum = fig.add_subplot(223)
    by_place_pie_sum = fig.add_subplot(224)

    explode_low = .3
    explode_high = .04

    list_period = []
    if (bool(re.match('\d\d\d\d', start)) and bool(re.match('\d\d\d\d', end))):
        # print('year')
        for elem in list:
            d = re.split('\.', elem['date'])
            if int(d[2]) >= int(start) and int(d[2]) <= int(end):
                list_period.append(elem)
    if (bool(re.match('\d\d\.\d\d\d\d', start)) and bool(re.match('\d\d\.\d\d\d\d', end))):
        # print('month')
        start_f = re.split('\.', start)
        end_f = re.split('\.', end)
        for elem in list:
            d = re.split('\.', elem['date'])
            if int(d[-1]) >= int(start_f[-1]) and int(d[-1]) <= int(end_f[-1]):
                # print(d[2], start_f[1], end_f[1] )
                # print(d[1], start_f[0], end_f[0] )
                if int(d[-1]) == int(start_f[-1]) and int(d[-2]) >= int(start_f[-2]):
                    list_period.append(elem)
                elif int(d[-1]) == int(end_f[-1]) and int(d[-2]) <= int(end_f[-2]):
                    list_period.append(elem)
                elif int(d[-1]) != int(start_f[-1]) and int(d[-1]) != int(end_f[-1]):
                    list_period.append(elem)
    if (bool(re.match('\d\d\.\d\d\.\d\d\d\d', start)) and bool(re.match('\d\d\.\d\d\.\d\d\d\d', end))):
        # print('day')
        start_f = re.split('\.', start)
        end_f = re.split('\.', end)
        for elem in list:
            d = re.split('\.', elem['date'])
            if int(d[-1]) >= int(start_f[-1]) and int(d[-1]) <= int(end_f[-1]):
                if int(d[-1]) == int(start_f[-1]) and int(d[-2]) >= int(start_f[-2]):
                    if int(d[-2]) == int(start_f[-2]) and int(d[-3]) >= int(start_f[-3]):
                        list_period.append(elem)
                    elif int(d[-2]) > int(start_f[-2]):
                        list_period.append(elem)
                if int(d[-1]) == int(end_f[-1]) and int(d[-2]) <= int(end_f[-2]):
                    if int(d[-2]) == int(end_f[-2]) and int(d[-3]) <= int(end_f[-3]):
                        list_period.append(elem)
                    if int(d[-2]) < int(end_f[-2]):
                        list_period.append(elem)
                if int(d[-1]) != int(start_f[-1]) and int(d[-1]) != int(end_f[-1]):
                    list_period.append(elem)







    # for elem in list_period:
        # print(elem['date'])


        # print(d)
        # if bool(re.match(f'{}'))

    #######################################################
    by_category_amount = []
    list = list_period
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
            # print(val / sum(by_category_amount))
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    # print(explode)
    # print(categories_list)
    # print(by_category_amount_copy)
    wedges, labels = by_category_pie_all.pie(by_category_amount_copy, labels=by_category_amount_copy,
                                             shadow=False, textprops={'alpha': 1}, explode=explode,
                                             labeldistance=.7, center=([10, 10]))
    for label in labels:
        label.set_horizontalalignment('center')
    # by_category_pie_all.
    # by_category_pie_all.margins(200, 200)
    by_category_pie_all.legend(categories_list, loc=[-.45, 0])
    by_category_pie_all.set_title('by category (number)')
    # by_category_pie_all.tight_layout()
    #########################################################

    by_place_amount = []

    for elem in dm.get_data_from_file('plc'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['place'])
            if sub_elem['place'] == elem:
                amount += 1
        # print(amount)
        by_place_amount.append(amount)
    # print(by_place_amount)
    by_place_amount_copy = []
    places_list = []
    explode = []
    for i, val in enumerate(by_place_amount):
        if by_place_amount[i] != 0:
            by_place_amount_copy.append(by_place_amount[i])
            places_list.append(dm.get_data_from_file('plc')[i])
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    # print(places_list)
    # print(by_place_amount_copy)
    wedges, labels = by_place_pie_all.pie(by_place_amount_copy, labels=by_place_amount_copy,
                                          shadow=False, textprops={'alpha': 1}, explode=explode,
                                          labeldistance=.7)
    for label in labels:
        label.set_horizontalalignment('center')
    by_place_pie_all.legend(places_list, loc=[-.60, 0])
    by_place_pie_all.set_title('by place (number)')
    # by_place_pie_all.tight_layout()
    ##################################################################

    #######################################################
    by_category_amount = []
    list = list_period
    for elem in dm.get_data_from_file('cat'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['category'])
            if sub_elem['category'] == elem:
                amount += sub_elem['amount']
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
            # print(val / sum(by_category_amount))
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    # print(explode)
    # print(categories_list)
    # print(by_category_amount_copy)
    by_category_amount_copy_label = []
    for elem in by_category_amount_copy:
        by_category_amount_copy_label.append('{:.2f} zł'.format(elem))
    wedges, labels = by_category_pie_sum.pie(by_category_amount_copy, labels=by_category_amount_copy_label,
                                             shadow=False, textprops={'alpha': 1}, explode=explode,
                                             labeldistance=.7, center=([10, 10]))
    for label in labels:
        label.set_horizontalalignment('center')
    # by_category_pie_all.
    # by_category_pie_all.margins(200, 200)
    by_category_pie_sum.legend(categories_list, loc=[-.45, 0])
    by_category_pie_sum.set_title('by category (amount)')
    # by_category_pie_all.tight_layout()
    #########################################################

    by_place_amount = []

    for elem in dm.get_data_from_file('plc'):
        amount = 0
        # print(type(elem))
        for sub_elem in list:
            # print(sub_elem['place'])
            if sub_elem['place'] == elem:
                amount += sub_elem['amount']
        # print(amount)
        by_place_amount.append(amount)
    # print(by_place_amount)
    by_place_amount_copy = []
    places_list = []
    explode = []
    for i, val in enumerate(by_place_amount):
        if by_place_amount[i] != 0:
            by_place_amount_copy.append(by_place_amount[i])
            places_list.append(dm.get_data_from_file('plc')[i])
            if val / sum(by_category_amount) > 0.05:
                explode.append(explode_high)
            else:
                explode.append(explode_low)
    # print(places_list)
    # print(by_place_amount_copy)
    by_place_amount_copy_label = []
    for elem in by_place_amount_copy:
        by_place_amount_copy_label.append('{:.2f} zł'.format(elem))
    wedges, labels = by_place_pie_sum.pie(by_place_amount_copy, labels=by_place_amount_copy_label,
                                          shadow=False, textprops={'alpha': 1}, explode=explode,
                                          labeldistance=.7)
    for label in labels:
        label.set_horizontalalignment('center')
    by_place_pie_sum.legend(places_list, loc=[-.60, 0])
    by_place_pie_sum.set_title('by place (amount)')
    # by_place_pie_all.tight_layout()
    ##################################################################

















    # active_inactive_label = ['active', 'inactive']
    # explode = [.04, .04]
    # active = 0
    # inactive = 0
    # for elem in dm.get_data_from_file('sub'):
    #     # print(elem['active'])
    #     if elem['active'] is True:
    #         active += 1
    #         print(True)
    #     else:
    #         inactive += 1
    #         print(False)
    # active_inactive_amount = [active, inactive]
    #
    # active_inactive_pie.pie(active_inactive_amount, labels=active_inactive_amount,
    #                         shadow=False, textprops={'alpha': 1}, explode=explode,
    #                         labeldistance=.7)
    # active_inactive_pie.legend(active_inactive_label, loc=[-.45, 0])
    # active_inactive_pie.set_title('active / inactive')

    #######################################################
    # by_category_amount = []
    #
    # for elem in dm.get_data_from_file('cat'):
    #     amount = 0
    #     # print(type(elem))
    #     for sub_elem in list:
    #         # print(sub_elem['category'])
    #         if sub_elem['category'] == elem and sub_elem['active'] == True:
    #             amount += 1
    #     # print(amount)
    #     by_category_amount.append(amount)
    # # print(by_category_amount)
    # by_category_amount_copy = []
    # categories_list = []
    # explode = []
    # for i, val in enumerate(by_category_amount):
    #     if by_category_amount[i] != 0:
    #         by_category_amount_copy.append(by_category_amount[i])
    #         categories_list.append(dm.get_data_from_file('cat')[i])
    #         print(val / sum(by_category_amount))
    #         if val / sum(by_category_amount) > 0.05:
    #             explode.append(explode_high)
    #         else:
    #             explode.append(explode_low)
    # print(explode)
    # print(categories_list)
    # print(by_category_amount_copy)
    # by_category_pie_active.pie(by_category_amount_copy, labels=by_category_amount_copy,
    #                            shadow=False, textprops={'alpha': 1}, explode=explode,
    #                            labeldistance=.7, center=([10, 10]))
    # # by_category_pie_active.
    # # by_category_pie_active.margins(200, 200)
    # by_category_pie_active.legend(categories_list, loc=[-.45, 0])
    # by_category_pie_active.set_title('by category (active)')
    # # by_category_pie_active.tight_layout()
    #########################################################
    #
    # by_platform_amount = []
    #
    # for elem in dm.get_data_from_file('plt'):
    #     amount = 0
    #     # print(type(elem))
    #     for sub_elem in list:
    #         # print(sub_elem['platform'])
    #         if sub_elem['platform'] == elem and sub_elem['active'] == True:
    #             amount += 1
    #     # print(amount)
    #     by_platform_amount.append(amount)
    # # print(by_platform_amount)
    # by_platform_amount_copy = []
    # platforms_list = []
    # explode = []
    # for i, val in enumerate(by_platform_amount):
    #     if by_platform_amount[i] != 0:
    #         by_platform_amount_copy.append(by_platform_amount[i])
    #         platforms_list.append(dm.get_data_from_file('plt')[i])
    #         if val / sum(by_category_amount) > 0.05:
    #             explode.append(explode_high)
    #         else:
    #             explode.append(explode_low)
    # print(platforms_list)
    # print(by_platform_amount_copy)
    # by_platform_pie_active.pie(by_platform_amount_copy, labels=by_platform_amount_copy,
    #                            shadow=False, textprops={'alpha': 1}, explode=explode,
    #                            labeldistance=.7)
    # by_platform_pie_active.legend(platforms_list, loc=[-.60, 0])
    # by_platform_pie_active.set_title('by platform (active)')
    # # by_platform_pie_active.tight_layout()
    ##################################################################

    # fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    plt.show()