print("Erling er teamleder for et prosjektteam som trenger litt veiledning med å håndtere konflikter og motivasjon. Han har tre situasjoner han må ta stilling til. " \
"\nNå skal du spille rollen som Erling og ta beslutninger for å håndtere situasjonene. Svar på spørsmålene ved å velge A eller B.")

while True:
    valg1 = input("Hvordan skal Erling håndtere situasjonen mellom Silje og Elias? " \
    "\nA = Ta det opp i plenum for å skape åpenhet "  \
    "" \
    "\nB = Begge får en tidsfrist til å lage en prototype "  \
    "\nSvar A eller B: ").strip().upper()


    if valg1 == "A":
        print("Erling tar det opp i plenum for å skape åpenhet.")
        break
    elif valg1 == "B":
        print("Erling gir begge en tidsfrist til å lage en prototype.") 
        break
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")

while True:
    valg2 = input("Hvordan forhindre at situasjonen mellom Hamdi og Hallgeir eskalerer? " \
"\nA = Ta initiativ til et felles møte for å avklare uenigheter " \
"\nB = Gi de en tidsfrist til å komme med et forslag hvor de jobber sammen som et par " \
"\nSvar A eller B: ").strip().upper()


    if valg2 == "A":
        print("Erling tar initiativ til et felles møte for å avklare uenigheter.")
        break
    elif valg2 == "B":
        print("Erling gir de en tidsfrist til å komme med et forslag hvor de jobber sammen som et par.")
        break
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")

while True:
    valg3 = input("Hvordan bevare motivasjonen i teamet som helhet? " \
"\nA = Skal han sette av tid til relasjonsbygging og sosiale aktiviteter for å " \
"gjenopprette tillit? " \
"\nB = Lage mål teamet kan oppnå rettet mot sluttproduktet, men fokusere mer på oppgavene enn teamet. " \
"\nSvar A eller B: ").strip().upper()


    if valg3 == "A":
        print("Erling setter av tid til relasjonsbygging og sosiale aktiviteter for å gjenopprette tillit.")
        break
    elif valg3 == "B":
        print("Erling lager mål teamet kan oppnå rettet mot sluttproduktet.")
        break
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")


alle_valg = [valg1, valg2, valg3]
antall_a = alle_valg.count("A")

if antall_a >= 2:
    print("Erling har valgt A i minst to av situasjonene, teamet jobbet seg gjennom konfliktene og går videre til norming fasen.")
elif antall_a == 1:
    print("Erling har valgt A i en av situsjonene, konfliktene er løst, men teamet har fortsatt noen sårbare relasjoner som bør jobbes med.") 
else:
    print("Erling har valgt B i alle situasjonene, teamet mister derfor samholdet og prosjektet blir forsinket.")