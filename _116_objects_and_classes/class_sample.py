

# this is a sample class
# notice in all the Dunder Methods, their 1st argument is self. 
# You actually dont suppy these your self
class Stack: 

  # the constructor of the class
  def __init__(self, *items):
    self._items = list(items)

  def push(self, item):
    self._items.append(item)

  def pop(self):
    return self._items.pop()
  
  # this is equivalent to Object::toString for java
  # you can use this using print(obj)
  def __repr__(self):
    return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'
  
  def __len__(self):
    return len(self._items)
  


# Using the Stack class that we created
s = Stack()
s.push('Dave')
s.push(42)
s.push([3, 4, 5])

# this will print s.__repr__ behind the hood
print(s)

x = s.pop()
print(f'{x} was popped: the Stack is now: {s}')

y = s.pop()
print(f'{y} was popped: the Stack is now: {s}')


###################################################
# Inheritance in python
###################################################

# NumericStack extends Stack and override the push method
class NumericStack(Stack):
  
  # the push() has been redefined to add extra checking.
  # The super() is a way to invoke the prior definition of push()
  def push(self, item):
    if not isinstance (item, (int, float)):
      raise TypeError('Expected an int or float')
    
    super().push(item)
    

###################################################
# Composition
###################################################

class Calculator:
  def __init__(self):
    self._stack = Stack()

  def push(self, item):
    self._stack.push(item)

  def pop(self):
    return self._stack.pop()
  
  def add(self):
    self.push(self.pop() + self.pop())

  def mul(self): 
    self.push(self.pop() * self.pop())

  def sub(self): 
    right = self.pop() 
    self.push(self.pop() - right)

  def div(self): 
    right = self.pop() 
    self.push(self.pop() / right)