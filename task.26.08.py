#encapsulation

class Student:
    def __init__(self, name, age, grade):
        self.name = name  
        self.__age = age  
        self._grade = grade  

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

student1 = Student("Sonu", 16, "12")

print(student1.name)             
print(student1.get_age())        
print(student1.get_grade())      

student1.set_age(20)
print(student1.get_age())      

student1.set_grade("10th")
print(student1.get_grade())      