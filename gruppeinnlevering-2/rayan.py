# Gruppeinnlevering 2 - IS-118
# Interaktiv historie om prosjektleder Erling
# Hvert valg gir poeng, og poengene bestemmer slutten

poeng = 0

# Introduksjon
print("--- Erling og stormen ---")
print("Det har gått seks uker siden Erling startet prosjektet med den nye medborgerportalen.")
print("Teamet er i storming-fasen og det har begynt å oppstå konflikter.")
print("Silje og Elias krangler om design og teknologi.")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Prototypen skal være ferdig om tre uker.")
print()

# Valg 1 - Silje og Elias
print("VALG 1: Silje og Elias krangler på møtet. Hva gjør du?")
print("A: Snakker med dem hver for seg")
print("B: Tar det opp med hele teamet")
valg1 = input("Skriv A eller B: ").upper()

# Spør på nytt hvis brukeren skriver noe annet enn A eller B
while valg1 != "A" and valg1 != "B":
    valg1 = input("Ugyldig valg, skriv A eller B: ").upper()

if valg1 == "A":
    print("Begge føler seg hørt og stemningen blir roligere.")
    poeng = poeng + 2
else:
    print("Det blir en ubehagelig diskusjon, men nå vet alle hva konflikten handler om.")
    poeng = poeng + 1
print()

# Valg 2 - Hamdi og Hallgeir
print("VALG 2: Hamdi og Hallgeir snakker nesten ikke sammen lenger. Hva gjør du?")
print("A: Kaller inn til et felles møte")
print("B: Venter og håper de løser det selv")
valg2 = input("Skriv A eller B: ").upper()

while valg2 != "A" and valg2 != "B":
    valg2 = input("Ugyldig valg, skriv A eller B: ").upper()

if valg2 == "A":
    print("De finner et kompromiss og begge er fornøyde.")
    poeng = poeng + 2
else:
    print("Hallgeir sender en sur mail til hele teamet. Konflikten blir større.")
print()

# Valg 3 - Motivasjon
print("VALG 3: Teamet er slitent. Hva gjør du?")
print("A: Tar med teamet på en sosial aktivitet")
print("B: Fokuserer bare på å bli ferdig")
valg3 = input("Skriv A eller B: ").upper()

while valg3 != "A" and valg3 != "B":
    valg3 = input("Ugyldig valg, skriv A eller B: ").upper()

if valg3 == "A":
    print("Dere drar på bowling og folk får det bedre sammen.")
    poeng = poeng + 2
else:
    print("Alle jobber hardt, men hver for seg.")
    poeng = poeng + 1
print()

# Slutten - avhenger av poengene
print("Du fikk", poeng, "av 6 poeng.")

if poeng >= 5:
    print("Teamet går videre til norming-fasen og prototypen blir levert i tide!")
elif poeng >= 3:
    print("Konflikten er delvis løst, men samarbeidet er fortsatt skjørt.")
else:
    print("Teamet mister samholdet og prosjektet blir forsinket.")