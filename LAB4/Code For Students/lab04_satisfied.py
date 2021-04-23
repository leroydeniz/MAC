#El orden del algoritmo es n²

def is_satisfied(num_variables, clauses, assignment):
     # Prendicion: len(assignment) = num_variables + 1
     
     validacion = True  #verifica todas las cláusulas a True
     
     #si encuentro una asignación que sea False, devuelve false
     for clausula in clauses:
         flag = False #verifica al menos un literal a True por cláusula
     
         for lit in clausula:
             if (assignment[abs(lit)]==1 and lit>0) or (assignment[abs(lit)]==0 and lit<0):
                 flag = True
                 break;
                 
         if flag == False:
            validacion = False
            
            
     return validacion
 
    


def test():
    num_variables = 4
    clauses = [[1,2,-3],[2,-4],[-1,3,4]]
    assignment = [0,1,1,1,1]
    assert is_satisfied(num_variables, clauses, assignment)

    assignment = [0,1,0,1,1]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    clauses = [[-3, -1], [2, -3, -4, -1], [-1, -4], [-3], [-1, -2], [-3, 4, -2], [-1, -4, 2]]
    assignment = [0,0,0,1,0]
    assert not is_satisfied(num_variables, clauses, assignment)
    
test()    

