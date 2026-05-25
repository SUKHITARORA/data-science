class student:
    def __init__(self,name,age,gender,color):
        self.name=name
        self.age=age
        self.gender=gender
        self.color=color
    def display(self):
        print(f"my name is {self.name} my age is {self.age} my gender is {self.gender} and my favourite color is {self.color}")
    def check(self,score):
        if(score>50):
            print(f"{self.name} has qualified the exam")
        else:
            print(f"{self.name} has not qualified the exam")
object1=student("sukhit","11","male","black")
object1.display()
object1.check(99)
object2=student("veer","11","male","dark blue")
object2.check(39)
object2.display()