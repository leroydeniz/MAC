from vertex_cover import solve_vc


def multisolve(graph, problem):    
    if problem ==  "VERTEX COVER":
        return solve_vc(graph)  
    else:
        if problem == "INDEPENDENT SET":
            min_vc=solve_vc(graph)
            for elem in range(0,len(min_vc)):
                if min_vc[elem]==0:
                    min_vc[elem]=1
                else:
                    min_vc[elem]=0
            return  min_vc
        else:
            #CLIQUE
            grafo_IS = []
            for i in range(len(graph)):
                lc = [((x+1)%2) for x in graph[i]]
                lc[i] = 0
                grafo_IS.append(lc)

            VertexCover_Result = solve_vc(grafo_IS)
            result = [((x+1)%2) for x in VertexCover_Result]
            return result



def test():
   graph = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   sol_clique = multisolve(graph, "CLIQUE")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]
   
   graph = [[0,1,1],[1,0,1],[1,1,0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   sol_clique = multisolve(graph, "CLIQUE")
     
   assert sol_vertex in [[0,1,1], [1,0,1], [1,1,0]]
   assert sol_independent_set in [[1,0,0],[0,1,0],[0,0,1]]
   assert sol_clique in [[1,1,1]]


test()
