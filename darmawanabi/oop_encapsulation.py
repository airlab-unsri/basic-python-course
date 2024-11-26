class computer:

    def __init__(self):
        self.maxPrice = 750

    def sell(self):
        print("Harga Jual : {}".format(self.maxPrice))

    def setMaxPrice(self, price):
        self.maxPrice = price

comp = computer()
comp.sell()

comp.maxPrice = 1000
comp.sell()

# gunakan fungsi setter 
comp.setMaxPrice(2000)
comp.sell()
