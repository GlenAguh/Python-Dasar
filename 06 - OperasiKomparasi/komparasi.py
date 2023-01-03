# Operasi Komparasi

# >, <, >= , <=, ==, !=, is, is not

a = 2
b = 4

# lebih dari >
print ("=======================")
print ("Lebih dari >")
hasil = a > 3 
print (a, '>', 3, '=', hasil)
hasil = b > 3 
print (b, '>', 3, '=', hasil)
hasil = b > 2 
print (b, '>', 2, '=', hasil)


print ("")
print ("========================")
print ("Kurang dari <")
# kurang dari <
hasil = a < 3 
print (a, '<', 3, '=', hasil)
hasil = b < 3 
print (b, '<', 3, '=', hasil)
hasil = b < 2 
print (a, '<', 2, '=', hasil)



print ("")
print ("========================")
print ("Kurang dari <=")
# kurang dari sama dengan <=
hasil = a <= 3 
print (a, '<=', 3, '=', hasil)
hasil = b <= 3 
print (b, '<=', 3, '=', hasil)
hasil = b <= 2 
print (a, '<=', 2, '=', hasil)



print ("")
print ("========================")
print ("lebih dari sama dengan >=")
# kurang dari sama dengan <=
hasil = a >= 3 
print (a, '>=', 3, '=', hasil)
hasil = b >= 3 
print (b, '>=', 3, '=', hasil)
hasil = b >= 2 
print (b, '>=', 4, '=', hasil)



print ("")
print ("========================")
print (" sama dengan ==")
# sama dengan ==
hasil = b == 3 
print (b, '==', 3, '=', hasil)
hasil = b == 4 
print (b, '==', 4, '=', hasil)




print ("")
print ("========================")
print (" sama dengan !=")
# sama dengan ==
hasil = b != 3 
print (b, '!=', 3, '=', hasil)
hasil = b != 4 
print (b, '!=', 4, '=', hasil)



print ("")
print ("========================")
print (" is ")
# sebagai komparasi object identifity
x = 5
y = 5
hasil = x is y
print ('x is y =', hasil) 

x = 5
y = 6
hasil = x is y
print ('x is y =', hasil) 



print ("")
print ("========================")
print (" is not  ")
# sebagai komparasi object identifity
x = 5
y = 5
hasil = x is not y
print ('x is y =', hasil) 

x = 5
y = 6
hasil = x is not y
print ('x is y =', hasil) 