class BilanganKompleks:
    def __init__(self, riil, imajiner):
        self.riil = riil
        self.imajiner = imajiner

    def __add__(self, bil_kompleks_lain):
        bil_kompleks_hasil = BilanganKompleks(0, 0)
        bil_kompleks_hasil.riil = self.riil + bil_kompleks_lain.riil
        bil_kompleks_hasil.imajiner = self.imajiner + bil_kompleks_lain.imajiner
        return bil_kompleks_hasil

    def print(self):
        print(self.riil, '+', str(self.imajiner) + 'i')


bil_kompleks_1 = BilanganKompleks(10, 5)
bil_kompleks_2 = BilanganKompleks(2, 4)
bil_kompleks_3 = bil_kompleks_1 + bil_kompleks_2
bil_kompleks_3.print()
