class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, I am {} and I am {} years old, my gender is {}".format(self.name, self.age, self.gender))

# create an instance of the Person class
p = Person("Alvin", 19, "Male")

# call the introduce method to display the person's information
p.introduce()