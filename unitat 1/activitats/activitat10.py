llista = [1, 5, 4, 6, 8, 11, 3, 12]
parells = list(filter(lambda x: x % 2 == 0,llista))
imparells = list(filter(lambda x: x % 2 == 1, llista))
print("Parells: {}".format(parells))
print("Imparells: {}".format(imparells))