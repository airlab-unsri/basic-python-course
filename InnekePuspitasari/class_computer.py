class computer:

    def __init__(self):
        self.__maxprice = 900
    def sell (self):
        print("selling Price: {}".format(self.__maxprice)) 
    def setMaxprice(self, price):
        self.__maxprice = price

c = computer()
c.sell()

#change the price
c.__maxprice=1000
c.sell()

c.setMaxprice(1000)
c.sell()