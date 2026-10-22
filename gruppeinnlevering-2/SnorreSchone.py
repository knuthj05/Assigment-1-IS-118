
import time

#Globale variabler for å spare konsekvensene av Erlings valg
status = {
    "team_tillit": 50,  # Starter på 50%
    "fremdrift": 50,    # Starter på 50%
    "risiko": 30        # Starter på 30%

}

def tekst_sakte(tekst):
    """Gir spillet en mer interaktiv følelse i terminalen."""
    print(tekst)
    time.sleep(1.5)


def vis_status():
    print(
        f"\nStatus -> Tillit: {status['team_tillit']}% | "
        f"Fremdrift: {status['fremdrift']}% | Risiko: {status['risiko']}%\n"
    )


#=====================================================
# Introduksjon
#=====================================================
def start_spill():
    print("\n=================================================")
    print("LEDERUTFORDRINGER: PROSJEKT MEDBORGERPORTAL.")
    print("=================================================")
    tekst_sakte("Det har gått seks uker siden du, Erling, samlet prosjektteamet ditt.")
    tekst_sakte("Etter en god oppstart har dere nå dundret inn i 'storming-fasen'.")
    tekst_sakte("Første prototype skal være klar om bare TRE UKER, og stemningen er spent.")

    vis_status()
    utfordring_1()


#===========================================
# UTFORDRING 1: Silje (UX) vs. Elias (IT)
#===========================================

def utfordring_1():
    print("\n--- UTFORDRING 1: PERSONKONFLIKT mellom Silje og Elias ---")
    tekst_sakte("Silje (UX) mener elias' teknologivalg låser brukeropplevelsen.")
    tekst_sakte("Elias mener Siljes design er urealistisk, usikkert og altfor dyrt.")
    tekst_sakte("Diskusjonene har blitt personlige. Hva gjør du som prosjektleder?")

    print("\n1. Ta det opp i plenum neste fellesmøte for å skape full åpenhet.")
    print("2. Kall inn Silje og Elias til individuelle samtaler på tomannshånd.")
    print("3. Koble inn HR med en gang for å sikre en nøytral og formell håndtering.")

    valg = input("Ditt valg (1/2/3): ").strip()

    if valg == "1":
        print("\nKONSEKVENS:")
        tekst_sakte("Å ta det i plenum gjorde vondt verre! Diskusjonen eskalerte foran alle.")
        tekst_sakte("Silje følte seg angrepet, og Elias låste seg helt fast.")
        status["team_tillit"] -= 20
        status["risiko"] += 25
        status["fremdrift"] -= 10
    elif valg == "2":
        print("\nKONSEKVENS:")
        tekst_sakte("De individuelle samtalene dempet temperaturen betraktelig.")
        tekst_sakte("Både Silje og Elias følte seg hørt av deg, og dere fant et kompromiss.")
        status["team_tillit"] += 15
        status["risiko"] -= 15
        status["fremdrift"] += 10
    elif valg == "3":
        print("\nKONSEKVENS:")
        tekst_sakte("HR profesjonaliserte prosessen, men teamet føler nå at situasjonen er 'krise'.")
        tekst_sakte("Det formelle oppsettet stjal verdifull tid fra utviklingen.")
        status["team_tillit"] -= 5
        status["risiko"] -= 20
        status["fremdrift"] -= 10
    else:
        print("\nUgyldig valg. du unngår situasjonen, noe som øker frustrasjonen.")
        status["risiko"] += 15

    vis_status()
    utfordring_2()


#=======================================================
# UTFORDRING 2: Den ulmende saken (Hamdi vs. Hallgeir)
#=======================================================
def utfordring_2():
    print("\n--- UTFORDRING 2: DEN ULMENDE SAKEN mellom Hamdi og Hallgeir ---")
    tekst_sakte("Hamdi (kultur) vil ha en kontrollert løsning for digitale folkemøter.")
    tekst_sakte("Hallgeir (brukerrepresentant) krever et helt åpent og spontant system.")
    tekst_sakte("Uenigheten er foreløpig lavmælt, men du merker at det ulmer. Hva gjør du?")

    print("\n1. Ta initiativ til et eget fellesmøte mellom dem for å avklare rammene nå.")
    print("2. Avvent situasjonen. Du har dårlig tid, og håper de finner ut av det selv.")

    valg = input("Ditt valg (1/2): ").strip()

    if valg == "1":
        print("\nKONSEKVENS:")
        tekst_sakte("Fellesmøtet tok brodden av konflikten før den rakk å bli personlig.")
        tekst_sakte("Hallgeir fikk gjennomslag for noe spontanitet mot at Hamdi fikk sikkerhetskontroll.")
        status["team_tillit"] += 10
        status["risiko"] -= 15
        status["fremdrift"] += 5
    elif valg == "2":
        print("\nKONSEKVENS:")
        tekst_sakte("Dårlig idé. Fordi du ikke tok tak i det, eksploderte uenigheten i lunsjen.")
        tekst_sakte("Hallgeir truer nå med å trekke innbyggerforeningen ut av hele prosjektet.")
        status["team_tillit"] -= 15
        status["risiko"] += 30
        status["fremdrift"] -= 15
    else:
        print("\nDu tok ikke et valg. saken ulmer videre.")
        status["risiko"] += 10

    vis_status()
    utfordring_3()

#==============================================================
# UTFORDRING 3: Motivasjon og veien videre
#==============================================================
def utfordring_3():
    print("\n--- UTFORDRING 3: TEAMETS MOTIVASJON OG MILEPÆLEN ---")
    tekst_sakte("Det er én uke igjen til den store prototype-leveransen.")
    tekst_sakte("Teamet er slitent etter ukene med storming. Hva prioriterer du nå?")

    print("\n1. Arranger en felles middag for å styrke samholdet.")
    print("2. Prioriter intensivt arbeid for å få prototypen ferdig.")
    valg = input("Ditt valg (1/2): ").strip()

    if valg == "1":
        print("\nKONSEKVENS:")
        tekst_sakte("Middagen senket skuldrene til folk. Marcia og Sivert fant tonen over god mat.")
        tekst_sakte("Teamet føler seg mer samlet, men dere mistet verdifulle kodetimer.")
        status["team_tillit"] += 20
        status["fremdrift"] -= 10
    elif valg == "2":
        print("\nKONSEKVENS:")
        tekst_sakte("Dere jobbet på spreng. Koden og designet begynner å falle på plass.")
        tekst_sakte("Men teamet er utbrendt, og folk snakker nesten ikke sammen utenom det faglige.")
        status["fremdrift"] += 25
        status["team_tillit"] -= 15
    else:
        print("\nIngen prioritering ble tatt.")

    avslutning()

#====================================================
# AVSLUTNING OG EVALUERING (basert på poeng)
#====================================================
def avslutning():
    print("\n======================================================================================")
    print("MILEPÆLEN ER NÅDD - EVALUERING AV ERLINGS LEDELSE")
    print("======================================================================================\n")
    time.sleep(1)

    print(
        f"Sluttstatus -> Tillit: {status['team_tillit']}% | "
        f"Fremdrift: {status['fremdrift']}% | Risiko: {status['risiko']}%\n"
    )

    # Utfall 1: Det perfekte teamet (Norming/performing)
    if status["team_tillit"] >= 65 and status["fremdrift"] >= 60 and status["risiko"] < 40:
        print("STRÅLENDE SEIER!")
        print("Erling, du har ledet teamet mesterlig gjennom stormen! Takket være dine grep")
        print("beveger gruppen seg raskt over i 'Norming'-fasen. Silje, Elias, Hamdi og Hallgeir")
        print("har funnet felles kjøreregler, og prototypen ble levert i tide med høy kvalitet.")

    # Utfall 2: Fremdrift på bekostning av menneskene
    elif status["fremdrift"] >= 65 and status["team_tillit"] < 50:
        print("DYREKJØPT SEIER (Resultatfokus)...")
        print("Prototypen ble levert i tide til bystyret og Marcia er fornøyd. Men til hvilken pris?")
        print("Teamet er preget av dype, uløste konflikter. Tilliten til deg og hverandre er tynn.")
        print("Dere risikerer å falle tilbake i en enda dypere storm ved neste korsvei.")

    # Utfall 3: God stemning, men forsinket leveranse
    elif status["team_tillit"] >= 65 and status["fremdrift"] < 60:
        print("GODT SAMHOLD, FORSINKET LEVERANSE...")
        print("Teamet har det hyggelig og spiser lunsj sammen igjen, men dere kom ikke i mål!")
        print("Kommunens IT-avdeling og ledelsen etterspør prototypen som er forsinket.")
        print("Det hjelper lite med god stemning når resultatene uteblir.")

    # Utfall 4: Total kollaps (Sittende fast i stormen)
    elif status["team_tillit"] < 50 and status["fremdrift"] < 50:
        print("TOTAL KOLLAPS I STORMEN...")
        print("Prosjektet har gått helt i stå. Konfliktene eskalerte, tidsfristen sprakk,")
        print("og kommunens nye medborgerportal har blitt en politisk hodepine for Marcia.")
        print("Som leder maktet du ikke å balansere relasjoner og fremdrift. Dere står bom fast.")

    else:
        print("BLANDET RESULTAT...")
        print("Du har gjort fremskritt, men prosjektet har fortsatt utfordringer.")
        print("Teamet må fortsette å jobbe med både samarbeidet og leveransen.")

    print("\n--- TAKK FOR AT DU SPILTE ---")

# Starte spillet
start_spill()
