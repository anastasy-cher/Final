import random, time

adiv = {"viento":"Silva sin labios, corre sin pies. En la espalda te pega pero no lo ves.",
        "pizza":"Un cuadrado tiene de envase, redonda es su base y triangular la porción.",
        "silencio":"Si me nombras, ya no estoy. Desaparezco.",
        "mapa":"Hay ríos, pero no agua. Ciudades pero no casas, hay bosques pero no árboles. ¿Dónde?",
        "reloj":"Todo el día sin parar de trabajar, y no se mueve del sitio."
        }

print();print()
print("Bienvenido al juego de adivinar palabras!")
print();print()
print("Adivina la palabra letra por letra.")
print("Tienes 5 vidas y 1 ayuda - una letra abierta.")
print("Al utilizar la ayuda - te bajará la puntuación, al derrotar al boss.")

print();print()
user_select=input("¿Jugamos?(si/no) -  ")

vidas = 5
lista_acertada = []

if user_select == "si" or user_select == "Si" or user_select == "s":
    
    print("Pensando en la palabra secreta...")
    secretword = random.choice(list(adiv))
    time.sleep(1)
    print();print()
    print(adiv[secretword])
    
    
print(" _ " *len(secretword))

print();print()
 
while True:
    while vidas > 0:
        print("Para utilizar la ayuda - marca 33")
        letra_acertada = input("Inserta la letra: ")
        
        if letra_acertada == "33":
            print();print()
            print("Por lo visto esta adivinanza está difícil para ti...")
            print("Bueno... Te bajo la puntuación y seguimos!")
            help = random.choice(list(secretword))
            print();print()
            print("La letra de ayuda, que te ha tocado es '", help,"'")
            break

        if letra_acertada in secretword:
            print();print()
            print("Acertaste la letra")
            lista_acertada.append(letra_acertada)
            break
        else:
            vidas -= 1
            print();print()
            print("Jaja! Te equivocaste!")
            print();print()
            print("Te quedan", vidas,"vidas.")
            break
        
    cont = ""
    letras_faltan = 0
    
    for i in secretword:
        if i in lista_acertada:
            cont += i
        else:
            cont += " _ "
            letras_faltan += 1
            
    print(cont)
    
    if vidas == 0:
        print("Has perdido. La palabra era: ", secretword)
        break
            
    if letras_faltan == 0:
        print("Ganaste!")
        break