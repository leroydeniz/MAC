from time import time
from tools import list_minisat2list_our_sat
from pre_processing import sat_preprocessing
      


    
def solve_3SAT(num_variables, clauses):

    # copia de clausses
    clausulas = clauses

    # la asignacion inicial es vacía, no hay valores para las variables al inicio
    asig = [None] * ( num_variables+1 )

    # se le pasa a la funcion sat_preprocessing del Lab 7, las clausulas, numero de 
    # variables y la asignacion al momento para preprocesar tomando en cuenta esos valores
    clausulas, asig = sat_preprocessing(num_variables, clausulas, asig)

    # como no es insatisfactible, se llama a la función recursiva
    sol = func_recursiva_3SAT(num_variables, clausulas, asig)
    
    # si devuelve insatisfactible, se devuelven todas las clausulas
    if(clausulas == "UNSATISFIABLE"): 
        return clausulas

    # si es satisfactible, se sustituyen los Nones por 0's
    if(type(sol) is list):
        for i in range(len(sol)):
            if(sol[i] == None):
                sol[i] = 0
    
    # se devuelve la solucion resultado
    return sol

    



def func_recursiva_3SAT ( num_variables, clausulas, asig ):

    # busco la solucion mediante un algoritmo recursivo de busqueda
    if(len(clausulas) == 0):
        # si no tiene clausulas, se devuelve la asignacion inicial
        return asig

    # en caso que si hayan clausulas para procesar
    for lit in range(len(clausulas[0])):
        
        # asigno los valores a los literales que ya estan predefinidos
        if(lit > 0): asig[abs(clausulas[0][lit-1])] = abs(asig[abs(clausulas[0][lit-1])]-1)
        
        if(clausulas[0][lit] < 0):
            asig[-clausulas[0][lit]] = 0
        else:
            asig[clausulas[0][lit]] = 1
    
        # se guardan las clausulas y la asignacion para trabajar con sus copias
        clausulas2 = [elem [:] for elem in clausulas[1:]]
        asig2 = asig.copy()

        # se llama nuevamente a la funcion de preprocesado para reducir el tamaño de la formula
        clausulas_aux, asig_aux = sat_preprocessing(num_variables, clausulas2, asig2)
    
        # si se devuelve una lista vacia, es que se proceso toda la formula y hay una solucion
        if(clausulas_aux == []): 
            # la formula es satisfactible, fin del procesado
            return asig_aux
    
        if(clausulas_aux != "UNSATISFIABLE"):

            # aun quedan posibles reducciones en la formula, recursion
            posible_asig = func_recursiva_3SAT(num_variables, clausulas_aux, asig_aux)
            if(posible_asig != "UNSATISFIABLE"):
                return posible_asig
    
    # si no se ha devuelto nada antes, entonces es insatisfactible por defecto
    return "UNSATISFIABLE"





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
    print("Test 1 OK") 
    
    
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
    print("Test 2 OK") 


    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    assert solve_3SAT(3,clauses) == "UNSATISFIABLE"
    print("Test 3 OK") 
    
     
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
    print("Test 4 OK") 
    
    
    
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time) 