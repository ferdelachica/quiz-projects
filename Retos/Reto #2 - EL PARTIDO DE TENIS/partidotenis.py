def partidotennis(jugadas):
    #Definimos las variables para los puntos de cada jugador
    p1 = 0
    p2 = 0
    #Definimos la puntuación posible en los partidos de tenis
    puntuacion = ["Love", "15", "30", "40"]
   
    for i in jugadas:
        #Si Gana el punto el P1 le sumará 1 posición
        if i == "P1":
            p1 +=1
        #Si Gana el punto el P2 le sumará 1 posición
        elif i == "P2":
            p2+=1
        else:
        #Si introduces un parámetro incorrecto saldrá error
            print("Error, jugador incorrecto")
            return
        
        #Si la posición de los jugadores es mayor a la tercera posición (40) se definen las posibilidades
        if p1 >3 or p2>3:
            if p1 == p2:
                print("Deuce")
            elif p1 > p2:
                print("Ha ganado el P1")
                return
            elif p1 -1 == p2:
                print("Ventaja para P2")
            elif p2 > p1:
                print("Ha ganado el P2")
                return
            else:
                print("Error de resultado")
        
        #Si los dos jugadores se encuentran en la misma posición (40) entrarán en el tie-break
        if p1 == 3 and p2 == 3:
            print("Deuce")
        else:
            print(f'{puntuacion[p1]} - {puntuacion[p2]}')

partidotennis(["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P1"])
    