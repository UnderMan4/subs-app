class expense():
    name: str
    date: str
    amount: float
    place: str
    category: str

    def __init__(self, name, date, amount, place=None, category=None):
        self.name = name
        self.date = date
        self.amount = amount
        self.place = place
        self.category = category

