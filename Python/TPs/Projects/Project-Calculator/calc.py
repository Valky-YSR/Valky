import math
def sumn():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    sumn = num+num1
    print(sumn)
def diff():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    diff = num-num1
    print(diff)
def mult():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    mult = num*num1
    print(mult)
def div():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    div = num/num1 
    print(div)
def modulo():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    modulo = num%num1
    print(modulo)
def square():
    num1 = float(input("Saisir un nombre : "))
    sqrt = math.sqrt(num1)
    print(sqrt)
def power():
    num = float(input("Saisir un numbre : "))
    num1 = float(input("Saisir un nombre : "))
    power = math.pow(num,num1)
    print(power)
def sin():
    num = float(input("Saisir un numbre : "))
    print(math.sin(num))
def cos():
    num1 = float(input("Saisir un nombre : "))
    print(math.cos(num1))
def tan():
    num1 = float(input("Saisir un nombre : "))
    print(math.tan(num1))
def fact():
    num1 = float(input("Saisir un nombre : "))
    print(math.factorial(num1))
def valabs():
    num1 = float(input("Saisir un nombre : "))
    print(math.fabs(num1))
def log():
    num1 = float(input("Saisir un nombre : "))
    print(math.log(num1))
def log10():
    num1 = float(input("Saisir un nombre : "))
    print(math.log10(num1))
def minore():
    num1 = float(input("Saisir un nombre : "))
    print(math.floor(num1))
def majore():
    num1 = float(input("Saisir un nombre : "))
    print(math.ceil(num1))
def factorielle():
    num1 = int(input("Saisir un nombre entier : "))
    print(math.factorial(num1))
while True:
    print("""
    Realisee par Yassir KHALFOUFI et BADREDDINE EJJEBLI 
    ====================================================
                        Calculator
    ====================================================
                        Operations
    ====================================================
        | 1 | Somme
        | 2 | Diffrence
        | 3 | Division
        | 4 | Multiplication
        | 5 | Modulo
        | 6 | Square root
        | 7 | Power
        | 8 | Sin
        | 9 | Cos
        | 10| Tan
        | 11| Logarithme
        | 12| Logarithme base 10
        | 13| Minorer un nombre
        | 14| majorer un nombre 
        | 15| Factorielle
        | 0 | Quitter
    ====================================================""")
    op = int(input("select operation : "))
    if op == 1:
        sumn()
    elif op == 2:
        diff()
    elif op == 3:
        div()
    elif op == 4:
        mult()
    elif op == 5:
        modulo()
    elif op == 6:
        square()
    elif op == 7:
        power()
    elif op == 8:
        sin()
    elif op == 9:
        cos()
    elif op == 10:
        tan()
    elif op == 11:
        log()
    elif op == 12:
        log10()
    elif op == 13:
        minore()
    elif op == 14:
        majore()
    elif op == 15:
        factorielle()
    elif op == 0:
        print("Au revoir !")
        break
    else:
        print("choix invalide")
