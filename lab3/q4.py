# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab3 Q4

class Quark:
    # Your code here.
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1.0/3.0
    def interact(self, q):
        self.color, q.color = q.color, self.color
        
'''
q1 = Quark("red", "up")
q2 = Quark("blue", "strange")
print("Object initialization")
print(q1.color == "red") # prints True
print(q2.flavor == "strange") # prints True
print("Class attributes")
print(abs(q2.baryon_number -1.0 / 3) <= 1e-5) # prints True
print("Quarks exchange color when interacting")
q1.interact(q2)
print(q1.color == "blue") # prints True
print(q2.color == "red") # prints True
'''