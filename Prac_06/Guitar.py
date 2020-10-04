
CURRENT_YEAR = 2020
VINTAGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE


# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.40
#
# Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
# print(Gibson.is_vintage())