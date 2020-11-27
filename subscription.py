import json

class subscription ():
    def __init__(self, name, date, amount, platform, category='brak', number_of_payments=None, expiration_date=None):
        self.name = name
        self.date = date
        self.amount = amount
        self.platform = platform
        self.category = category
        self.number_of_payments = number_of_payments
        self.expiration_date = expiration_date

    def __del__(self):
        pass

