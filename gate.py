def AND (a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def NAND (a,b):
    if a==1 and b==1:
        return 0
    else:
        return 1
    
def OR (a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1

def NOR (a,b):
    if a==0 and b==0:
        return 1
    else:
        return 0
    
def XOR (a,b):
    if a==b:
        return 0
    else:
        return 1
    
def XNOR (a,b):
    if a==b:
        return 1
    else:
        return 0
    

print("+-------+-------+--------------+")
print("|      AND GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A AND B =",AND(0,0)," |")
print("| A = 0 | B = 1 | A AND B =",AND(0,1)," |")
print("| A = 1 | B = 0 | A AND B =",AND(1,0)," |")
print("| A = 1 | B = 1 | A AND B =",AND(1,1)," |")
print("+-------+-------+--------------+")

print("+-------+-------+--------------+")
print("|      NAND GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A NAND B =",NAND(0,0)," |")
print("| A = 0 | B = 1 | A NAND B =",NAND(0,1)," |")
print("| A = 1 | B = 0 | A NAND B =",NAND(1,0)," |")
print("| A = 1 | B = 1 | A NAND B =",NAND(1,1)," |")
print("+-------+-------+--------------+")

print("+-------+-------+--------------+")
print("|      OR GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A OR B =",OR(0,0)," |")
print("| A = 0 | B = 1 | A OR B =",OR(0,1)," |")
print("| A = 1 | B = 0 | A OR B =",OR(1,0)," |")
print("| A = 1 | B = 1 | A OR B =",OR(1,1)," |")
print("+-------+-------+--------------+")

print("+-------+-------+--------------+")
print("|      NOR GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A NOR B =",NOR(0,0)," |")
print("| A = 0 | B = 1 | A NOR B =",NOR(0,1)," |")
print("| A = 1 | B = 0 | A NOR B =",NOR(1,0)," |")
print("| A = 1 | B = 1 | A NOR B =",NOR(1,1)," |")
print("+-------+-------+--------------+")

print("+-------+-------+--------------+")
print("|      XOR GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A XOR B =",XOR(0,0)," |")
print("| A = 0 | B = 1 | A XOR B =",XOR(0,1)," |")
print("| A = 1 | B = 0 | A XOR B =",XOR(1,0)," |")
print("| A = 1 | B = 1 | A XOR B =",XOR(1,1)," |")
print("+-------+-------+--------------+")

print("+-------+-------+--------------+")
print("|      XNOR GATE TRUTH TABLE    |")
print("+-------+-------+--------------+")
print("| A = 0 | B = 0 | A XNOR B =",XNOR(0,0)," |")
print("| A = 0 | B = 1 | A XNOR B =",XNOR(0,1)," |")
print("| A = 1 | B = 0 | A XNOR B =",XNOR(1,0)," |")
print("| A = 1 | B = 1 | A XNOR B =",XNOR(1,1)," |")
print("+-------+-------+--------------+")



