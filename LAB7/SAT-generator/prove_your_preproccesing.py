import sat_generator
import TU PRE-PROCCESING


# 8 es el num de cláusulas y 6 el num de variables
# puedes cambiar el num de variables y el num de clausulas 
sats = [sat_generator.generate(8,6) for i in range(1)]

# Elimina los posibles repetidos
sats = [[list(set(x)) for x in elem] for elem in sats]

print(sats[0])

print("Tras el preproceso:")
for formula in sats:
    print (TU_PRE-PROCCESING(6,formula))
