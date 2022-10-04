import os


suma = lambda x, y: x + y
def resta(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

carpeta = os.path.dirname(__file__)
ruta_arxiu_operacion = os.path.join(carpeta, "operacions.txt")
ruta_arxiu_resultats = os.path.join(carpeta, "resultats.txt")
with open(ruta_arxiu_operacion, 'r', encoding='utf-8') as arxiu_operacions:
    with open(ruta_arxiu_resultats, 'a', encoding='utf-8') as arxiu_resultats:
        linies = arxiu_operacions.readlines()
        for linia in linies:
            linia = linia.strip()
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
                    resultat = None
            arxiu_resultats.write(
                "{} = {}\n".format(linia, resultat))