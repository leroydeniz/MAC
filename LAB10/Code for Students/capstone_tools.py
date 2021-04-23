
#Graph Visualization
import matplotlib.pyplot as plt

from nsat_solver import solve_nSAT
from tools import num_variables_formula
from nqueens_backtracking import solveNQ

def read_satisfied_assignment(last_line, n):
    last_line=last_line[:-2] #Remove ' 0'
    last_line=last_line.split(None, n*n)
    return [int(x) for x in last_line]

def backtracking_display(clauses, n):
    
    result = solveNQ(n)
    if result == "UNSATISFIABLE":
        print("NOT SATISFIABLE -> CANNOT GRAPHICALLY DISPLAY BOARD")
    else:
        print("DISPLAYING BOARD FOR: " + str(clauses))
        
        # Prepare board
        #columns = ('A', 'B', 'C', 'D', 'E')
        columns = [elem+1 for elem in range(0, n)]
        rows = [elem+1 for elem in range(0, n)]

        #variables = read_satisfied_assignment(last_line, n)
        variables = result
        
        colors = [["black" if var==1 else "w" for var in mylist] for mylist in variables]
        
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        ax.table(#cellText=cell_text,
                             cellColours=colors,
                             colLabels=columns,
                             rowLabels=rows,
                             loc='center')
        
        plt.show()

#Call sat_solver to solve and visualization if satisfiable
def nSAT_solver_display(clauses, n):
    num_variables = num_variables_formula(clauses)
    for i in range(1,len(clauses)):
        clauses[i].remove(0)
    result = solve_nSAT(num_variables, clauses[1:]) 
    if result == "UNSATISFIABLE":
        print("NOT SATISFIABLE -> CANNOT GRAPHICALLY DISPLAY BOARD")
    else:
        print("DISPLAYING BOARD FOR: " + str(clauses))
        
        # Prepare board
        #columns = ('A', 'B', 'C', 'D', 'E')
        columns = [elem+1 for elem in range(0, n)]
        rows = [elem+1 for elem in range(0, n)]

        #variables = read_satisfied_assignment(last_line, n)
        variables = result[1:n*n+1]
        
        colors = ["black" if var==True else "w" for var in variables]
        
        colors = [colors[x:x+n] for x in range(0, len(colors), n)]
        
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        ax.table(#cellText=cell_text,
                             cellColours=colors,
                             colLabels=columns,
                             rowLabels=rows,
                             loc='center')
        
        plt.show()
    
#Call minisat to solve and visualization if satisfiable
def minisat_display(clauses, n):

    filename = 'myresults/' + str(n) + '_queens' +  '.txt'
    
    #List to Str
    listToStr = [' '.join([str(elem) for elem in clause]) for clause in clauses]
    
    import os
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w+') as f:
        for item in listToStr:
            f.write("%s\n" % item)
        
    
    my_command = 'minisat ' + filename + ' ' + filename + '_output.txt'
    p = os.popen(my_command,"r")
    while 1:
        line = p.readline()
        if not line: break
        print(line)
    
    output_file = filename + '_output.txt'
    f_read = open(output_file, "r")
    last_line = f_read.readlines()[-1]
    print(last_line)
    f_read.close()
    
    if "UNSAT" in last_line:
        print("NOT SATISFIABLE -> CANNOT GRAPHICALLY DISPLAY BOARD")
    else:
        print("DISPLAYING BOARD FOR: " + filename)
        
        # Prepare board
        #columns = ('A', 'B', 'C', 'D', 'E')
        columns = [elem+1 for elem in range(0, n)]
        rows = [elem+1 for elem in range(0, n)]

        variables = read_satisfied_assignment(last_line, n)
        
        colors = ["black" if var>0 else "w" for var in variables]
        
        colors = [colors[x:x+n] for x in range(0, len(colors), n)]
        
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        ax.table(#cellText=cell_text,
                             cellColours=colors,
                             colLabels=columns,
                             rowLabels=rows,
                             loc='center')
        
        plt.show()