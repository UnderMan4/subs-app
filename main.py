import json
import os.path
from os import path

# appdata = os.getenv('APPDATA') + '\Subs-App'
# print(appdata)
os.chdir(os.getenv('APPDATA'))
# print(os.getcwd())
if not path.exists('Subs-App'):
    os.mkdir('Subs-App')
os.chdir('Subs-App')
print(os.getcwd())





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
