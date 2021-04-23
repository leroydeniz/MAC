from time import time

def recursive_vertex_cover(graph, cover):

############
# TODO: Programa esta parte de la funcion
#
# Comprueba es posible construir un cover valido.
# Si no es posible, devuelve [1]*len(cover).
# En otro caso, encuentra dos nodos u y v conectados y que no estan en el cover.
# Si no los hay, completa el cover decidiendo si los que faltan deben formar parte 
# del cover o no y una vez hecho esto, devuelve el cover completo.
# En otro caso continua con u y v

    if not partial_validity_check(cover,graph):
        return [1]*len(cover)
    elif nones(cover)==0:
        return cover
    else:
        u,v=par(cover,graph)
        
        if u==-1:
            while nones(cover)!=0:
                u=cover.index(None)
                cover[u]=0
                if not partial_validity_check(cover,graph):
                    cover[u]=1
            return cover
        else:

    # Final de tu codigo
    # Lo siguiente abre las tres ramas del arbol de busqueda.
    # No modificar nada.
    ##############
            copy_cover = list(cover)
            cover[u] = 1
            cover[v] = 0
            c10 = recursive_vertex_cover(graph, cover)
            cover = list(copy_cover)
            cover[u] = 0
            cover[v] = 1
            c01 = recursive_vertex_cover(graph, cover)
            cover = list(copy_cover)
            cover[u] = 1
            cover[v] = 1
            c11 = recursive_vertex_cover(graph, cover)
            if c10.count(1) <= min(c01.count(1), c11.count(1)):
                return c10
            elif c01.count(1) <= c11.count(1):
                return c01
            else:
                return c11


#llamar el árbol de búsqueda
def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover(graph, cover)

#validar que existe un cover
def partial_validity_check(cover, graph):
    graphcover=[]
    for i in range(len(cover)):
        l=[0]*len(graph)
        graphcover.append(l)
    for i in range(len(cover)):
        if cover[i] !=0:
            for j in range(len(cover)):
                if graph[i][j]==1:
                    graphcover[i][j]=1
                    graphcover[j][i]=1
    return graphcover==graph

#bucar el par de nodos
def par(cover,graph):
    u=cover.index(None)
    for i in range(len(cover)):
        if i!=u and cover[i]==None:
            if graph[i][u]==1:
                return i,u
    return -1,-1

def nones(c):
    i=0
    for k in c:
        if k == None:
            i+=1 
        else:
            i=0
    return i

def test():
    g1 =  [[0, 1],
           [1, 0]]
        
    g2 = [[0, 1, 1],
          [1, 0, 0],
          [1, 0, 0]]
        

    g3 = [[0, 1, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 1, 1, 1, 0]]

        
    g4 = [[0, 1, 1, 1],
          [1, 0, 1, 0],
          [1, 1, 0, 1],
          [1, 0, 1, 0]]

        
    g5 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0]]

    g6 = [[0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]





    #    Descomentar para probar la funcion recursive_vertex_cover
    assert vertex_cover_tree(g1) in [[1,0],[0,1]]
    assert vertex_cover_tree(g2)  == [1,0,0]
    assert vertex_cover_tree(g3) in [[1, 0, 1, 0, 1], 
                                [1, 0, 0, 1, 1]]
    assert vertex_cover_tree(g4)  == [1, 0, 1, 0]
    assert vertex_cover_tree(g5)  in  [[0, 1, 1, 1, 0, 0], 
                                [0, 1, 1, 0, 0, 1]]


    assert vertex_cover_tree(g6) in [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                                [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                                [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                                [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]]

start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)      