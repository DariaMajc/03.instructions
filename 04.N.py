# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika,
# ale nie większe niż 8).

N = int(input('Podaj N nie wieksze niż 8: '))
if (N > 0) and (N < 8):
    print(f'Silnia z {N} to ')
else:
    print('N musi być większe od 0 i nie może być większe od 8')

iloczyn = 1
for i in range(1, N+1):
    iloczyn = iloczyn * i
    print(iloczyn)