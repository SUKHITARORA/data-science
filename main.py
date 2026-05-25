class fruits:
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def display (self):
        print(f"my name is {self.name} and my color is {self.color}")
object1=fruits("orange","orange")
object1.display()                                                                                                                                                                                                                                           
object2=fruits("red","apple")
object2.display()