from itertools import permutations  

def graph_has_Hamiltonian_circuit(g):
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    
    camino=[] #define los posibles caminos
    
    #cargo la lista de nodos en el grafo [1,2,3,...n]
    for i in range(0,len(g)):
        camino.append(i+1)
    
    #encuentro todas las permutaciones de posibles caminos entre los nodos anteriores
    posibles_caminos = permutations(camino)
    
    #tomamos uno a uno los posibles caminos en el nodo
    for i in posibles_caminos:
        #va contando la cantidad de nodos conectados en cada camino elegido
        nodos_conectados = 0 
        
        #se va tomando cada nodo y su siguiente para buscar en la matriz si hay un 1
        for j in range(0,len(i)-1):
            
            #si en la matriz hay un 1, entonces esos nodos están conectados
            #luego a nodos_conectados le anoto esta conección, sino, es que ya esa
            #alternativa de camino no será válida y no sigo recorriendo esa opción
            if (g[j][j+1]==1):
                nodos_conectados=nodos_conectados+1
            else:
                break;
        #como caso especial, pregunto por el último elemento y el primero
        #como es el último, no preciso un else para no seguir evaluando
        if(g[i[len(i)-1]-1][i[0]-1]==1):
            nodos_conectados=nodos_conectados+1
            
        #si la cantidad de nodos conectados es igual a la cantidad de nodos del
        #grafo para ese camino, entonces existe un circuito hamiltoniano, luego
        #de encontrar el primero ya no sigue buscando
        if(nodos_conectados==len(i)):
            print(i)
            return True
        
    #si terminó de evaluar todos los caminos y no devolvió True, entonces no
    #existe un camino entre los nodos y devuelve False
    return False
   
    
#El costo del algoritmo es O(2^n)
    

def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g3)
    
    g4 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    g5 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g5)
    
   
   
    
test()
