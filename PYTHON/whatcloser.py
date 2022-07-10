def startx(x):
    def increment(y):
        return x+y
    return increment


closer1 = startx(1)
closer2 = startx(2)
print("c1 :", closer1(3))
print("c2 :", closer2(4))
