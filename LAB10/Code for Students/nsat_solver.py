

def is_there_unit_clauses(clauses, num_variables):
# return if a single literal exists
    for i in range(0,len(clauses)):
        if len(clauses[i])==1:
            return clauses[i][0]
    return num_variables + 1


def how_many_times(clauses, num_variables):
# return how many times each literal appears.
    how = []
    for i in range(0,num_variables*2):
        how.append(0)
    for i in range(0,len(clauses)):
        for j in range(0,len(clauses[i])):
            lit = clauses[i][j]
            if lit < 0:
                how[num_variables+abs(lit)-1] = how[num_variables+abs(lit)-1] +1
            else:
                how[lit-1] = how[lit-1]+1
    return how            


def update_clauses(clauses, v, value, assignment):
# return the simplified set of clauses + the new assignment 
    top = len(clauses)
    new_clauses = []
    new_assignment = list(assignment)
    new_assignment[v] = value
    for i in range(top):
        aux = list(clauses[i])
        if value==True:
            if not (v in clauses[i]):
                if (-v in clauses[i]):
                    aux.remove(-v)
                    new_clauses.append(aux)
                else:
                    new_clauses.append(aux)
        else:
            if not (-v in clauses[i]):
                if (v in clauses[i]):
                    aux.remove(v)
                    new_clauses.append(aux)
                else:
                    new_clauses.append(aux)  
                                    
    return [new_clauses, new_assignment]                
    

def sat_preprocessing(num_variables, clauses, assignment):
# return the simplified set of clauses with the corresponding assignment
     
                
    update = True
    result = [list(clauses), list(assignment)]
    
    while update:
        update = False   
        
        # Rule 1
        lit = is_there_unit_clauses(result[0], num_variables)
        if (lit <= num_variables):
            update = True
            result = update_clauses(result[0], abs(lit), (lit > 0), result[1])
       
        # Rule 2
        
        how_many = how_many_times(result[0], num_variables)
        for i in range(0,num_variables):
            if how_many[i] + how_many[num_variables+i] == 1:
                update = True
                result= update_clauses(result[0], i+1, (how_many[i]==1), result[1])
                how_many = how_many_times(result[0], num_variables) 
                
        
                
   
        # possible output
        if [] in result[0]:	
            return [None, result[1]]
        else:
            if (result[0] == []) or (not update):
                     return result  


def complete (assignment):
# Fill out the assignment
    for i in range(1,len(assignment)):
        if assignment[i] == None:
                assignment[i] = True
    assignment[0] = False            
    return assignment    

def in_list (l1, l2):
    for elem in l1:
        if elem not in l2:
            return False
    return True    

def solve_SAT_inmersion(num_variables, clauses, assignment):          
    result = sat_preprocessing(num_variables, clauses, assignment)
    if result[0] == None:
        return None
    else:
        if len(result[0])==0:
            return complete(result[1])
        else:
                lit = result[0][0][0]
                result_1 = update_clauses(result[0], abs(lit), (lit > 0), result[1])
                go_ahead = solve_SAT_inmersion(num_variables, result_1[0], result_1[1])
                if go_ahead != None:
                    return go_ahead
                else:
                    result_0 = update_clauses(result[0], abs(lit), (lit < 0), result[1])
                    go_ahead = solve_SAT_inmersion(num_variables, result_0[0], result_0[1])
                    if go_ahead != None:
                        return go_ahead
                    else:
                        return None
	
def solve_nSAT(num_variables, clauses):
    assignment = []
    for i in range(0,num_variables+1):
        assignment.append(None)
    # Primero eliminamos las cláusulas que tengan dos literales opuestos
    for v in range(0,num_variables+1):
        for c in clauses:
            if (v in c) and (-v in c):
                clauses.remove(c)         
    assignment = solve_SAT_inmersion(num_variables, clauses, assignment)
    if assignment != None:
        return assignment
    else:
        return "UNSATISFIABLE"

