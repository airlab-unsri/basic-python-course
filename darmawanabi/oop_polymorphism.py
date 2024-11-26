class Parrot:

    def __init__(self):
        print("Parrot can fly")
    
class Penguin:
    
    def fly(self):
        print("Penguin can't fly")
    
def flyingTest(bird):
    bird.fly()

blu = Parrot()
# peggy = Penguin()

flyingTest(blu)
# flyingTest(peggy)

# masih error
