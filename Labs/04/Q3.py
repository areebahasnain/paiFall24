class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def print_biodata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

s1 = Student("Areeba", 21)
s1.print_biodata()

