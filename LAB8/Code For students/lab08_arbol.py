def prim_algorithm(graph):

      # la lista nodos contendrá los nodos que se han ido agregando al arbol
      nodos_cubiertos=[0]*len(graph)

      # arbol que se devolverá
      arbol=[]

      # precargo el arbol con un camino de peso infinito por arista 
      for i in range(0,len(graph)):
            c=[float("inf")]*len(graph)
            arbol.append(c)

      # marcamos un nodo cualquiera, sera el nodo de partida.
      nodos_cubiertos[0]=1

      # mientras haya 0s en la lista nodos, es que aún faltan recorrer algunos de ellos al arbol
      while 0 in nodos_cubiertos:

            # seteamos minimo como inf para que siempre tome los valores de los pesos de las aristas
            minimo=float("inf")

            # tendrá la posicion del nodo y su peso
            elems=()
            for i in range(len(graph)):
                  if nodos_cubiertos[i]==1:

                        # seleccionamos la arista de menor peso incidente en el nodo marcado anteriormente
                        for j in range(len(graph)):

                              # si el nodo no está marcado como cubierto y ademas, su peso es menor que el minimo hasta el momento
                              if nodos_cubiertos[j]==0 and graph[i][j]<minimo:

                                    # se guarda el nuevo minimo y se guarda la posicion y peso en elems
                                    minimo=graph[i][j]
                                    elems=(i,j,minimo)

            # asignamos el peso al camino
            arbol[elems[0]][elems[1]]=elems[2]
            # marcamos el otro nodo en el que incide y asignamos el mismo peso
            arbol[elems[1]][elems[0]]=elems[2]

            # marcamos como cubiertos ambos nodos que ya están en el arbol
            nodos_cubiertos[elems[0]]=1
            nodos_cubiertos[elems[1]]=1

      # el proceso termina cuando tenemos todos los nodos del grafo marcados.
      # devolvemos el arbol minimo
      return arbol


def test():
      g1 =  [[float("inf"), 2.0],
      [2.0, float("inf")]]

      assert prim_algorithm(g1) == g1
      print("Grafo G1 - OK")



      g2 = [[float("inf"), 5.0, 3.0],
      [5.0, float("inf"), float("inf")],
      [3.0, float("inf"), float("inf")]]

      assert prim_algorithm(g2) == g2
      print("Grafo G2 - OK")



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
      print("Grafo G3 - OK")



      g4 = [[float("inf"), 6.0, 2.0, 5.0],
      [6.0, float("inf"), 4.0, float("inf")],
      [2.0, 4.0, float("inf"), 2.0],
      [5.0, float("inf"), 2.0, float("inf")]]

      assert prim_algorithm(g4) == [[float("inf"), float("inf"), 2.0, float("inf")], 
                              [float("inf"), float("inf"), 4.0, float("inf")], 
                              [2.0, 4.0, float("inf"), 2.0], 
                              [float("inf"), float("inf"), 2.0, float("inf")]]
      print("Grafo G4 - OK")



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
      print("Grafo G5 - OK")



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
      print("Grafo G6 - OK")



test()