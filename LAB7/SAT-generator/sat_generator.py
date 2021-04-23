import sys
import random

def generate(c,lm):

    sat = []

    for i in range(c):
        cla = []
        varc  = random.randint(1,lm)

        for j in range(varc):

            var = random.randint(1,lm)
            cflip = random.randint(0,1)

            if (cflip):
                cla.append(var*-1)
            else:
                cla.append(var)


        cla2 = list(set(cla))
        sat.append(cla2)
    return sat

if __name__ == "__main__":

    if ( len(sys.argv) != 3):
        sys.exit(0)
    c = int(sys.argv[1])
    lm = int(sys.argv[2])
    print(lm)
    print(c)
    sat = generate(c,lm)
    for i in sat:
        st = ""

        for j in i:
            st += str(j)
            st += " "

        print(st[:len(st)-1])
