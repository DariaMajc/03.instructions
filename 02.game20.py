# 2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_number = 13
user_num = 0
user_num += 1
while user_num != secret_number:
     user_num = int(input("Podaj liczbę: "))
     if user_num == 13:
         print('Trafiłeś!')
     else:
         print(f'Twoja liczba to {user_num}. Podaj inną liczbę, ta jest nieprawdłowa')


