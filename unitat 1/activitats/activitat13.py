import random


class ErrorEnterMassaMenut(Exception):
    pass


class ErrorEnterMassaGran(Exception):
    pass


numero_buscat = random.randint(0, 100)
while True:
    numero_introduit = input("Introdueix un número sencer: ")
    try:
        numero_introduit = int(numero_introduit)
        if numero_introduit == numero_buscat:
            print("Enhorabona! Has encertat.")
            break
        elif numero_introduit < numero_buscat:
            raise ErrorEnterMassaMenut
        elif numero_introduit > numero_buscat:
            raise ErrorEnterMassaGran
    except ErrorEnterMassaMenut:
        print("El número introduït és massa menut")
    except ErrorEnterMassaGran:
        print("El número introduït és massa gran")
    except ValueError:
        print("No has introduit un valor vàlid.")
