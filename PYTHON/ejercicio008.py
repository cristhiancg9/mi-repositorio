#STRING Y MAS

esto_es_un_string = "hola cristhian como estas"
esto_es_otro_string = "mundo"

print(esto_es_un_string +' '+ esto_es_otro_string)
#hola mundo

#MAYUS
print(esto_es_un_string.upper())
#minus
print(esto_es_otro_string.lower())
#primera con mayuscula
print(esto_es_un_string.capitalize())
#Poner mayuscula en cada palabra
print(esto_es_un_string.title())
#longitud 
print(len(esto_es_un_string))
#buscar un caracter y muestra su ubicación 
print(esto_es_un_string.find('e'))
#imprimir solo la primera letra , rebanar o slice
print(esto_es_un_string[0:1]) #tu le dices que inicie desde cero
print(esto_es_un_string[:1]) #el asume que inicia desde cero
print(esto_es_un_string[5:14])
#radar
print(esto_es_un_string[::-1])
