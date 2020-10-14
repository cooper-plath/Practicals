from Prac_08.taxi import Taxi

class SilverTaxi(Taxi):
    flagpole = 4
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{}, plus flagfall of ${}".format(super().__str__(), self.fanciness)