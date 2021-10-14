lista = []
lista_nombres_completados = []
posicion = 1
puntaje_obtenido = 530
entry = 'Mikami'
puntaje_final = ''


#Apartado de Ranking ==============================================================================================================================
#Transformar de txt de nombres a lista ------------------------------------
def conseguir_nombres(lista_nombres):
    with open('Ranking_Nombres.txt') as nombres_txt:
        lines = nombres_txt.readlines()
        lista_nombres = lines
        return sort_nombres(lista_nombres, 0)

def sort_nombres(lista_nombres, conteo):
    global lista_nombres_completados, posicion, entry
    posicion = int(posicion)
    if posicion > 10:
        return print('No quedó en el top 10')
    
    if posicion > conteo + 1:
        conteo += 1
        lista_nombres_completados.append(lista_nombres[0])
        return sort_nombres(lista_nombres[1:], conteo)
    
    else:
        entry += '\n'
        lista_nombres_completados.append(entry)
        tamaño = int(len(lista_nombres) - 1)
        lista_nombres_completados = lista_nombres_completados + lista_nombres[0:tamaño]
        return sobreescribir_txt(lista_nombres_completados)

    
def sobreescribir_txt(lista):
    with open('Ranking_Nombres.txt', 'w') as nombres_txt:
        nombres_txt.write(lista[0])
        nombres_txt.write(lista[1])
        nombres_txt.write(lista[2])
        nombres_txt.write(lista[3])
        nombres_txt.write(lista[4])
        nombres_txt.write(lista[5])
        nombres_txt.write(lista[6])
        nombres_txt.write(lista[7])
        nombres_txt.write(lista[8])
        nombres_txt.write(lista[9])
        return 0
        
        

#Transformar de txt de números a lista ------------------------------------
def cont(conteo, lista, seek):
    global posicion
    MiArchi1= open('Ranking.txt', 'r+')
    posicion = 1
    if conteo < 10:
        MiArchi1.seek(seek)
        num = MiArchi1.readline()
        lista.append(int(num))
        conteo += 1
        seek += 5
        return cont(conteo, lista, seek)
    else:
        MiArchi1.close()
        return insert_sort(lista)


#Ordenar de menor a mayor la lista -------------------------------------
def insert_sort(Lista):
    return insert_sort_aux(Lista,1,len(Lista))

def insert_sort_aux(Lista,i,n):
    if i == n:
        return aux_invierta(Lista,[])
    Aux = Lista[i]
    j = incluye_orden(Lista,i,Aux)
    Lista[j] = Aux
    return insert_sort_aux(Lista,i+1,n)

def incluye_orden(Lista,j,Aux):
    if j <= 0 or Lista[j-1]<=Aux:
        return j
    Lista[j] = Lista[j-1]
    return incluye_orden(Lista,j-1,Aux)


#Invertir lista ------------------------------------------
def aux_invierta(lista,lista_final):
    if lista != []:
        num = lista[-1]
        lista_final.append(num)
        return aux_invierta(lista[:-1],lista_final)
    else:
        return comparar(lista_final,[])
    

#Comparar la lista con el puntaje obtenido --------------------------
def comparar(lista,lista_completa):
    global posicion, puntaje_obtenido, volver
    puntaje_obtenido = int(puntaje_obtenido)
    if lista == []:
        #volver =  WINNER_FONT.render('volverás a la pantalla de forma automática', 1, (255,255,255))
        return 0
    if puntaje_obtenido < lista[0]:
        num_mayor = lista[0]
        posicion += 1
        lista_completa.append(num_mayor)
        return comparar(lista[1:],lista_completa)
    else:
        lista_completa.append(puntaje_obtenido)
        tamaño = int(len(lista) - 1)
        lista_completa = lista_completa + lista[0:tamaño]
        print(lista_completa)
        return nueva_lista(lista_completa,0,0)


#Agregar nuevos elementos a la lista completa ----------
def nueva_lista(lista,num,seek):
    global posicion, volver
    MiArchi1= open('Ranking.txt', 'r+')
    if lista == []:
        MiArchi1.close()
        posicion = str(posicion)
        conseguir_nombres([])
        #volver =  WINNER_FONT.render('Felicidades! Quedaste en la posición: '+ posicion, 1, (255,255,255))
        return print('Programá de números se ejecutó con éxito')
    else:
        MiArchi1.seek(seek)
        num = lista[0]
        num = str(num) + '\n'
        MiArchi1.write(num)
        seek += 5
        return nueva_lista(lista[1:],0,seek)



print(cont(0, [], 0))


'''
with open('Ranking.txt', 'r') as f:
    size_to_read = 4
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)'''


        
