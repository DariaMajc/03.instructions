# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Podaj hasło. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków')
password.isalpha()
password.isdigit()
password.islower()

if len(password) <= 8:
    print('Hasło musi miec conajmniej 8 znaków.')
elif password.isdigit() or password.isalpha():
    print('Hasło musi zawierac cyfry i litery')
elif password.islower():
    print('Hasło zwierać conajmniej 1 małą literę.')
elif password.isupper():
    print('Hasło zwierać conajmniej 1 dużą literę.')
else:
    print('Hasło Twoje hasło jest prawidłowe.')

