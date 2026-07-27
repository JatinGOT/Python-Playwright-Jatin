class Animal:
    def __init__(self, gender, color):
        self.gender = gender
        self.color = color

    def getData(self):
        print("Gender:", self.gender)
        print("Color:", self.color)

obj = Animal("Male", "Black")
obj.getData()