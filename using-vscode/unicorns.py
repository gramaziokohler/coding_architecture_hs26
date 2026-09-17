class Unicorn:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    
    def __str__(self):
        return f"{self.name} is a {self.color} unicorn, {self.age} years old."
