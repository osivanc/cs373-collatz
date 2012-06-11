import random
import sys
def main():
    fout = open("results.out", "a")
    for i in range(0, 1000):
        inta = random.randint(1, 1000000)
        intb = random.randint(1, 1000000)
        stra = ""
        stra = str(inta) + ' ' + str(intb)

#        print "int a =", inta,"int b =", intb
        print stra
#        sys.stdout.write(stra + "\n")

main()
