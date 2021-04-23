from time import time
from tools import list_minisat2list_our_sat

def sat_preprocessing(num_variables, clauses, asignation):
    cambio = True
    while(cambio):
        cambio = False
        cont_variables = [0]*((2*num_variables) -1)
        #Recorrido de lista
        i = 0
        while i < len(clauses):
            #Aparece una variable de un solo elemento
            if(len(clauses[i]) == 1):
                if(clauses[i][0] < 0): 
                    if(asignation[-clauses[i][0]] == 1): return "UNSATISFIABLE", None
                    asignation[-clauses[i][0]] = 0
                else:
                    if(asignation[clauses[i][0]] == 0): return "UNSATISFIABLE", None
                    asignation[clauses[i][0]] = 1
            
            #Recorrido de clausula
            j = 0
            while j < len(clauses[i]):
                cont_variables[clauses[i][j]]+=1
                if(clauses[i][j] < 0):
                    #Eliminar clausula
                    if(asignation[-clauses[i][j]] == 0):
                        clauses.pop(i)
                        i-=1
                        cambio = True                        
                        break
                    #Eliminar variable
                    elif(asignation[-clauses[i][j]] == 1):
                        clauses[i].pop(j)
                        j-=1
                        cambio = True
                else:
                    #Eliminar variable
                    if(asignation[clauses[i][j]] == 0):
                        clauses[i].pop(j)
                        j-=1
                        cambio = True
                    #Eliminar clausula
                    elif(asignation[clauses[i][j]] == 1):
                        clauses.pop(i)
                        i-=1
                        cambio = True
                        break
                j+=1
            #Caso se han eliminado todos los elementos                  
            if([] in clauses): return "UNSATISFIABLE", None
            i+=1
            
        k = -num_variables
        while k <= num_variables:
            #Caso en la que una variable solo es positiva o negativa
            if(cont_variables[-k] == 0) and (asignation[abs(k)] == None):
                if k < 0: asignation[-k] = 0
                else: asignation[k] = 1
                cambio = True
            #Caso una variable aparece solo una vez
            elif(cont_variables[k] == 1) and (cont_variables[-k] == 0):
                if(asignation[abs(k)] == None):
                    if k < 0: asignation[-k] = 0
                    else: asignation[k] = 1
                    cambio = True
            k+=1
            
    return clauses, asignation

    
def recursive_3SAT(num_variables, clauses, asignation):
    if(len(clauses) == 0): return asignation
    for i in range(len(clauses[0])):
        #VALOR ANTERIOR DE LA CLAUSULA = FALSE
        if(i > 0): asignation[abs(clauses[0][i-1])] = abs(asignation[abs(clauses[0][i-1])]-1)
        #ASIGNACIÓN
        if(clauses[0][i] < 0):
            asignation[-clauses[0][i]] = 0
        else:
            asignation[clauses[0][i]] = 1
    
        #REDUCCIÓN
        clauses_copy = [elem [:] for elem in clauses[1:]]
        asignation_copy = asignation.copy()
        clauses_aux, asignation_aux = sat_preprocessing(num_variables, clauses_copy, asignation_copy)
    
        #ASIGNACION ENCONTRADA
        if(clauses_aux == []): return asignation_aux
    
        #COMPROBACIÓN
        if(clauses_aux != "UNSATISFIABLE"):
            posible_asignation = recursive_3SAT(num_variables, clauses_aux, asignation_aux)
            if(posible_asignation != "UNSATISFIABLE"):
                return posible_asignation
    
    #Es insatisfactible
    return "UNSATISFIABLE"


def solve_3SAT(num_variables, clauses):
   #TODO
   asignation = [None]*(num_variables+1)
   clauses, asignation = sat_preprocessing(num_variables, clauses, asignation)
   if(clauses == "UNSATISFIABLE"): return clauses
   solution = recursive_3SAT(num_variables, clauses, asignation)
   #Delete None's
   if(type(solution) is list):
       for i in range(len(solution)):
           if(solution[i] == None):
               solution[i] = 0
   return solution
   

    
def test():
    
    clauses = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    solutions = [[0, 0, 0, 0],
                 [0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0],
                 [None, 0, 0, 0],
                 [None, 0, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 1, 0]]
    assert solve_3SAT(3,clauses) in solutions
    
    
    clauses = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    solutions = [[0, 1, 0, 0], 
                 [0, 1, 0, 1], 
                 [0, 1, 1, 0], 
                 [0, 1, 1, 1], 
                 [1, 1, 0, 0], 
                 [1, 1, 0, 1], 
                 [1, 1, 1, 0], 
                 [1, 1, 1, 1],
                 [None, 1, 0, 0], 
                 [None, 1, 0, 1], 
                 [None, 1, 1, 0], 
                 [None, 1, 1, 1]]
    assert solve_3SAT(3,clauses) in solutions
    
    
    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]

    assert solve_3SAT(3,clauses) == "UNSATISFIABLE"
    
     
    clauses = [[4, -18, 19],[3, 18, -5],[-5, -8, -15],[-20, 7, -16],[10, -13, -7],
               [-12, -9, 17],[17, 19, 5],[-16, 9, 15], [11, -5, -14],[18, -10, 13],
               [-3, 11, 12],[-6, -17, -8],[-18, 14, 1],[-19, -15, 10],[12, 18, -19],
               [-8, 4, 7],[-8, -9, 4],[7, 17, -15],[12, -7, -14],[-10, -11, 8],
               [2, -15, -11],[9, 6, 1],[-11, 20, -17],[9, -15, 13],[12, -7, -17],
               [-18, -2, 20],[20, 12, 4],[19, 11, 14],[-16, 18, -4],[-1, -17, -19],
               [-13, 15, 10],[-12, -14, -13],[12, -14, -7],[-7, 16, 10],[6, 10, 7],
               [20, 14, -16],[-19, 17, 11],[-7, 1, -20],[-5, 12, 15],[-4, -9, -13],
               [12, -11, -7],[-5, 19, -8],[-16],[20, -14, -15],[13, -4, 10],
               [14, 7, 10],[-5, 9, 20],[10, 1, -19],[-16, -15, -1],[16, 3, -11],
               [-15, -10, 4],[4, -15, -3],[-10, -16, 11],[-8, 12, -5],[14, -6, 12],
               [1, 6, 11],[-13, -5, -1],[-12],[1, -20, 19],[-2, -13, -8],
               [18],[-11, 14, 9],[-6, -15, -2],[-5],[-6, 17, 5],
               [-13, 5, -19],[20, -1, 14],[9, -17, 15],[-5, 19, -18],[-12, 8, -10],
               [-18, 14, -4],[15, -9, 13],[9, -5, -1],[10, -19, -14],[20, 9, 4],
               [-9, -2, 19],[-5, 13, -17],[2, -10, -18],[-18, 3, 11],[7, -9, 17],
               [-15, -6, -3],[-2, 3, -13],[12, 3, -2],[2, -2, -3, 17],[20, -15, -16],
               [-5, -17, -19],[-20, -18, 11],[-9, 1, -5],[-19, 9, 17],[17],[1],
               [4, -16, -5]]
    assert solve_3SAT(20, clauses) == "UNSATISFIABLE" 
    """
    tupla = list_minisat2list_our_sat("instancias/1-unsat.cnf")
    print(solve_3SAT(tupla[0], tupla[1]))    
    """
    print('Tests passed') 
    
    
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time) 

