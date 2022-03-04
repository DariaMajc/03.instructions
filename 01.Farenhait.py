# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

# C = 5/9 * (F - 32) wzór F na C

F_degree = 0

while (F_degree <= 200):
    C_degree = round(5 / 9 * (F_degree - 32), 2)
    print(f'{F_degree} F --> {C_degree} C')

    F_degree = F_degree + 20

print('----------------------------------------------------------')


F_degree2 = 0
for F_degree2 in range(0, 201, 20):
    C_degree2 = round(5 / 9 * (F_degree2 - 32), 2)
    print(f'{F_degree2} F --> {C_degree2} C')

    F_degree2 = F_degree2 + 20

