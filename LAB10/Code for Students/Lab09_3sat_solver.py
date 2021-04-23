from time import time
from tools import list_minisat2list_our_sat
from pre_processing import sat_preprocessing
      


    
def solve_nSAT(num_variables, clauses):

    # copia de clausses
    clausulas = clauses

    # la asignacion inicial es vacía, no hay valores para las variables al inicio
    asig = [None] * ( num_variables+1 )

    # se le pasa a la funcion sat_preprocessing del Lab 7, las clausulas, numero de 
    # variables y la asignacion al momento para preprocesar tomando en cuenta esos valores
    clausulas, asig = sat_preprocessing(num_variables, clausulas, asig)

    # como no es insatisfactible, se llama a la función recursiva
    sol = func_recursiva_nSAT(num_variables, clausulas, asig)
    
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

    



def func_recursiva_nSAT ( num_variables, clausulas, asig ):

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
            posible_asig = func_recursiva_nSAT(num_variables, clausulas_aux, asig_aux)
            if(posible_asig != "UNSATISFIABLE"):
                return posible_asig
    
    # si no se ha devuelto nada antes, entonces es insatisfactible por defecto
    return "UNSATISFIABLE"
