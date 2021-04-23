from tools import list_minisat2list_our_sat

def sat_preprocessing(num_variables, clausulas, asig):

    # variable flag para detectar cambio
    cambio = True

    # comienza el preprocesado
    while(cambio):

        # si la variable termina a False, termina el preprocessing
        cambio = False

        # contador de variables
        cont_variables = [0]*((2*num_variables) - 1)

        clausula = 0
        while clausula < len(clausulas):

            # Si hay alguna clausula formada por una unica variable (negada o no),
            # asigna a dicha variable el valor de verdad para que la cla usula se haga cierta
            if(len(clausulas[clausula]) == 1):
                if(clausulas[clausula][0] > 0): 
                    if(asig[clausulas[clausula][0]] == 0): 
                        return "UNSATISFIABLE", None
                    asig[clausulas[clausula][0]] = 1
                else:
                    if(asig[-clausulas[clausula][0]] == 1): 
                        return "UNSATISFIABLE", None
                    asig[-clausulas[clausula][0]] = 0

            
            # (c)   Elimina todas las clausulas que se hayan hecho ciertas
            # (d)   Elimina todos los literales que evaluen a False. Es decir,
            #       todas las variables x que tengan asignado un 0 y todas las ¬x que
            #       tengan asignado un True. Como resultado a este proceso, si una clausula se reduce a [ ],
            #       la formula de entrada es insatisfactible
            literal = 0
            while literal < len(clausulas[clausula]):
                cont_variables[clausulas[clausula][literal]] = cont_variables[clausulas[clausula][literal]] +1
                if(clausulas[clausula][literal] < 0):

                    # elimina las clausulas que tengan literales negados y asignados 0, evaluan true
                    if(asig[-clausulas[clausula][literal]] == 0):
                        clausulas.pop(clausula)
                        clausula = clausula - 1
                        cambio = True                        
                        break

                    # eilmina los literales negados que tengan asignados 1, luego no aportan a la satisfactibilidad de la clausula
                    elif(asig[-clausulas[clausula][literal]] == 1):
                        clausulas[clausula].pop(literal)
                        literal = literal - 1
                        cambio = True

                else:
                    
                    # eilmina los literales que tengan asignados 0, luego no aportan a la satisfactibilidad de la clausula
                    if(asig[clausulas[clausula][literal]] == 0):
                        clausulas[clausula].pop(literal)
                        literal = literal - 1
                        cambio = True

                    # elimina las clausulas que tengan literales asignados 1, evaluan true
                    elif(asig[clausulas[clausula][literal]] == 1):
                        clausulas.pop(clausula)
                        clausula = clausula - 1
                        cambio = True
                        break
                literal = literal + 1



            # si no hay mas variables en una clausula                 
            if([] in clausulas): 
                return "UNSATISFIABLE", None
            clausula = clausula + 1
            
            
        aux = -num_variables
        while aux <= num_variables:

            # variables que aparecen con un unico signo
            if(cont_variables[-aux] == 0) and (asig[abs(aux)] == None):
                if aux < 0: 
                    asig[-aux] = 0
                else: 
                    asig[aux] = 1
                cambio = True

            # Si una variable aparece solo una vez y no se le ha asignado previamente un valor de verdad,
            # asigna a dicha variable el valor de verdad para que la clusula se haga cierta.
            elif(cont_variables[aux] == 1) and (cont_variables[-aux] == 0):
                if(asig[abs(aux)] == None):
                    if aux < 0: 
                        asig[-aux] = 0
                    else: 
                        asig[aux] = 1
                    cambio = True

            # aumento el contador de apariciones de cada variable
            aux = aux + 1
            
    # devuelve el resultado del preprocessing
    return clausulas, asig