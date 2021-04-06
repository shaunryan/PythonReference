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

class BigDog(Dog, LoudBark):
    pass

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
