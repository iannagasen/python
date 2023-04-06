
------------------------------------------
_116_objects_and_classes
  dir(object)
    - returns the list of all the valid attributes in methods of the object
    
    names which begins and end with double underscore implements operator:
      Ex: __add__() implements the + operator

    this are also known as `DUNDER METHODS`

------------------------------------------
_117_modules

  with statement
    - is a control structure used to managed resources that need to be cleaned up or released when they are no longer needed.
    - similar to try-with statement in JAVA

  namespace
    - a container that holds a collection of identifiers 
      (such as  variable names, funciton names, class names, etc) and their corresponding objects
    - Each namespace is like a dictionary, where:
      keys -> identifiers
      values -> the object they refer to
    - Different types of namespace:
      1. Global namespace
        - which contains the names defined at the top level of a module
      2. Local namespaces
        - which contain the names defined within a function or method
      3. Built tin namespaces
        - which contain the names of built in functions and modules
    
    - is closely related to JAVA's package
    - python namespace vs java package
      - java does not provide a way to create custom namespaces for variables or functions.
        Instead, all variables or functions are defined within a class or interface, 
        and their names are scoped to that class or interface
      - java does not have the notion of global namespace like python does,
        all variables and functions must be defined within a class or method
          