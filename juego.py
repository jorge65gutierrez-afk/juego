#este es un juego de adivinar el numero 
import random
intentos = 0
print("hola ¿cual es tu nombre?")
nombre = input()
numero = random.randint(1,20)
print("bueno"+nombre+"piensa en un numero entre 1 y 20.")
while intentos <6:
    print("adivinalo tienes 6 intentos")
    adivina = input()
    adivina = int(adivina)
    intentos = intentos+1
    if adivina < numero:
        print("¡deamsiado pequeño!")
    if adivina >numero:
        print("¡demasiado grande!")
    if adivina == numero:
        break
if adivina == numero:
    intentos = str(intentos)
    print("fabuloso"+nombre+"acertaste el numero en "+intentos+"intentos")
if adivina != numero:
    numero = str(numero)
    print("¡que fatalidad!"+nombre+"¡yo estab pensando en el numero!"+numero)