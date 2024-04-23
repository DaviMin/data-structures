from Price import Price


class Pizza:
    def __init__(self, name, toppings):
        # pridat druh testa, moznost pridat druh zakladu
        # moznost pridat extra toppings
        self.__name = name
        self.__toppings = toppings
        self.__DOUGHT_PRICE = Price(4, 90)   # to jakoze cena testa je konstanta (plati obecne)

    def get_name(self):
        return self.__name

    def get_price(self):
        result = self.__DOUGHT_PRICE.get.price()
        for t in self.__toppings:
            result += t.get_price().get_price() # to je zanoření do get price

        return result
    def __str__(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ", "
        # odstraneni posledni carky
        return f"""
    
 {self.__name}                      {self.get_price()}€
 ------------------------------------------------------
 {topps}
"""
    
