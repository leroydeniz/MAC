
  
def prim_algorithm(graph):
    nodos=[0]*len(graph)
    arbol=[]
    for i in range(len(graph)):
    	c=[float("inf")]*len(graph)
    	arbol.append(c)
    nodos[0]=1
    while 0 in nodos:
        tupla=buscar_min(graph, nodos)
        añadir(arbol, tupla[0],tupla[1], tupla[2], nodos)
    return arbol
        
def buscar_min(g, nodos):
    tupla=()
    minimo=float("inf")
    for i in range(len(g)):
        if nodos[i]==1:
            for j in range(len(g)):
                if nodos[j]==0 and g[i][j]<minimo:
                    minimo=g[i][j]
                    tupla=(i,j,minimo)
    return tupla
                    
def añadir(arbol, i, j, peso,nodos):
 	arbol[i][j]=peso
 	arbol[j][i]=peso
 	nodos[i]=1
 	nodos[j]=1

        
def test():
    
    g1 =  [[float("inf"), 2.0],
           [2.0, float("inf")]]
    
    assert prim_algorithm(g1) == g1
    print("ok")
    
       
    g2 = [[float("inf"), 5.0, 3.0],
          [5.0, float("inf"), float("inf")],
          [3.0, float("inf"), float("inf")]]
    
    assert prim_algorithm(g2) == g2
    print("ok")   
    
    
    g3 = [[float("inf"), 1.0, 2.0, 3.0, 4.0],
          [1.0, float("inf"), float("inf"), float("inf"), 8.0],
          [2.0, float("inf"), float("inf"), 2.0, 3.0],
          [3.0, float("inf"), 2.0, float("inf"), 5.0],
          [4.0, 8.0, 3.0, 5.0, float("inf")]]
    
    assert prim_algorithm(g3) == [[float("inf"), 1.0, 2.0, float("inf"), float("inf")], 
                                  [1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                  [2.0, float("inf"), float("inf"), 2.0, 3.0], 
                                  [float("inf"), float("inf"), 2.0, float("inf"), float("inf")], 
                                  [float("inf"), float("inf"), 3.0, float("inf"), float("inf")]] 
    
    
        
    g4 = [[float("inf"), 6.0, 2.0, 5.0],
          [6.0, float("inf"), 4.0, float("inf")],
          [2.0, 4.0, float("inf"), 2.0],
          [5.0, float("inf"), 2.0, float("inf")]]
    
    assert prim_algorithm(g4) == [[float("inf"), float("inf"), 2.0, float("inf")], 
                                  [float("inf"), float("inf"), 4.0, float("inf")], 
                                  [2.0, 4.0, float("inf"), 2.0], 
                                  [float("inf"), float("inf"), 2.0, float("inf")]]
    
    
       
    g5 = [[float("inf"), 10.0, 1.0, float("inf"), float("inf"), float("inf")],
          [10.0, float("inf"), float("inf"), 5.0, 4.0, float("inf")],
          [1.0, float("inf"), float("inf"), 8.0, 2.0, 3.0],
          [float("inf"), 5.0, 8.0, float("inf"), float("inf"), 2.0],
          [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")],
          [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
    
    assert prim_algorithm(g5) == [[float("inf"), float("inf"), 1.0, float("inf"), float("inf"), float("inf")], 
                                  [float("inf"), float("inf"),float("inf"), float("inf"), 4.0, float("inf")], 
                                  [1.0, float("inf"), float("inf"), float("inf"), 2.0, 3.0], 
                                  [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2.0], 
                                  [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")], 
                                  [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
    
    
    
    g6 = [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")],
          [3.0, float("inf"), 8.0, 10.0, 5.0, float("inf"), float("inf")],
          [1.0, 8.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
          [float("inf"), 10.0, float("inf"), float("inf"), 6.0, float("inf"), 9.0],
          [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0],
          [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), 4.0],
          [float("inf"),float("inf"),float("inf"), 9.0, 2.0, 4.0, float("inf")]]
    
    
    assert prim_algorithm(g6) == [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                 [3.0, float("inf"), float("inf"), float("inf"), 5.0, float("inf"), float("inf")], 
                                 [1.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 6.0, float("inf"), float("inf")], 
                                 [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), float("inf")], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 2.0, float("inf"), float("inf")]]

    
    print("ok")
test()
