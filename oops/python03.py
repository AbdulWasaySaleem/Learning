#inheritence, polymorphism, encapsulation 


class Animal: 
  def __init__(self,name,age,breed):
    self.name = name
    self.age = age
    self.__breed = breed 
  
  def sound(self):
    return "Animal sound"

class Dog(Animal):
  def __init__(self,name,age,breed,gender):
    super().__init__(name,age,breed)
    self.gender = gender
  
  def bio(self):
    return f"The dog's name is {self.name}, it is {self.age} years old, and its breed is {self._Animal__breed}" 
  
  

class Cat(Animal):
  def __init__(self,name,age,breed,gender):
    super().__init__(name,age,breed)
    self.gender = gender
  def bio(self):
    return f"The cat's name is {self.name}, it is {self.age} years old, and its breed is {self._Animal__breed}"

my_Dog = Dog("pups",1,"labrador","male")
my_cat = Cat("kitty",3,"persian","female")
print(my_Dog.bio())
print(my_cat.bio())
