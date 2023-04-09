# Python Numeric Data Type
var1 = 1
var2 = 10
var3 = 10.023
var4 = 10.23j
print(var1, var2, var3, var4)

# Python String Data Type
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# Python List Data Type

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinyList = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinyList * 2)    # Prints list two times
print (list + tinyList) # Prints concatenated lists

# Python Tuple Data Type
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinyTuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinyTuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinyTuple)   # Prints concatenated tuples

# Python Ranges
# range(start, stop, step)
for i in range(5):
  print(i)
for i in range(1, 5):
  print(i)
for i in range(1, 5, 2):
  print(i)
# Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinyDict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinyDict)          # Prints complete dictionary
print (tinyDict.keys())   # Prints all the keys
print (tinyDict.values()) # Prints all the values

# Python Data Type Conversion
    # Conversion to int
a = int(1)     # a will be 1
print (a)
    # Conversion to float
c = float("3.3") # c will be 3.3
print (c)
    # Conversion to string
a = str(1)     # a will be "1" 
print (a)

# Data Type Conversion Functions
# int(x [,base]), long(x [,base]), float(x), complex(real [,imag]), str(x), repr(x), eval(str), tuple(s), list(s), set(s), dict(d), 	
# frozenset(s), chr(x), unichr(x), ord(x), hex(x), oct(x)