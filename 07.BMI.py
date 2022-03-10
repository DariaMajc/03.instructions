# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

moja_masa = input('Jaka jest Twoja masa?')
moja_masa = int(moja_masa)
moj_wzrost = input('Jaki jest Twoj wzrost?')
moj_wzrost = int(moj_wzrost)

BMI = moja_masa / (moj_wzrost ** 2)
print('Twoje BMI to ', BMI)

if BMI <= 0.0012:
    print('Niedowaga')
elif (BMI > 0.0012) and (BMI <= 0.002):
    print('Waga normalna')
elif (BMI > 0.002) and (BMI <= 0.003):
    print('Nadwaga')
elif BMI > 0.003:
    print('Otyłość')
