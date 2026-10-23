print("Erling leder et prosjekt for å utvikle en digital medborgerportal.")
print("Teamet har konflikter, og den første prototypen skal være klar om tre uker.")
print("Du spiller rollen som Erling. Valgene dine påvirker prosjektets utvikling.")
print("Beslutningspunkt 1: Silje ønsker et kreativt design, mens Elias prioriterer sikkerhet og kostnader.")
print("A: Erling holder en papirtest. Silje tegner forsiden, Elias markerer det som er dyrt eller usikkert, og brukerrepresentantene prøver å finne fram på skissen.")
print("B: Erling ber Elias lete etter sikkerhetshull i en prototype med falske data. Silje får bare legge til funksjoner som består testen.")
valg1 = input("Velg A eller B: ").upper()
if valg1 == "A":
   print("Papirtesten viser at brukerne ikke finner søknadsskjemaet. Silje må flytte det før Elias sjekker sikkerheten.")
elif valg1 == "B":
    print("Sikkerhetstesten finner en svakhet i en ny funksjon. Erling setter den på pause, så Elias kan sikre løsningen først.")
print("Beslutningspunkt 2: Hamdi vil bruke kommunens plattform, mens Hallgeir ønsker en mer åpen løsning for innbyggerne.")
print("A: Erling ber Hamdi lage en prototype på kommunens plattform, mens Hallgeir lager en prototype på en åpen plattform. Brukerne tester begge prototypene.")
print("B: Erling velger Hallgeirs åpne løsning og ber Hamdi undersøke om den kan kobles trygt til kommunens system.")
valg2 = input("Velg A eller B: ").upper()
if valg2 == "A":
    print("Tester begge prototypene. Brukerne har mer positive erfaringer med den åpne plattformen.")
elif valg2 == "B": 
    print("Hamdi finner at koblingen tar mer tid enn planlagt, så Erling må kutte noen funksjoner for å rekke prototypen.")
print("Beslutningspunkt 3: Prototypen skal være klar om tre uker.")
print("A: Erling ber teamet prioritere de viktigste funksjonene og kutte mindre viktige funksjoner.")
print("B: Erling ber teamet jobbe overtid for å få med alle funksjonene før fristen.")
valg3 = input("Velg A eller B: ").upper()
if valg3 == "A":
    print("Teamet klarer å levere en fungerende prototype med de viktigste funksjonene innen fristen.")
elif valg3 == "B":
    print("Teamet får med flere funksjoner, men rekker ikke å teste dem godt nok før fristen.")
print("Sluttutfall:")

if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("Teamet leverer en enkel prototype i tide. Brukernes tilbakemeldinger har forbedret løsningen, og teamet har et bedre grunnlag for å samarbeide videre.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Teamet får med mange funksjoner, men sikkerhetsproblemer, forsinkelser og lite testing gjør prototypen utrygg. Motivasjonen i teamet faller.")
else:
    print("Teamet løser noen problemer, men ikke alle. De leverer en begrenset prototype og må fortsette å jobbe med sikkerhet, testing og samarbeid.")