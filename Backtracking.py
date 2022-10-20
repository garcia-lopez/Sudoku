tabla = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def resolver(tab):
    buscar = encontrar_Vacio(tab)
    if not buscar:
        return True #retorna verdadero unicamente cuando encuentra la solución
    else:
        fila, col = buscar  
    for i in range(1, 10): #i tendra valores del 1 al 9 
        if validar(tab, i, (fila, col)):
            tab[fila][col] = i
            #si el numero es valido se agrega a la tabla
            
            if resolver(tab):
                return True #recursividad para llamar a la funcion resolver 
            #con nuestra nueva tabla
            #si resolver es falsa 
            # reasignamos el valor al numero que acabamos de poner e intentar el for 
            #otra vez con un valor diferente
            tab[fila][col] = 0
            
    return False
                
        

def validar(tab, num, pos): 
    #validar la tabla, el numero a ocupar y la posición vacia
    #revisa la fila
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False
        #Verifica por cada uno de los elementos de una fila para 
        # ver si es igual al numero que se quiere ubicar
        # si la psoción que estamos comparando es 
        # la misma que acabamos de agregarle 
        # no se va a revisar, es decir, la ignorara
        
    #revisa la columna
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False
            #hace lo mismo que la función pasada solo
            #que esta vez con las columnas
            #verifica que no sea la misma en la que acabamos de
            #agregarn un elemento
            
    #revisa el cuadro en el que nos ubicamos
    tabla_x = pos[1] // 3 
    # este operador // permite hacer una integer division
    # la cual consiste en desechar la parte decimal y mantener unicamente
    # la parte entera
    tabla_y = pos[0] // 3
    # x - y determinan si nos encontramos en las cajas superiores, medias o inferiores
    
    #bucle para verificar que no tengamos elementos repetidos en la caja
    for i in range(tabla_y * 3, tabla_y* 3 + 3):
         for j in range(tabla_x * 3, tabla_x * 3 + 3):
             #multiplicamos por tres para llegar a la posición correcta 
             # los indices de x y y serán 0, 1 y 2, para llegar a la pos correcta
             if tab[i][j] == num and (i,j) != pos: #verifica que no sea la misma pos
                 # a la que le acabamos de agregar
                 return False
             
    return True

def imprimirTabla(tab):
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - -")
            # comprueba si estamos en la tercera fila para imprmir
            # una linea horizontal
        for j in range(len(tab[0])):
                # comprueba si es el último elemento de la columna 
                # para imprimir una separación 
           if j % 3 == 0 and j != 0:
               print(" | ", end="")
           if j == 8:
               
                print(tab[i][j])
           else:
                print(str(tab[i][j])  + " ", end=" ")
                #end=" " indica que se mantenga en la misma linea
                5

def encontrar_Vacio(tab):
    #encuentra un lugar vacio en la tabla señalado con un 0
    for i in range(len(tab)):
        for j in range(len(tab[0])): #toma el tamaño de cada fila
            if tab[i][j] == 0:
                return(i, j) #retorna la posción de fila y columna del espacio vacio
    
    return None  #si ya no hay posiciones vacias (iguales a 0) retorna vacio       

imprimirTabla(tabla)
    
resolver(tabla)
print(" ") 
print(" ")
imprimirTabla(tabla)
