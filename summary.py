import random

# 1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem
# lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

name = input('Podaj dowolną liczbę imion: ')
name_list = name.split(" ")

for i in name_list:
    print('Hej', i, '!')

# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input('Wpisz dowolny tekst ')
print(text[2::2])

text2 = text[2::2]
text3 = text2.split(' ')

for i in range(len(text3)):
    print('Znaki na pozycjach parzystych', text3[i])

# 3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

##Python program to count upper case or lower case letter in given string
#str = input("Enter a string: ")
#upper = 0
#lower = 0
#for i in range(len(str)):
      #to lower case letter
      #if (str[i] >= 'a' and str[i] <= 'z'):
      #    lower += 1
      #to upper case letter
      #elif(str[i]>='A' and str[i]<='Z'):
      #    upper+=1
#print('Lower case letters= ',lower)
#print('Upper case letters=' ,upper)



user_char = input('Wpisz dowolny ciag znaków: ')

upper = 0
lower = 0
specialchar = 0
digit = 0
for i in user_char:
    if i.islower():
        lower = lower + 1
    elif i.isupper():
        upper = upper + 1
    elif i.isdigit():
        digit = digit + 1
    elif i.isalnum:
        specialchar = specialchar + 1

print("Małych liter", lower)
print("Wielkich liter:", upper)
print("Znaków specjalnych:", specialchar)
print("Cyfr:", digit)




# 4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
#Użytkownik podaje jedną z 3 figur.
#Komputer losuje jedną z 3 figur.
#Sprawdź kto wygrał tę rundę.
#Zmień kod tak, by użytkownik mógł podac liczbę rund.
#Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

number_of_rounds = input("How many times do you want to play")
number_of_rounds = int(number_of_rounds)

for i in range(0, number_of_rounds):
    if number_of_rounds <= 0:
        break
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action.lower() == 'koniec':
        break
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")




# 5▹ Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.