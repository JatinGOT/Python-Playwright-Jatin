from Inheritance.Parent_Class import Animal


class Child(Animal):
    def __init__(self, gender, color,breed):
        self.gender = gender
        self.color = color
        self.breed = breed

    def showBreed(self):
        print("Breed",self.breed)

dog = Child("Male", "Black", "Labrador")
dog.getData()
dog.showBreed()