class People:

    def __init__(self, name):
        self.name = name

    def talk(self):
        return "Hi, my name is {}".format(self.name)


class Student(People):

    def learn(self):
        return "I get it!"


class Instructor(People):

    def teach(self):
        return "An object is an instance of a class"


nadia = Instructor("Nadia")
print(nadia.talk())
chris = Student("Chris")
print(chris.talk())
print(nadia.teach())
print(chris.learn())
