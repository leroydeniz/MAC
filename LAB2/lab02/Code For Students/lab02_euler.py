def graph_has_Eulerian_circuit(g):
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    
    #Costo del algoritmo O(n^2)
    
    for i in range(0,len(g)):
        nodo=0
        for j in range(0,len(g[i])):
            if (g[i][j]==1):
                nodo = nodo+1
        if(nodo%2 != 0):
            return False
    return True



def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert not graph_has_Eulerian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g3)
    
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
    
    assert graph_has_Eulerian_circuit(g4)
    

test()

