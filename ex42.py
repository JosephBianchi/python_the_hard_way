class Animal(object)
    pass


# dog is-a animal
class Dog(Animal):
    def __init__(self, name)
    ## dog has-a name
    self.name = name

#cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        # cat has-a names
        self.name = name

# person is a object
class Person(object):
    def __init__(self, name):
        ##person has-a name
    self.name = name
    self.pet = none

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary

class Fish(object)
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary,pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
