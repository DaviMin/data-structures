# je to ted resene bez databaze, abychom videli praci s objektama
class Topping:

    def __init__(self, name, proce):
        self.__name = name    # to aby nam na to nikdo nikde nemohl zmenit
        self.__price = price    # to aby nam na to nikdo nikde nemohl zmenit

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # TODO pridat moznost zdrazeni
