"""Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie

danych kończone jest podaniem wartości 0 (nie wliczana do danych). W następ-
nej kolejności program powinien wyświetlić sumę największej oraz najmniejszej

z podanych liczb oraz ich średnią arytmetyczną. Rozszerz zadanie, aby program
wyświetlał całą sekwencję liczb wprowadzonej przez użytkownika.
Przykład:
Użytkownik podał ciąg: 1, -4, 2, 17, 0.
Wynik programu:
13 // suma min. i maks.
6.5 // średnia"""

# TODO można coś przyświrować
def MinMax():

    userInput = input("Type a number (type 0 to stop): ")
    inputLog = "" + userInput

    num = int(userInput)
    uMin = num
    uMax = num

    while num != 0:
        userInput = input("Type a number (type 0 to stop): ")
        inputLog = inputLog + " " + userInput
        num = int(userInput)

        if num < uMin:
            uMin = num
        elif num > uMax:
            uMax = num

    print(f" User input: {inputLog.split()}")
    print(f" Min: {uMin}")
    print(f" Max: {uMax}")
    print(f" Average: {(uMin+uMax)/2}")

MinMax()