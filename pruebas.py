def quick_sort(Lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <= 1:
        return Lista
    Pivote = Lista[-1]
    partir(Lista,0,len(Lista),Pivote,Menores,Iguales,Mayores)
    Ret=quick_sort(Menores)
    Ret.extend(Iguales)
    Ret.extend(quick_sort(Mayores))
    Final = Ret
    return print(Final)

def partir(Lista,i,n,Pivote,Menores,Iguales,Mayores):
    if i == n:
        return Menores,Iguales,Mayores
    if Lista[i] < Pivote:
        Menores.append(Lista[i])
    elif Lista[i] > Pivote:
        Mayores.append(Lista[i])
    elif Lista[i] == Pivote:
        Iguales.append(Lista[i])
    return partir(Lista,i+1,n,Pivote,Menores,Iguales,Mayores)


'''#Invertir lista ------------------------------------------
def aux_invierta(lista,lista_final):
    if lista != []:
        num = lista[-1]
        lista_final.append(num)
        return aux_invierta(lista[:-1],lista_final)
    else:
        return print(lista_final)'''

print(quick_sort([45,98,65,32,48,32,48,651,2]))