from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def talk(self)->str:
        pass

class Dog(Animal):
    def talk(self)->str:
        return "wooof"

class LoudBark(Animal):
    def bark(self)->str:
        return self.talk().upper()

    def talk(self)->str:
        return "wooooooof"

class BigDog(Dog, LoudBark):
    def print_base(self):
        for base in self.__class__.__bases__:
            print(base.__name__)


dog = Dog()
msg = f"Dog talks: {dog.talk()}"
print(msg)

bigDog:Dog = BigDog()
msg = f"BigDog talks: {bigDog.talk()}"
print(msg)
msg = f"BigDog barks: {bigDog.bark()}"
print(msg)

msg = f"bigDog type is: {type(bigDog)}"
print(msg)

msg = f"bigDog is an instance of BigDog: {isinstance(bigDog, BigDog)}"
print(msg)
msg = f"bigDog is also a Dog: {isinstance(bigDog, Dog)}"
print(msg)
msg = f"bigDog has a LoudBark: {isinstance(bigDog, LoudBark)}"
print(msg)

bigDog.print_base()