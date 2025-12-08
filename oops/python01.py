print("Please enter your name:")
name = input("Your name: ")
techStack = input("Your tech stack: ")
age = input("Your age: ")

class Cv:
  def __init__ (self, name, techStack):
    self.name = name
    self.techStack = techStack
  def bio(self):
    return f"The name of a developer is {self.name} & the TECH stack is {self.techStack}"  
  
class Selected(Cv): 
  def __init__ (self, name, techStack,age):
    
    
    super().__init__(name, techStack)
    self.age = age
    
    if(int(age) < 18):
      print("You are not eligible")
      return

candidate = Selected(name, techStack, age)
print(candidate.bio())


# person = Cv(name, techStack, age)
# print(person.bio())