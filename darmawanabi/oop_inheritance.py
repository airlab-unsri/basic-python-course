class Bird:

    def __init__(self):
        print("Bird Initialization")

    def siapaYa(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

class Penguin(Bird):

    def __init__(self):
        # memanggil super func
        super().__init__()
        print("Penguin Initialization")

    def siapaYa(self):
        print("Penguin")

    def run(self):
        print("Run Faster")

ping = Penguin()
ping.siapaYa()
ping.swim()
ping.run()
