class MyType:                           # [1]
    def print_it(self):
        if self.useUppercase:
            print(self.str.upper() * self.times)
        else:
            print(self.str * self.times)

if __name__ == '__main__':
    myObj = MyType()                # [2]
    MyType.useUppercase = True      # [3]
    myObj.str = "Hello! "           # [4]
    myObj.times = 3                 # [5]
    myObj.print_it()                # [6]
    
    mySecondObj = MyType()      
    print(mySecondObj.useUppercase) # [7]
    mySecondObj.print_it()          # [8]


# [1]:  We define a class without constructor and one method.
#       The method (print_it) uses undefined attributes!
# [2]:  We create a new instance of MyType called myObj
# [3]:  We (dynamically) add a class variable to MyType called useUppercase
# [4]:  We (dynamically) add an instance variable (of type string) to this (and only this!) object.
# [5]:  We add an instance variable (of type int)
# [6]:  The method is called and uses the "dynamically" inserted attributes (1 class variable and 2 instance variables)
# [7]:  The class variable useUppercase is printed (which was defined dynamically in #3)
# [8]:  Which exception is thrown? Why?
