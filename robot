class Robot:
    def __init__(self, name, color, purpose):
        self.name = name
        self.color = color
        self.purpose = purpose
    def introduce(self):
        print("Hello!")
        print("My name is", self.name)
        print("My color is", self.color)
        print("My purpose is", self.purpose)
robot1 = Robot("RoboX", "Blue", "Helping humans")
robot2 = Robot("TechBot", "Red", "Teaching students")
robot1.introduce()
robot2.introduce()
