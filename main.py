# Konversi satuan temperatur suhu


# konversi celcius ke satuan lain
print("Program Konversi temperatur")
print("===== Celcius ke satuan lain ===== \n")

celcius = float(input("Masukkan suhu dalam Celcius : "))
print("- suhu adalah",celcius,"°C")

# Celsius (°C) ke Reamur (°Ré)
CelciusToReamur = (4/5)*celcius
print("- suhu dalam reamur adalah",CelciusToReamur,"°Ré")

# celcius (°C) ke Fahrenheit (°F)
CelciusToFahrenheit = ((9/5)* celcius) + 32
print("- suhu dalam Fahrenheit adalah",CelciusToFahrenheit,"°F")

# celcius (°C) ke Kelvin (K)
CelciusToKelvin = celcius + 273
print("- suhu dalam Fahrenheit adalah",CelciusToKelvin,"k")





print("=============================")
# Konversi Reamur ke-3 satuan lainnya
print("\nProgram Konversi temperatur Suhu")
print("===== Reamur ke satuan lain ===== \n")

reamur = float(input("Masukkan suhu dalam Reamur (°Ré) : "))
print("- Suhu adalah", reamur,"°Ré")

# konversi reamur ke celcius
ReamurToCelcius = (5/4) * reamur
print("- suhu dalam Celcius adalah",ReamurToCelcius,"°C")

# konversi reamur ke Fahrenheit
ReamurToFahrenheit = ((9/4)* reamur) + 32
print("- suhu dalam Fahrenheit adalah",ReamurToFahrenheit,"°F")

# konversi reamur ke kelvin
ReamurToKelvin = ((5/4)* reamur) + 273
print("- suhu dalam Kelvin adalah",ReamurToKelvin,"k")





print("=============================")
# Konversi Fahrenheit ke-3 satuan lainnya
print("\nProgram Konversi temperatur Suhu")
print("===== Fahrenheit ke satuan lain ===== \n")

fahrenheit = float(input("Masukkan Suhu dalam Fahrenheit (°F) : " ))
print("- Suhu adalah", fahrenheit,"°F")

#konversi fahrenheit ke celcius
FahrenheitToCelcius = 5/9 * (fahrenheit - 32)
print("- suhu dalam Celcius adalah",FahrenheitToCelcius,"°C")

#konversi fahrenheit ke reamur
FahrenheitToReamur =  4/9 * (fahrenheit - 32)
print("- suhu dalam reamur adalah",FahrenheitToReamur,"°Ré")

#konversi fahrenheit ke kelvin
FahrenheitToKelvin = FahrenheitToCelcius + 273 # versi pendek
# FahrenheitToKelvin = 5/9 * (fahrenheit - 32) + 273  | veris panjang
print("- suhu dalam Kelvin adalah",FahrenheitToKelvin,"k")





print("=============================")
# Konversi Kelvin ke-3 satuan lainnya
print("\nProgram Konversi temperatur Suhu")
print("===== kelvin ke satuan lain ===== \n")

kelvin = float(input("Masukkan suhu kedalam kelvin : "))
print("- data adalah", kelvin,"K")

#konversi kelvin ke celcius
KelvinToCelcius = kelvin - 273
print("- suhu dalam Celcius adalah",KelvinToCelcius,"°C")

#konversi kelvin ke reamur
# KelvinToReamur = 4/5 * (kelvin - 273) 
KelvinToReamur = 4/5 * KelvinToCelcius
print("- suhu dalam reamur adalah",KelvinToReamur,"°Ré")

#konversi kelvin ke Fahrenheit
# KelvinToFahrenheit = 5/5 * (kelvin - 273) + 32
KelvinToFahrenheit = 9/5 * KelvinToCelcius + 32
print("- suhu dalam Fahrenheit adalah",KelvinToFahrenheit,"°F")