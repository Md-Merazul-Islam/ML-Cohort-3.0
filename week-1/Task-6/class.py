class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def summation(self):
        return self.length + self.width

    def difference(self):
        print(self.length - self.width)


ans = Rectangle(20, 30)
print(ans.area())

print(ans.summation())

ans.difference()
