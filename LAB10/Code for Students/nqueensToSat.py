from capstone_tools import minisat_display
from capstone_tools import nSAT_solver_display
from capstone_tools import backtracking_display
from time import time
import os,copy



def code(i,j,n):
    return (i-1)*n + j

def decod(m,n):
    if m%n == 0:
        j = n
    else:
        j =m%n
    i = int((m-j)/n) + 1
    return i,j





### CODE ###

def reduce_nqueens_to_SAT(n):
    list=[]
    columnas=[]
    filas=[]

    # presetea variables
    for i in range(n):
        columna=[]
        fila=[]
        
        for j in range(n):
            p1= i+1
            p2= j+1
            fila.append(code(p1,p2,n))
            columna.append(code(p2,p1,n))
            
        filas.append(fila)
        columnas.append(columna)
        
    filasDesc=copy.deepcopy(filas)
    filasAsc=copy.deepcopy(filas)
    filas_copy=copy.deepcopy(filas)
    columnas_copy=copy.deepcopy(columnas)

    # agrego filas y columnas a la lista
    for fila in filas:
        fila.append(0)
        list.append(fila)
        
    for columna in columnas:
        columna.append(0)
        list.append(columna)
        
    # crea diagonales a partir de filas
    for i in filas_copy:
        while len(i)!= 1:
            act=i.pop(0)
            for elem in i:
                clausula=[]
                clausula.append(-act)
                clausula.append(-elem)
                clausula.append(0)
                list.append(clausula)

    for j in columnas_copy:
        while len(j)!= 1:
            act=j.pop(0)
            for elem in j:
                clausula=[]
                clausula.append(-act)
                clausula.append(-elem)
                clausula.append(0)
                list.append(clausula)

    DDescendentes=[]
    DAscendentes=[]

    for i in range(n):
        fila=filasDesc.pop(0)
        
        for elem in fila:
            diagonal1=[]
            diagonal1.append(elem)
            
            for i in range(len(filasDesc)):
                k=-1
                for j in range(len(filasDesc[i])):
                    act=filasDesc[i][j]
                    x,y=decod(elem,n)
                    p,q=decod(act,n)
                    if x-y==p-q:
                        diagonal1.append(act)
                        k=j
                        break
                if k!=-1:
                    filasDesc[i].pop(k)
            if len(diagonal1)!=1:
                DDescendentes.append(diagonal1)
                
    for i in range(n):
        fila=filasAsc.pop(len(filasAsc)-1)
        for elem in fila:
            diagonal1=[]
            diagonal1.append(elem)
            for i in range(len(filasAsc)):
                k=-1
                for j in range(len(filasAsc[i])):
                    act=filasAsc[i][j]
                    x,y=decod(elem,n)
                    p,q=decod(act,n)
                    if (x+y)==(p+q):
                        diagonal1.append(act)
                        k=j
                        break
                if k!=-1:
                    filasAsc[i].pop(k)
            if len(diagonal1)!=1:
                DAscendentes.append(diagonal1)
                
    for i in DAscendentes:
        while len(i)!= 1:
            act=i.pop(0)
            for elem in i:
                clausula=[]
                clausula.append(-act)
                clausula.append(-elem)
                clausula.append(0)
                list.append(clausula)

    for i in DDescendentes:
        while len(i)!= 1:
            act=i.pop(0)
            for elem in i:
                clausula=[]
                clausula.append(-act)
                clausula.append(-elem)
                clausula.append(0)
                list.append(clausula)

    largo=len(list)
    list.insert(0, ['p', 'cnf', n**2, largo])
    return list






### Para visualizar las soluciones

def solve_case_backtracking(filename, n, formula):
    start_time = time()        
    backtracking_display(formula, n)
    elapsed_time = time() - start_time   
    print("Elapsed time for test n=%s with backtracking: %0.10f" % (n,elapsed_time)) 
    with open(filename, 'a') as f:
        f.write("%s,backtracking,%s\n" % (n,elapsed_time))

def solve_case_minisat(filename, n, formula):
    start_time = time()        
    minisat_display(formula, n)
    elapsed_time = time() - start_time   
    print("Elapsed time for test n=%s with minisat: %0.10f" % (n,elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,minisat,%s\n" % (n,elapsed_time))

def solve_case_nSAT_solver(filename, n, formula):
    start_time = time()        
    nSAT_solver_display(formula, n)
    elapsed_time = time() - start_time   
    print("Elapsed time for test n=%s with SATSolver: %0.10f" % (n,elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,SATSolver,%s\n" % (n,elapsed_time))

def generate_formula(filename, n):
    start_time = time()        
    formula = reduce_nqueens_to_SAT(n)
    elapsed_time = time() - start_time   
    print("Elapsed time for n=%s sized formula generation: %0.10f seconds." % (n,elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,formula,%s\n" % (n,elapsed_time))
    return formula
    
def test():

    filename = 'myresults/n_queens_times.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
        

    formula = generate_formula(filename, 10)
    solve_case_minisat(filename, 10, formula)    
    solve_case_backtracking(filename, 10, formula)
    solve_case_nSAT_solver(filename, 10, formula)


    formula = generate_formula(filename, 11) 
    solve_case_minisat(filename, 11, formula)
    solve_case_backtracking(filename, 11, formula)
    solve_case_nSAT_solver(filename, 11, formula)


    formula = generate_formula(filename, 15)
    solve_case_minisat(filename, 15, formula)
    solve_case_backtracking(filename, 15, formula)
    solve_case_nSAT_solver(filename, 15, formula)


    formula = generate_formula(filename, 16)
    solve_case_minisat(filename, 16, formula)
    solve_case_backtracking(filename, 16, formula)
    solve_case_nSAT_solver(filename, 16, formula)


    formula = generate_formula(filename, 28)
    solve_case_minisat(filename, 28, formula)
    solve_case_backtracking(filename, 28, formula)


    formula = generate_formula(filename, 50)
    solve_case_minisat(filename, 50, formula)





test()
