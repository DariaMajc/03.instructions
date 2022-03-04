# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

integer = int(input('Podaj liczbę całkowitą '))
integer2 = int(input('Podaj drugą liczbę całkowitą '))
sum = integer + integer2

if sum > 100:
    print(f'Suma podanych liczb to: {sum}')
else:
    print('Koniec')