class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age

def greet(self):
    return f"hi the  name is {self.name,self.age}."
    person = Person('mushkan',21)
    print(person.greet())
