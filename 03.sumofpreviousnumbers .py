#Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
#Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

sum_number = 1
for number in range(11):
    sum_number = sum_number + number
    print(sum_number)
