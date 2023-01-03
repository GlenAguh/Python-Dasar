# not , or , and , xor


# not
print ("----NOT----")
a = False
b = not a
print ("Data a = ",a)
print ("----------NOT")
print ("Data b = ",b)


# or (Jukia salah satu true,maka hasilnya true)
print ("----OR----")
a = False
b = False
c = a or b 
print (a ,'OR',b,'=',c)
a = False
b = True
c = a or b 
print (a ,'OR',b,'=',c)
a = True
b = False
c = a or b 
print (a ,'OR',b,'=',c)
a = True
b = True
c = a or b 
print (a ,'OR',b,'=',c)




# XOR (Akan true, jika salah satu true, sisanya false)
print ("")
print ("----XOR----")
a = False
b = False
c = a ^ b 
print (a ,'XOR ',b,'=',c)
a = False
b = True
c = a ^ b 
print (a ,'XOR ',b,'=',c)
a = True
b = False
c = a ^ b 
print (a ,'XOR ',b,'=',c)
a = True
b = True
c = a ^ b 
print (a ,'XOR ',b,'=',c)




# AND (Jika dua buah nilai true, maka hasilnya true)
print ("")
print ("----AND----")
a = False
b = False
c = a and b 
print (a ,'AND ',b,'=',c)
a = False
b = True
c = a and  b 
print (a ,'AND ',b,'=',c)
a = True
b = False
c = a and b 
print (a ,'AND ',b,'=',c)
a = True
b = True
c = a and   b 
print (a ,'AND ',b,'=',c)