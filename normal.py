class MyType:                           # [1]
    useUppercase = False

    def __init__(self):
        self.str = "Hello! "
        self.times = 3

    def print_it(self):
        if self.useUppercase:
            print(self.str.upper() * self.times)
        else:
            print(self.str * self.times)

if __name__ == '__main__':
    myObj = MyType()            # [2]
    myObj.print_it()            # [3]
    
    myObj.useUppercase = True
    myObj.print_it()

    mySecondObj = MyType()      
    mySecondObj.print_it()      # [6]


# [1]:  We define a class with a constructor and one method.
#       The method (print_it) uses the variables defined in the constructor!
#       The class contains one **class variable** (useUppercase).
#       The class contains two **instance variables** (str and times)
# [2]:  We create a new instance of MyType called myObj
# [3]:  The method is called and uses the class and instance variables
# [4]:  No exception is thrown because all variables were defined in the class-definition
#       and not added dynamically at a later time.
