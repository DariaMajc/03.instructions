# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

text = 'Trolololoa'
text_len = len(text)
text_a = text.count("a")
if (text_len > 5) and text_a >= 1:
    print(text[:8]+'z')