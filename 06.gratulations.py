# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

user_number = input('Podaj numer od 1 do 100 ')
if user_number == '99':
    print('Gratualcje!')
else:
    print('Pudło!')