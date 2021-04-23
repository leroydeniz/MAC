from time import time
import itertools 
from itertools import combinations


# la funcion has_sum, dada una coleccion de positivos y un valor "value", decide si
# hay una subcoleccion de positivos que sumen "value" o no.    
def has_sum(value, collection):
    
    if value==0:
        return True
    elif collection==[]:
        return False
    elif collection[0]>value:
        return has_sum(value, collection[1:])
    else:
        return has_sum(value-collection[0], collection[1:]) or has_sum(value, collection[1:])
    
    
    



#Tiempo de ejecución del punto 6: 7.0345211029 seconds.
            
            
            
            
            

# la funcion subset, dada una coleccion de positivos y un valor "value", decide
# si existe una subcoleccion de positivos que sumen "value" devuelve dicha 
# subcoleccion. En otro caso devuelve la lista [None].    
def subset(value, collection):
    if value==0:
        return []
    elif collection==[]:
        return [None]
    elif collection[0]>value:
        return subset(value, collection[1:])
    else:
        sol1 = subset(value-collection[0], collection[1:])
        sol2 = subset(value, collection[1:])
        if sol1 == [None]:
            return sol2
        else:
            return sol1 + [collection[0]]
        
        
    
    
    
    
def all_subsets(value, collection):

    #Quito de la colección original los elementos que son mayores al valor, no son combinables
    #no necesito el array ordenado para probar combinaciones en un espacio más acotado
    menores_que_value = []
    soluciones = []
    
    for i in collection:
        aux = []
        if i<=value:
            menores_que_value.append(i)
        
    
    #encuentro las posibles combinaciones para probar de tamaño 2 a n
    for i in range(1,len(menores_que_value)):
        for j in combinations(menores_que_value,i):
            
            if sum(j) == value:
                #saco los elementos de una combinación y los devuelvo como lista
                aux = []
                for k in j:
                    aux.append(k)
                soluciones.append(aux)
    
    #verifica el resultado
    print(soluciones)
    if soluciones==[]:
        return [None]
    else:
        return soluciones






def test():
    
    # coleccion 0
    collection0 = [3, 11, 8, 13, 16, 1, 6]
    value0 = 59
    
    # Primera coleccion
    collection1 = [3, 11, 8, 13, 16, 1, 6]
    value1 = 21
    

    sol11 = [3, 11, 1, 6]
    perm11 = [list(t) for t in itertools.permutations(sol11)]
    perm12 = [[13, 8], [8, 13]]
   
    # Segunda coleccion
    collection2 = [518533, 1037066, 2074132, 1648264,
                   796528, 1593056, 686112, 1372224,
                   244448, 488896, 977792, 1955584,
                   1411168, 322336, 644672, 1289344,
                   78688, 157376, 314752, 629504, 1259008]
    value2 = 2463098
    
    sol21 = [1037066, 796528, 629504] 
    perm21 =[list(t) for t in itertools.permutations(sol21)]
    
    # Tercera coleccion
    collection3 = [15, 22, 14, 26, 32, 9, 16, 8]
    value3 = 53
    
    
    sol31 = [15, 22, 16]
    perm31 = [list(t) for t in itertools.permutations(sol31)]
    sol32 = [14, 15, 16, 8]
    perm32 = [list(t) for t in itertools.permutations(sol32)]   
    sol33 = [9, 22, 14, 8]
    perm33 = [list(t) for t in itertools.permutations(sol33)]
    
    #Cuarta coleccion
    collection4 = [1,5,6]
    value4 = 6
    perm41 = [[6], [1, 5], [5, 1]]
    
    
    #Quinta coleccion
    collection5 = [4,5,1]
    value5 = 6
    perm51 = [[1, 5], [5, 1]]
    
    
    
    
    
#   DESCOMENTAR PARA PROBAR HAS_SUM
#######################################################    
#    assert not has_sum(value0, collection0)
#    assert has_sum(value1, collection1)
#    assert has_sum(value2, collection2)
#    assert has_sum(value3, collection3)
#    assert has_sum(value4, collection4)
#    assert has_sum(value5, collection5)
    
    
#   DESCOMENTAR PARA PROBAR SUBSET
###############################################################
#    assert subset(value0, collection0) == [None]
#    assert subset(value1, collection1) in perm11 + perm12 
#    assert subset(value2, collection2) in perm21
#    assert subset(value3, collection3) in perm31 + perm32 + perm33
#    assert subset(value4, collection4) in perm41 
#    assert subset(value5, collection5) in perm51 
    

##  ALL_SUBSETS PROBATZEKO KOMENTARIOAK KENDU   
##############################################################
    
    assert all_subsets(value0, collection0) == [None]

    all_solutions1 = all_subsets(value1, collection1)
    assert len(all_solutions1) == 2
    assert all_solutions1[0] in perm11 + perm12
    assert all_solutions1[1] in perm11 + perm12
    
    all_solutions2 = all_subsets(value2, collection2)
    assert len(all_solutions2) == 1
    assert all_solutions2[0] in perm21
    
        
    all_solutions3 = all_subsets(value3, collection3)
    assert len(all_solutions3) == 3
    assert all_solutions3[0] in perm31 + perm32 + perm33
    assert all_solutions3[1] in perm31 + perm32 + perm33
    assert all_solutions3[2] in perm31 + perm32 + perm33
    
    
    all_solutions4 = all_subsets(value4, collection4)
    assert len(all_solutions4) == 2
    assert all_solutions4[0] in perm41
    assert all_solutions4[1] in perm41


    all_solutions5 = all_subsets(value5, collection5)
    assert len(all_solutions5) == 1
    assert all_solutions5[0] in perm51
    
    
### PARA MEDIR TIEMPO USA ESTA COLECCION QUE NO TIENE SUBSECCIONES
### QUE SUMEN VALUE5
####################################################################    
#    collection6 = list(range(1,25))
#    value6 = 301
#    assert subset(value6, collection6) == [None]



  
start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
