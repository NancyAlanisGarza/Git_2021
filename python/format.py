#using format option in a simple string
print ("{}: Yako, Nico, Nila, Nona"
.format("Mis Nenes")) 
# using format option for a value stored in a variable 
str = "Mi Vida: {}"
print (str.format("Mi Flako, Natalia y Valentina")) 
# formatting a string using a numeric constant 
print ("Juntos {} años !".format(100000)) 
# usando f.string
name = 'Nancy' 
print (f'Mi Nombre es: {name}')
# usando .format
juego = '{} le gusta a Nico'
print(juego.format('correr,saltar'))  
# today date function 
from datetime import datetime
today = datetime.today().date()
osea = 'puente' 
date_str = f"El día de hoy es: {today}, y aparte es {osea}"
print(date_str)
# usar .format
city_str = '{} lives in {}'
print(city_str.format('Nancy', 'Monterrey'))
print(city_str.format('Amir', 'Guadalajara'))
