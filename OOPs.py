# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Hi,I'm {self.name} and I'm {self.age} years old")
#
#     def __str__(self):
#         return f"{self.name},{self.age}years old"
# p1 = Person("Kishore",21)
# p1.greet()
# print(p1)

class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hi, I'm {self.name}")

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"{self.name}'s roll number is {self.roll}")
    def greet(self):
        print("this greetsa child")

s1 = Student("kishore",213)
s1.greet()
s1.show()