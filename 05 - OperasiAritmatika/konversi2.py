print ("Konversi Fahrenheit ke Kelvin")
print ("================================")

Fahrenheit = float(input("Masukkan suhu dalam Fahrenheit:"))
Celcius = ((5/9) * Fahrenheit) - 32  
Kelvin = Celcius + 273
print("suhu dalam Kelvin =", Kelvin, "K")


Kelvin = float(input("Masukkan suhu dalam Kelvin:"))
Celcius  = Kelvin  - 273
Fahrenheit = ((9/5) * Celcius) + 32
print("suhu dalam Fahrenheit =", Fahrenheit, "F")
