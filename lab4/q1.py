# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab4 Q1

class Person():
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
class Programmer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.list = []
    def add_skill(self,skill):
        self.list.append(skill)
    def remove_skill(self,skill):
        self.list.remove(skill)
    def has_skill(self,skill):
        return skill in self.list

'''
mike = Person("Mike", 21)
sheila = Programmer("Sheila", 23)
sheila.add_skill("C++")
sheila.add_skill("Python")
sheila.add_skill("Linux")
sheila.remove_skill("Python")
print(mike.name, mike.age) # Mike 21
print(sheila.name, sheila.age) # Sheila 23

print(isinstance(sheila, Person)) # True
print(isinstance(mike, Programmer)) # False
print(sheila.has_skill("C++")) # True
print(sheila.has_skill("Python")) # False
print(sheila.has_skill("Java")) # False
print(sheila.has_skill("Linux")) # True

'''