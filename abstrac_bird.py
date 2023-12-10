from abc import ABCMeta,abstractclassmethod
class animal(metaclass=ABCMeta):
    def __init__(self ,name ,age , color) :
        self.name =name
        self.age =age
        self.color = color

    @abstractclassmethod
    def sound(self):
        pass
class bird(animal):
    def sound(self):
        return "zzzzz"
    def move(self):
        return "fly"
    def info(self):
        print(f"name is :{self.name}\nage is :{self.age}\ncolor:{self.color}")
var =bird("niro",2 ,"bleu" )
var.info()
print(var.sound())
print(var.move())