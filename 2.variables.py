
# variables: Variables are containers for storing data values.

#     * python has no cammand for declareing vatiable.
#     * a variable is created the moment you first assign a value t it. 
#     * variable do not need to be declare with any perticular type and even change after they have been set

#example

x = 4                # x is of type int
print(x)    

x = "Abhi"           # x is now type str
print(x)

#-----------------------------------------------------------------------------------------------------------------------
#Casting : if you want to specify the data type of a variable,this can be done with Casting
#example

x = str("cast") 
y = int(3) 
z = float(3.1)  

print(x)
print(y)
print(z)

#---------------------------------------------------------------------------------------------------------------------------
#Get the type: You can get the type of a variable with the  type() function
#example

x = 5
y = "Abhi"
print(type(x))
print(type(y))


#string variable can be declare either single('') or double quote(" ")

#varible names are case sensitive
#Example
a=10
A="Abhi"
print(a)
print(A)

#----------------------------------------------------------------------------------------------------------
# variable name examples
#variable name can only contain alphanumeric characters and underscores( A-a, 0-9 , _ )

myvar   ="abhi"
my_var  = "abhi"
_my_var = "abhi"
myVar   = "abhi"
MyVar   = "abhi"
myvar2  = "abhi"


print(myvar)
print(my_var)
print(_my_var)
print(myvar)
print(MyVar)
print(myvar2)

#----------------------------------------------------------------------------------------------
#Assign multi values
#Example

x , y, z = 1 , "Abhi", "Nashik"

print(x)
print(y)
print(z)

#------------------------------------------------------------------------------------------------

# one value to multiple
x=y=z="red"
print(x)
print(y)
print(z)

#----------------------------------------------------------------------------------------------

# Unpacked collection
car = ["Tata","Mahindra","Maruti"]
x,y,z=car
print(x)
print(y)
print(z)

# -----------------------------------------------------------------------------------------------
# Output variable

# The Python print() function is often used to output variables.

x= "hello "
y= " python"
print( x + y)

#-------------------------------------------------------------------------------------------------
# Global variables : variables that are created a outside a function are known as global variables.
#example

x = " this is global variable test "

def myfunc():
   print("hii abhi" + x)
myfunc()

# -------------------------------------------------------------------------------------------------
#local variable : Variable that are created inside a finction is known as local variables.
#example
def myfun():
   x = "this is local variable test"
   print("hii abhi " + x)
myfun()

# -----------------------------------------------------------------------------------------------------
#global Kyword
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# -------------------------------------------------------------------------------------------------------

  
