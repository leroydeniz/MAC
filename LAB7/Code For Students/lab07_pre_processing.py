from time import time

def sat_preprocessing(num_variables, clauses):

    asignacion = {}
    cambio = True

    while cambio:
        cambio = False
        satisfactibles = []
        
        # Si hay alguna clausula formada por una unica variable (negada o no),
        # asigna a dicha variable el valor de verdad para que la cla usula se haga cierta
        for clausula in clauses:
            if len(clausula) == 1:
                if abs(clausula[0]) in asignacion:
                    continue
                    
                if clausula[0] < 0:
                    asignacion[ abs(clausula[0]) ] = 0
                else:
                    asignacion[ abs(clausula[0]) ] = 1
                
                cambio = True
                for i in clauses:
                        if clausula[0] in i:
                            satisfactibles.append(i)
                
        # Si una variable aparece solo una vez y no se le ha asignado previamente un valor de verdad,
        # asigna a dicha variable el valor de verdad para que la cl ́usula se haga cierta.
        count = [0] * (num_variables + 1)

        for clausula in clauses:
            for i in clausula:
                count[ abs(i) ] += 1

        for i in range(1, num_variables + 1):
            if count[i] == 1 and i not in asignacion:

                for clausula in clauses:
                    if i in clausula:
                        asignacion[i] = 1
                        satisfactibles.append(clausula)
                        cambio = True
                    elif -i in clausula:
                        asignacion[i] = 0
                        satisfactibles.append(clausula)
                        cambio = True

        # (c) Elimina todas las clausulas que se hayan hecho ciertas
        clausulas_pendientes = []
        for i in clauses:
            if i not in satisfactibles:
                clausulas_pendientes.append(i)
        
        # (d) Elimina todos los literales que evaluen a False. Es decir,
        # todas las variables x que tengan asignado un 0 y todas las ¬x que
        # tengan asignado un True. Como resultado a este proceso, si una clausula se reduce a [ ],
        # la formula de entrada es insatisfactible y se debe devolver la formula [[1],[-1]]
        for literal in asignacion:
            for clausula in clausulas_pendientes:
                if (literal in clausula and asignacion[literal] == 0):
                    clausula.remove(literal)
                    cambio = True
                elif (-literal in clausula and asignacion[literal] == 1):
                    clausula.remove(-literal)
                    cambio = True

        # Si la formula resultante es insatisfactible debes devolver [[1],[-1]]
        clauses = clausulas_pendientes
        if [] in clauses:
            return [[1], [-1]]

    # Revisa si hay alguna clausula sin asignar y las devuelve
    largo = 0
    for clausula in clauses:
        for i in clausula:
            if (i in asignacion and asignacion[i] == 1) or (-i in asignacion and asignacion[-i] == 0):
                largo += 1
                break
    
    # Cuando el pre-proceso haya acabado, puede ser que la formula resultante
    # sea satisfactible trivialmente. En ese caso debes devolver [].
    if len(clauses) == largo:
        return []

    # En otro caso devolveras la lista de cl ́ausulas resultante.
    return clauses




def test():
    assert [] == sat_preprocessing(1, [[1]])
    assert [[1],[-1]] == sat_preprocessing(1, [[1], [-1]])
    assert [] == sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                            [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                            [1, 3, -4], [3, -4, 1], [-1]])
    assert [[1],[-1]] == sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                            [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                            [-3, -1], [-4], [4, -1, 2]])

    ans = [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4]])
    # Nuevo assert
    assert [] == sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]])
            
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)    