class MyType:                           # [1]
    def print_it(self):
        print(self.str * self.times)

if __name__ == '__main__':
    myObj = MyType()            # [2]
    myObj.str = "Hello! "       # [3]
    myObj.times = 3             # [4]
    myObj.print_it()            # [5]
    
    mySecondObj = MyType()      
    mySecondObj.print_it()      # [6]


# [1]:  We define a class without constructor and one method.
#       The method (print_it) uses undefined attributes!
# [2]:  We create a new instance of MyType called myObj
# [3]:  We add an attribute (of type string) to this (and only this!) object.
# [4]:  We add an attribute (of type int)
# [5]:  The method is called and uses the "dynamically" inserted attributes
# [6]:  Which exception is thrown? Why?
