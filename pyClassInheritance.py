class Familymembers:
    """This is class for family members within Ekavala Village"""
    def __init__(self, name, status, age, family, gender):

        self.fullname = name
        self.merital = status
        self.age = age
        self.family = family
        self.gender = gender

    def intro(self):
        print(f"My name is {self.fullname}. I'm {self.age} yrs, {self.merital} and happy. I'm a {self.gender} from {self.family} family")

class Musungus(Familymembers):
    def __init__(self, name, status, age, family, gender, course):
        super().__init__(name, status, age, family,gender)
        self.course = course
#   def intro(self):
#        print("My name is" + self.fullname + "from" + self.family + "family")

# special magic method "dander '__str__'
    def __str__(self):
        return f"My name is {self.fullname} from {self.family} family"

fifthborn = Musungus("Esau Otenyo","married","47","Musungus","male","Agriculture")
fifthborn.fullname
print("\n***")
fifthborn.intro()
print("***\n")

print(f"{fifthborn.gender}\n")
print(f"{fifthborn.course}\n")

firstborn = Familymembers("John Anyangu","married",67,"Musungus","Man")
print("***\n")
# print(firstborn.intro())
print("***\n")
secondborn = Familymembers("Phylis","married",65,"Musungus","woman")
print(secondborn.intro())

# isinstance checking
print("\nisinstance\n")
print(isinstance(fifthborn, Musungus))
print(isinstance(firstborn, Musungus))
print(isinstance(firstborn, Familymembers))

# issubclass checking
print("\nissubclass\n")
print(issubclass(Musungus, Familymembers))

# Checking dander special method output
print("\n***dander special method __str__\n")
print(fifthborn.__str__())
print("\n***dander special method ends***\n")

print(fifthborn)

# Printing object of related to method "def intro(self)" which has not been initialized with "special magic methed" - dander.
print(firstborn)
