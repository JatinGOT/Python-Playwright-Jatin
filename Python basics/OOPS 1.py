# classes are user defined blueprint or prototype
#sum, mul, add, constant

#methods, class variable , instance variable, constructor etc



# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should be __init__
    

class Calculator :
    num = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def getData(self):
            print("I am now executing as method in class ")


    def summation(self):
        return self.a + self.b

# obj = Calculator()
# obj.getData()
# print(obj.num)


obj2 = Calculator(5,10)
print(obj2.summation())