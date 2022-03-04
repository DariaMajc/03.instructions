# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input('Wpisz dowolny tekst ')
print(text[2::2])


print(list(range(10, 30, 3)))
text2 = int(text[0])

for text in range(text2, len(text), 2):
    print(text)