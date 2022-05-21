import clases as cl
import sonidos_pantallas as sp
import utilidades as ut
import random,time
        # Dimension Planet Express

    #jugadores
#bender
bender = cl.Jugador("Bender",100,40,50,50,20,"Este jugador es muy sociopatico e impredecible. ")

#habilidades
calentador = cl.Habilidades("Calentador de agua","veneno",(5,10),"echa agua hirrviendo al villado, dejando quemaduras, que quitarán vida. ")
estiron = cl.Habilidades("Estirón brusco","normal",(10,20),"las piernas y brazon de estiran a gran longitud bruscamente para hacer el golpe inesperado.")
canyon = cl.Habilidades("Cañon","normal",(0,50),"Bender puede utilizarse como cañon, para dispara, lo malo es que no sabe apuntar bien, asi que puede quitar mucha o nada de vida.")

#items
#sk
doblador = cl.Items("Doblar objetos","sk",0,"Bender fue creado como doblador de objetos profesional. Dale golpes fuertes al enemigo!",1)

#ataque
thompson = cl.Items("Thompson 1928","a",20,"subfusil favorito, desde que Bender trabajó con la mafia. Aumenta tu fuerza!",2)

#sanacion
benderbrau = cl.Items("La cerveza 'Bendërbrau'","s",15,"con la cerveza favorita de Bender aumenta tu salud!",1)

#item de precision 
detector = cl.Items("Detector de homosexuales","p",25,"con este detector de homosexuales Bender se vuelve más activo y tu precisión aumenta",1)

faro = cl.Items("Faro incorpordo","p",30,"con el faro encendidio aumentas tu precision a la hora del golpe.")

#villanos( Nombre, Vida, Ataque, Defensa, Precision, Velocidad)
zapp_branningan = cl.Mob("Zapp Branningen",100,5,5,50,100)
hipnosapo = cl.Mob("Hipnosapo",100,5,5,50,10)
babosa_cerebral = cl.Mob("Babosa Cerebral",100,5,5,50,10)

#dimension

dimension_express = cl.Dimension("Planet Express",[doblador,thompson,benderbrau,detector,faro],[zapp_branningan,hipnosapo,babosa_cerebral])


def mostrar_bender():
    print("""
---------------------------------------------------------------------------------------------
                                                                             ( )
                                                                              H
                                                                              H
    Nombre: {}                                                               _H_ 
                                                                         .-' -.-'-.
    Defensa: {}                                                         /           \\
                                                                        |            |
    Precision: {}                                                       |   .-------'._
                                                                        |  / /  '.' '. \\
    Velocidad: {}                                                       |  \ \ @   @ / / 
                                                                        |   '---------'        
    Descripcion: {}                                                     |     _______|  
                                                                        |   .'-+-+-+|  
                                                                        |   '.-+-+-+|         
                                                                        |     """"""       |
                                                                        '-._ _   __.-'
---------------------------------------------------------------------------------------------
          """.format(bender.nombre, bender.ataque,bender.defensa,bender.precision,bender.velocidad))
        
mostrar_bender()