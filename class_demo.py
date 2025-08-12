from python_demo import student


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Parent: {self.name} is {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def describe(self):

        print(f"Student: {self.name} is {self.age} years old.")

student = Student("Ram", 25, "Reading")
student.describe()
