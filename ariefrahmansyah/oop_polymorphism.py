class Parrot:

    def fly(self):
        print("Parrot can fly")


class Penguin:

    def fly(self):
        print("Penguin cannot fly")


# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
