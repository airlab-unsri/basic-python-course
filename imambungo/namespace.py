a = 1
b = 0
c = 9

def test_1():
    b = 2

    def test_2():
        c = 3
        print("test_2() scope = ", a, b, c)

    print("test_1() scope = ", a, b, c)
    test_2()


print("global scope = ",a,b,c)
test_1()
