import json
import os.path
from os import path
from subscription import subscription as sub
from expense import expense as exp
from urllib.request import urlopen
from gui import gui
import stats
import random
import data_manipulation as dm

# appdata = os.getenv('APPDATA') + '\Subs-App'
# print(appdata)
os.chdir(os.getenv('APPDATA'))
# print(os.getcwd())
if not path.exists('Subs-App'):
    os.mkdir('Subs-App')
os.chdir('Subs-App')


if not os.path.isfile('data.json'):
    with urlopen("https://raw.githubusercontent.com/UnderMan4/subs-app/main/empty_data.json") as nf:
        file = json.loads(nf.read())
        # print(str(nf.read()))
        with open('data.json', 'w') as lf:
            # print(type(nf.read()))
            # lf.write(str(nf.read()))
            # print(json.dumps(file, indent=2))
            lf.write(json.dumps(file, indent=2))
            del file
            # for line in nf.read():
            #     print(line)
            #       lf.write(line)

# f = urlopen('https://raw.githubusercontent.com/UnderMan4/subs-app/main/empty_data.json')
# print(f.read())
# print(type(f))




# if os.path.isfile('data.json'):
#     with open('data.json'):
#         file = json.load('data.json')
# else:
#     with urlopen("https://raw.githubusercontent.com/UnderMan4/subs-app/main/empty_data.json") as f:
#         file = f.read()
# # print(os.getcwd())
# # print(file)
# data = json.loads(file)
# print(json.dumps(data, indent=2))

# subscriptions = []
#
# subscriptions.append(sub('Netflix', 'Monday', 59.99, 'Netflix.com'))
# item = sub('Google 100 GB', '15', 8.99, 'Google.com')
# item2 = exp('party shopping', '15.06.2020', 53.65, 'Lidl')
# item3 = exp('costam', '17.11.2020', 35.82)
# print(dm.get_data_from_file('sub'))
# dm.add_element('sub', item)
# dm.add_element('exp', item2)
# dm.add_element('exp', item3)
# dm.add_element('cat', 'movies')
# dm.add_element('cat', 'food')
# dm.add_element('plc', 'Żabka')
# dm.add_element('plc', 'Biedronka')
# dm.add_element('plc', 'Lidl')
# dm.add_element('plt', 'Netflix')
# dm.add_element('plt', 'Google')
# dm.add_element('plt', 'Amazon')
# dm.add_element('plt', 'Spotify')
# # with open('subscriptions.json', 'w') as sub_file:
# #     json.dumps(subscriptions)
#     # for sub in subscriptions:
#     #     json.dump(sub.__dict__, sub_file, separators=(', \n', ': '))
#
# x = list([])
# x.lappend(sub('Netflix', 'Monday', 59.99, 'Netflix.com'))
# x.lappend(sub('Google 100 GB', '15', 8.99, 'Google.com'))
# with open('subscription.json', 'w') as file:
#     json.dump(x.__dict__, file, indent=4)

# class subscribtion():
#     def __init__(self, platform, category, name, date, price):
#         # self.number_of_payments = number_of_payments
#         # self.expiration_date = expiration_date
#         self.platform = platform
#         self.category = category
#         self.name = name
#         self.date = date
#         self.price = price
#
#
# s1 = subscribtion('netflix', 'film', 'netflix', 12, 12.8)
#
# with open('subscription.json', 'w') as json_file:
#     json.dump(s1.__dict__, json_file, separators=(', \n', ': '))

# print(stats.get_monthly_subs())
# stats.get_expenses_period('2014')
# print(stats.get_expenses("", place="Lidl"))
# print(dm.search('exp', '2015'))
# stats.plot_stats_subscriptions()
# dm.delete_all('sub')
# dm.delete_all('exp')
# for i in range(500):
#     name = str(i)
#     d = random.randint(1, 28)
#     m = random.randint(1, 12)
#     y = random.randint(2017, 2020)
#     datee = '{:02d}.{:02d}.{:04d}'.format(d, m, y)
#     amount = random.randint(100, 15000)/100
#     place = random.choice(['Zabka', 'Biedronka', 'Lidl', 'Dino', 'Lewiatan'])
#     category = random.choice(['movies', 'food', 'drink', 'alcohol', 'books', 'music'])
#     dm.add_element('exp', exp(name=name, date=datee, amount=amount, place=place, category=category))
#
# for i in range(500):
#     name = str(i)
#     d = random.randint(1, 28)
#     m = random.randint(1, 12)
#     temp = random.randint(1, 2)
#     if temp == 1:
#         datee = '{:02d}'.format(d)
#     if temp == 2:
#         datee = '{:02d}.{:02d}'.format(d, m)
#     amount = random.randint(100, 10000)/100
#     temp = random.randint(1, 2)
#     if temp == 1:
#         active = True
#     if temp == 2:
#         active = False
#     category = random.choice(['movies', 'storage', 'books', 'music'])
#     platform = random.choice(['Netflix', 'Google', 'Amazon', 'Spotify', 'Empik.com'])
#     dm.add_element('sub', sub(name, datee, amount, platform, active, category))

# stats.plot_period_stats_expenses('05.2017', '05.2019', category='books', place='Lidl')
# stats.plot_stats_expenses('2017', '2020')
# dm.delete_element('plc', 'Lidl')

gui()