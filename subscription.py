
class subscription ():
    name: str
    date: str
    amount: float
    platform: str
    active: bool
    category: str
    number_of_payments: int
    expiration_date: str

    def __init__(self, name, date, amount, platform, active=True,
                 category=None, number_of_payments=None, expiration_date=None):
        self.name = name
        self.date = date
        self.amount = amount
        self.platform = platform
        self.active = active
        self.category = category
        self.number_of_payments = number_of_payments
        self.expiration_date = expiration_date

