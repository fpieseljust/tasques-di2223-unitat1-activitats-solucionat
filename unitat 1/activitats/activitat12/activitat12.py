import os


def suma(x, y): return x + y
def resta(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

class UnrecognizedOperationError(Exception):
    pass


carpeta = os.path.dirname(__file__)
ruta_arxiu_operacion = os.path.join(carpeta, "operacions.txt")
ruta_arxiu_resultats = os.path.join(carpeta, "resultats.txt")

try:
    with open(ruta_arxiu_operacion, 'r', encoding='utf-8') as arxiu_operacions:
        try:
            with open(ruta_arxiu_resultats, 'a', encoding='utf-8') as arxiu_resultats:
                linies = arxiu_operacions.readlines()
                numero_linia = 0
                for linia in linies:
                    numero_linia = numero_linia + 1
                    try:
                        linia = linia.rstrip('\n')
                        operands = linia.split(" ")
                        match operands[1]:
                            case "+":
                                resultat = suma(
                                    int(operands[0]), int(operands[2]))
                            case "-":
                                resultat = resta(
                                    int(operands[0]), int(operands[2]))
                            case "*":
                                resultat = mult(
                                    int(operands[0]), int(operands[2]))
                            case "/":
                                resultat = div(
                                    int(operands[0]), int(operands[2]))
                            case _:
                                raise UnrecognizedOperationError("Operació desconeguda")
                        arxiu_resultats.write(
                            "{} = {}\n".format(linia, resultat))
                    except Exception as e:
                        print("Error executant operació de la línia {} ({}).".format(
                            numero_linia, e.__class__))
        except Exception as e:
            print("Error escrivint l'arxiu de resultats. {}".format(e.__class__))
except Exception as e:
    print("Error llegint l'arxiu d'operacions. {}".format(e.__class__))
