# Tipe Dataa
import string
from xmlrpc.client import boolean


print ("Integerr :")
integer = 2
print ("Data : ",integer)
print ("Bertipe : ", type(integer))

print ("")
print ("-----------------")
print ("")

print ("Float : ")
float = 1.20
print ("Data : " ,float)
print ("Bertipe : ", type(float))

print ("")
print ("-----------------")
print ("")

print ("String : ")
string = "Glennn No Counter"
print ("Data : " ,string)
print ("Bertipe : ", type(string))

print ("")
print ("-----------------")
print ("")

print ("Boolean : ")
boolean = True    # True / False 
print ("Data : " ,boolean)
print ("Bertipe : ", type(boolean))

print ("")
print ("-----------------")
print ("")


print ("Compleks : ")
complex = complex(2,3)   
print ("Data : " ,complex)
print ("Bertipe : ", type(complex))

print ("")
print ("-----------------")
print ("")

# Tipe data dari bahasa C
from ctypes import c_double
c_double = c_double (2.25)
print ("Data : " ,c_double)
print ("Bertipe : ", type(c_double))
