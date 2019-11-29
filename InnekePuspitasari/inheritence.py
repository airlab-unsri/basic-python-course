#parent class
class flower:
    def __init__(self):
        print("flower is ready")

    def whoisThis(self):
        print("flower")

    def color(self):
        print("color is red")

#child class
class rose(flower):
    def __init__(self):
        #call super() fungtion 
        super().__init__()
        print("rose is ready")

    def whoisThis(self):
        print("rose") 

    def smell(self):
        print("smell nice")

lil = rose()
lil.whoisThis()
lil.color()
lil.smell()               