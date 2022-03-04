# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

rewiev1 = int(input('Podaj swoją opinię o książce'))
rewiev2 = int(input('Podaj swoją opinię o książce'))
rewiev3 = int(input('Podaj swoją opinię o książce'))

avg = (rewiev1 + rewiev2 + rewiev3)//3

if avg >= 7:
    print('Bardzo dobra ksiązka')
elif (avg >= 5) and (avg <= 7):
    print('Przeciętna')
else:
    print('Nie warta uwagi')
