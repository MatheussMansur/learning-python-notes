# Module 4 - Object-oriented programming

- class = the cookie cutter, instance = the cookie
- `__init__(self, ...)` is the constructor, runs when the object is created
- `self` is the instance itself, every method needs it as the first parameter
- method inside the class: `self.method()`, outside: `obj.method()`
- `__str__` is what `print(obj)` shows
- `__repr__` is what shows when you just type the object in the console
- `isinstance(obj, Class)`

## inheritance
- `class Fish(Animal):` -> Fish is-a Animal
- is-a is transitive: a ClownFish is also an Animal, and everything is an `object`
- child classes get the parent's methods
- writing a method with the same name in the child overrides it
- a parent method can use an attribute the child created (`self.name`), but
  creating the parent directly breaks if the attribute only exists in the child
