# Daily Challenge - Circle
# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Object-Oriented Programming (OOP)
# Dunder (Magic) Methods in Python
# Instructions
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.
# Abilities of a Circle Instance
# Your Circle class should be able to:
# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.
# Bonus Challenge (Optional)
# If you want an extra challenge:
# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!
# 💡 Tip:
# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.
import math
import turtle
import random
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle with radius {self.radius}"
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        return Circle(self.radius + other.radius)
    def __gt__(self, other): #comparison of circles if one is greater than another one
        return self.radius > other.radius
    def __eq__(self, other): #comparison of circles if equal
        return self.radius == other.radius
    def __lt__(self, other): #Store multiple circles in a list
        return self.radius < other.radius
c1 = Circle(2)
c2 = Circle(3)

print(c1.area())
print(c1.diameter)

c3 = c1 + c2
print(c3)

print(c1 > c2)
print(c1 == c2)

circles = [Circle(5), Circle(1), Circle(3)]
print(sorted(circles))
# Bonus Challenge (Optional)
# If you want an extra challenge:
# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle() #pen
t.speed(0)
def draw_circle(t, radius, x, y):
    t.penup()
    t.goto(x, y - radius)  # центр круга
    t.pendown()
    t.circle(radius)
circles = [Circle(50), Circle(30), Circle(70), Circle(40)]
sorted_circles = sorted(circles)
x = -200
for circle in sorted_circles:
    draw_circle(t, circle.radius, x, 0)
    x += circle.radius * 2 + 20
turtle.done()
