# Casting adalah merubah dari satu tipe ke tipe yang lain

import string
from xmlrpc.client import Boolean

# int
print ("Integerr")
data_integer = 10
print ("Data = ", data_integer  , ",type =", type(data_integer))

data_float = float (data_integer)
data_string = str (data_integer)
data_Boolean = bool (data_integer)

print ("data = ", data_float , ",type =",type (data_float))
print ("data = ", data_string , ",type =", type (data_string))
print ("data = ", data_Boolean , ",type =", type (data_Boolean))




print("")
print("####################")
print("")




# Float
print ("Float")
data_float = 8.9
print ("Data = ", data_float  , ",type =", type(data_float))

data_integer = int (data_float)
data_string = str (data_float)
data_Boolean = bool (data_float)

print ("data = ", data_integer , ",type =",type (data_integer))
print ("data = ", data_string , ",type =", type (data_string))
print ("data = ", data_Boolean , ",type =", type (data_Boolean))




print("")
print("####################")
print("")




# string
print ("String")
data_string = "10"
print ("Data = ", data_string  , ",type =", type(data_string))

data_integer = int (data_string)
data_float = float (data_string)
data_Boolean = bool (data_string)

print ("data = ", data_integer , ",type =",type (data_integer))
print ("data = ", data_float , ",type =", type (data_float))
print ("data = ", data_Boolean , ",type =", type (data_Boolean))




print("")
print("####################")
print("")




# Boolean
print ("Boolean")
data_Boolean = False
print ("Data = ", data_Boolean  , ",type =", type(data_Boolean))

data_integer = int (data_Boolean)
data_float = float (data_Boolean)
data_string = str (data_Boolean)

print ("data = ", data_integer , ",type =",type (data_integer))
print ("data = ", data_float , ",type =", type (data_float))
print ("data = ", data_string , ",type =", type (data_string))

