# Abstract Base Classes (abc's) 

# When programming, there is a need to interact with objects in a uniform way.
# Some mechanisms for implementing this are inheritance in OOP languages and
# interfaces. Another need is to customize the implementation of methods for
# different subclasses that share a common parent.

# In inheritance, abstract classes can be defined. Subclasses can inherit from
# abstract classes and will have to implement abstract methods. The same goes
# for interfaces. Interfaces can be defined and subtypes that implement the
# interface must provide implementations for all the methods defined. When used
# with polymorphism features these languages, these address the needs mentioned
# above.

# Another way to address these needs is to allow code external to the class to
# inspect the object and see if it supports certain methods. Developers can
# manually check if a class contains certain properties and methods. For
# example, the dir() function can be used to check if an object has the
# __sizeof__ method and the __len__ property to identify a list object, then
# proceed to interact with the list object.

# A more formal way of doing this in Python is to use the issubclass() and
# isinstance() methods. issubclass(myclass, someclass) returns whether or not
# myclass inherits from a class that ultimately inherits from someclass.
# isinstance() returns whether or not an object was created by a certain class'
# constructor. These methods can be used by a developer to ascertain the class
# and interact with it accordingly.

# Abstract Base Classes (ABCs) are built on top of the standard isinstance() and
# issubclass() methods. ABCs and their abstract methods represent a contract:
# all classes that inherit from an ABC must implement all its abstract methods.

from abc import ABC, abstractmethod, ABCMeta

# A regular class
class MyClass:
    pass

# This class inherits from list. It is a subclass of list
class MyList(list):
    pass

# This class inherits from MyList. It is a subclass of MyList
class MySubList(MyList):
    pass



# ----------------------------------------
# Methods decorated with @abstractmethod must be overriden by inheriting classes
class Person(metaclass=ABCMeta):
    # An abstract method with default implementation
    @abstractmethod
    def work(self):
        print("Go to work")

class Manager(Person):
    pass

# A concrete class - a class that inherits from an abstract base class and
# implements its abstractmethods are concrete classes
class Employee(Person):
    def work(self):
        print("Go to office")

class Athlete(Person):
    def work(self):
        print("Go to gym")

class RandomPerson(Person):
    def work(self):
        super().work()


# ----------------------------------------
if __name__ == "__main__":

    ml = MyList()
    msl = MySubList()

    # Inspecting classes and their classing
    issubclass(MyClass, list) # False, MyClass is not a list
    issubclass(MyList, list) # True, MyList is a list because it inherits from list
    isinstance([], list) # True, [] is an instance of list
    isinstance([], MyList) # False, [] is not an instance of MyList
    isinstance(ml, MyList) # True, ml is created by constructor of MyList
    isinstance(ml, list) # True, ml is also a list because MyList inherits from list
    issubclass(MySubList, list) # True, MySubList inherits from a child of list

    try:
        # TypeError: Can't instantiate abstract class Person with abstract method work
        Person()
    except TypeError:
        pass

    try:
        # TypeError: Can't instantiate abstract class Person with abstract method work
        Manager()
    except TypeError:
        pass

    # A concrete class can be instantiated. Inherting from abstract base
    # classes can be used to enforce guarantees on the presence of a set of methods.
    emp = Employee()

    # Python's polymorphism. Method called depends on type of object
    ath = Athlete()
    rp = RandomPerson()
    emp.work()
    ath.work()
    rp.work()
