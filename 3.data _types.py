# DATA TYPES IN PYTHON

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#- OBJECT ----------------------------------- DATA TYPE ------------------ OUTPUT-------------------------------------------
 
a = 5                                           #int     
print(type(a))                  

a = "hello abhi"                                #str
print(type(a))

a = 5.5                                         #float
print(type(a))

a = 1j                                          #complex # for complex number always use 'j' in the object insteat of 'i or anything'
print(type(a))

a = ['abhi','lakhan','ram','seeta','hanuman']   #list 
print(type(a))

a = ('abhi','lakhan','ram','seeta','hanuman')   #tuple
print(type(a))

a = range(5)                                    #range
print(type(a))

a = {'name':'lakhan','age':22 }                 #dict
print(type(a))

a = {'abhi','lakhan','ram','seeta','hanuman'}   #set
print(type(a))

a = frozenset ({'abhi','lakhan','ram','seeta','hanuman'}) #frozenset
print(type(a))

a = True                                        #bool
print(type(a))

a = b"hello"                                    #bytes
print(type(a))

a = bytearray(5)                                #bytearray
print(type(a))

a = memoryview(bytes(5))                        #menoryview
print(type(a))

a = None                                        #none 
print(type(a))


a = 5
print(int(a))

a = "Hello abhi"
print(str(a))

a = 5.5
print(float(a))

a = 5j
print(complex(a))

a = ['ram', 'seeta' , 'hanuman']
print(list(a))

a = ('ram', 'seeta' , 'hanuman')
print(tuple(a))

a = range(5)
print








