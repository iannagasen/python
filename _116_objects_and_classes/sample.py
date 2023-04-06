
items = [37, 42]
for i in dir(items):
  print(i)

# the __add__ implements the + operator
# the + operator for list is to concatenate the 2 list
# result of this will be equal to [37, 42, 73, 101]
items.__add__([73, 101])





