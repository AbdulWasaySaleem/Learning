#Exmaple of Encapsulation and Inheritance in Python

print("You wanted to pet/take care of a new dog")

options = input("Do you want to know the breed of the dog? (yes/no): ")


class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.__breed = breed  # private attribute
    
    def get_breed(self, user_choice):
        if user_choice.lower() == "yes":
            return f"The breed of the dog is {self.__breed}"
        else:
            return "You chose not to know the breed of the dog."
          
class dogBio(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    
    def bio(self):
        return (
            f"The dog's name is {self.name}, "
            f"it is {self.age} years old, "
            f"and its breed is {self._Animal__breed}"
        )

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    def bio(self):
        return (
            f"The cat's name is {self.name}, "
            f"it is {self.age} years old, "
            f"and its breed is {self._Animal__breed}"
        )

#my_pet = Animal("Dog", 2, "German Shepherd")  
#print(my_pet.get_breed(options))
#my_dog = dogBio("pups", 1, "labrador")
#print(my_dog.bio())

my_cat = Cat("kitty", 3, "persian")
my_Dog = dogBio("pups", 1, "labrador")
print(my_Dog.bio())
print(my_cat.bio())


#polymorphism example : same methd name in deff classes 