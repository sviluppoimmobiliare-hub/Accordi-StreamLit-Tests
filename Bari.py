import streamlit as st


zone_bari = {
    "ZONA 1": "CITTA' VECCHIA",
    "ZONA 2": "MURAT",
    "ZONA 3": "LIBERTA'",
    "ZONA 4": "MADONNELLA",
    "ZONA 5": "JAPIGIA E SANT'ANNA",
    "ZONA 6": "SAN PAOLO",
    "ZONA 7": "STANIC",
    "ZONA 8": "SAN GIROLAMO - FESCA",
    "ZONA 9": "TORRE A MARE SAN GIORGIO",
    "ZONA 10": "CARRASSI - SAN PASQUALE",
    "ZONA 11": "POGGIOFRANCO - PICONE",
    "ZONA 12": "CARBONARA - CEGLIE - LOSETO",
    "ZONA 13": "SANTO SPIRITO - PALESE"
}

caratteristiche_comuni = [
    "Appartamenti dal 1º piano fuori terra",
    "Ingresso alloggio da piazza o da mare",
    "Balcone con vista su piazza o mare",
    "Allacciamento gas metano",
    "Impianto di condizionamento",
    "Secondo servizio igienico",
    "Spazi esterni ad uso esclusivo e/o condominiale",
    "Porta blindata",
    "Cantina o soffitta o giardino privato o terrazza a livello",
    "Posto auto di pertinenza e/o condominiale assegnato",
    "Box auto",
    "Ascensore",
    "Portierato",
    "Videosorveglianza condominiale o individuale",
    "Impianto fotovoltaico o pannelli solari produzione acqua calda",
    "Impianto citofono",
    "Impianto di videocitofono",
    "Impianto di autoclave",
    "Impianto elettrico interno adeguato ai sensi del D.M. 37/2008",
    "Attico",
    "Ripostiglio",
    "Parquet",
    "Postazione di ricarica veicoli elettrici nel box/posto auto o antenna satellitare",
    "Cucina abitabile di almeno 9 mq. con finestra",
    "Sistemi di sicurezza allarme",
    "Sistemi di domotica in almeno il 50% dell'unità immobiliare",
    "Riscaldamento autonomo o centralizzato o pompa di calore",
    "Infissi interni ed esterni in buono stato",
    "Cassaforte",
    "Doppio ingresso o cortile/giardino recintato"
]

lista_zone = list(zone_bari.values())
zona = st.selectbox("Selezionare la zona", lista_zone)
st.subheader("Superficie convenzionale")
superficie_utile = st.number_input("Superficie utile calpestabile in mq (non catastale)", min_value=0.0)
superficie_vani_bassi = st.number_input("Di cui vani con altezza inferiore a 170 cm (conteggiati al 50%)", min_value=0.0)
superficie_autorimessa = st.number_input("Autorimessa singola ad uso esclusivo in mq (conteggiata al 50%)", min_value=0.0)
superficie_posto_auto = st.number_input("Posto auto ad uso esclusivo in mq (conteggiato al 25%)", min_value=0.0)
superficie_accessori = st.number_input("Balconi, terrazze, cortili, cantine, soffitte e accessori simili in mq (conteggiati al 25%)", min_value=0.0)
superficie_scoperta = st.number_input("Superficie scoperta ad uso esclusivo del conduttore in mq (conteggiata al 15%)", min_value=0.0)
superficie_verde = st.number_input("Superficie a verde per quota millesimale in mq (conteggiata al 10%)", min_value=0.0)

superficie_convenzionale = (superficie_utile - superficie_vani_bassi * 0.50 +
                            superficie_autorimessa * 0.50 +
                            superficie_posto_auto * 0.25 +
                            superficie_accessori * 0.25 +
                            superficie_scoperta * 0.15 +
                            superficie_verde * 0.10)


if superficie_convenzionale > 130:
    superficie_convenzionale = 130 + (superficie_convenzionale - 130) * 0.50


superficie_calcolo = superficie_convenzionale
if superficie_convenzionale <= 45:
    superficie_calcolo = min(superficie_convenzionale * 1.20, 45.0)
elif superficie_convenzionale <= 70:
    superficie_calcolo = min(superficie_convenzionale * 1.20, 70.0)

st.info(f"Superficie convenzionale: {superficie_convenzionale:.2f} mq - Superficie di calcolo: {superficie_calcolo:.2f} mq")
st.caption("È ammessa una tolleranza del 4% in più o in meno sulla superficie convenzionale")

st.subheader("Contratto e classe energetica")
tipo_contratto = st.selectbox("Tipo di contratto", ["Agevolato (3+2)", "Transitorio ordinario", "Transitorio per studenti universitari"])

maggiorazione_durata = 0.0
if tipo_contratto == "Agevolato (3+2)":
    durata_contratto = st.selectbox("Durata del contratto",
                                    ["3 anni", "4 anni (+5%)", "5 anni (+7%)", "6 anni o superiore (+12%)"])
    if durata_contratto == "4 anni (+5%)":
        maggiorazione_durata = 0.05
    elif durata_contratto == "5 anni (+7%)":
        maggiorazione_durata = 0.07
    elif durata_contratto == "6 anni o superiore (+12%)":
        maggiorazione_durata = 0.12

classe_energetica = st.selectbox("Classe energetica",
                                 ["G o non dichiarata", "A (A4-A3-A2-A1) (+5%)", "B (+3%)", "C (+3%)", "D (+3%)", "E (+3%)", "F (+3%)"])
incremento_energetico = 0.0
if classe_energetica == "A (A4-A3-A2-A1) (+5%)":
    incremento_energetico = 0.05
elif classe_energetica != "G o non dichiarata":
    incremento_energetico = 0.03

st.subheader("Selezionare le caratteristiche")
valori_checkbox = {}

for elemento in caratteristiche_comuni:
    valori_checkbox[elemento] = st.checkbox(label=elemento, value=False)

counter = list(valori_checkbox.values()).count(True)

st.subheader("Arredamento (allegato 3)")

arredi_comuni = [
    "Cucina: pensili a muro oppure credenza",
    "Cucina: frigorifero",
    "Cucina: cucina (elettrodomestico autonomo a norma)",
    "Cucina: tavolo con sedie",
    "Cucina: scolapiatti e stoviglie",
    "Camera da letto: letto con materasso",
    "Camera da letto: comodino",
    "Camera da letto: armadio e/o guardaroba",
    "Camera da letto: sedia",
    "Soggiorno - tinello: tavolo con sedie",
    "Soggiorno - tinello: vetrinetta o mobiletto",
    "Bagno arredato (mensole, specchio)"
]

arredi_studenti = [
    "Camera - studio: scrivania con sedia",
    "Camera - studio: libreria"
]


lista_arredi = arredi_comuni
if tipo_contratto == "Transitorio per studenti universitari":
    lista_arredi = arredi_comuni + arredi_studenti

valori_arredi = {}
for arredo in lista_arredi:
    valori_arredi[arredo] = st.checkbox(label=arredo, value=False)

illuminazione = st.checkbox("Tutte le camere hanno idonea illuminazione elettrica")

counter_arredi = list(valori_arredi.values()).count(True)


parzialmente_ammobiliato = False
totalmente_ammobiliato = False
if counter_arredi == len(lista_arredi) and illuminazione:
    totalmente_ammobiliato = True
elif counter_arredi > 0:
    parzialmente_ammobiliato = True

if totalmente_ammobiliato:
    st.info("Immobile totalmente ammobiliato")
elif parzialmente_ammobiliato:
    st.info("Immobile parzialmente ammobiliato")
else:
    st.info("Immobile non ammobiliato")


can_min = 0.0
can_max = 0.0
fascia_finale = ""

if zona == "CITTA' VECCHIA":
    zona_pregio = st.checkbox("Zona di Pregio",
                              help="gli immobili con balcone su mare o su Piazza Mercantile – Piazza Ferrarese – Piazza Massari – Via Venezia")
    requisiti_pregio = (zona_pregio and valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and  valori_checkbox["Impianto elettrico interno adeguato ai sensi del D.M. 37/2008"])

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:
        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""
        if counter > 5 or requisiti_pregio:
            fascia_nativa = "A"
        elif counter > 3:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 6.37
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.26, 6.37

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.26, 6.37 * 1.10

            else:
                if fascia_nativa == "B":
                    can_min, can_max = 4.38, 5.25
                else:
                    can_min, can_max = 2.18, 4.37

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "MURAT":
    zona_pregio = st.checkbox(
        "Zona di Pregio",
        help="Immobili con balcone e ingresso su via Sparano, C.so V. Emanuele, C.so Cavour, piazza Garibaldi, Piazza Umberto, piazza Moro"
    )
    piano_oltre_secondo = st.checkbox("L'immobile è situato oltre il 2° piano?",
                                      help="Rilevante per la Zona di Pregio: l'ascensore è richiesto solo dopo il 2° piano")
    buone_condizioni = st.checkbox("Condizioni generali dell'appartamento e dello stabile buone",
                                   help="Rilevante per la Zona di Pregio")

    requisito_ascensore = valori_checkbox["Ascensore"] or not piano_oltre_secondo
    requisiti_pregio = (zona_pregio and valori_checkbox["Impianto di autoclave"] and
                        valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and valori_checkbox[
                            "Impianto elettrico interno adeguato ai sensi del D.M. 37/2008"] and
                        requisito_ascensore and buone_condizioni)

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if requisiti_pregio:
            fascia_nativa = "A"
        elif counter > 7:
            fascia_nativa = "A"

        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 6.63, 8.20
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.63, 8.20

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.63, 8.20 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 5.38, 6.62
                else:  # Fascia C
                    can_min, can_max = 4.76, 5.37

        elif fascia_nativa == "D":
            can_min, can_max = 2.37, 4.75
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "LIBERTA'":

    zona_pregio = st.checkbox(
        "Zona di Pregio",
        help="Zona Executive – zona contrada Barone"
    )

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:
        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )

        fascia_nativa = ""

        if zona_pregio:
            fascia_nativa = "A"
        elif counter > 7:
            fascia_nativa = "A"

        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":
            can_min, can_max = 5.13, 6.06
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:
            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.13, 6.06

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13, 6.06 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.51, 5.12
                else:
                    can_min, can_max = 4.11, 4.50

        elif fascia_nativa == "D":
            can_min, can_max = 3.88, 4.10
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "MADONNELLA":

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )

        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"

        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":
            can_min, can_max = 6.01, 6.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:
            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.01, 6.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.01, 6.50 * 1.10

            else:
                if fascia_nativa == "B":
                    can_min, can_max = 5.31, 6.00
                else:
                    can_min, can_max = 4.41, 5.30

        elif fascia_nativa == "D":

            can_min, can_max = 3.41, 4.40
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "JAPIGIA E SANT'ANNA":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter >= 8:
            fascia_nativa = "A"
        elif counter > 6:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"

        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 6.00
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 6.00

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 6.00 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.81, 5.25
                else:
                    can_min, can_max = 3.51, 4.80

        elif fascia_nativa == "D":

            can_min, can_max = 3.00, 3.50
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")
if zona == "SAN PAOLO":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter > 6:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 4.94, 5.18
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 4.94, 5.18

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 4.94, 5.18 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.57, 4.93
                else:
                    can_min, can_max = 4.32, 4.56

        elif fascia_nativa == "D":

            can_min, can_max = 2.16, 4.31
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")
if zona == "STANIC":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.19, 5.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.19, 5.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.19, 5.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.91, 5.18
                else:
                    can_min, can_max = 4.31, 4.90

        elif fascia_nativa == "D":

            can_min, can_max = 2.16, 4.30
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")
if zona == "SAN GIROLAMO - FESCA":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.13, 6.00
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13, 6.00

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13, 6.00 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.51, 5.12
                else:
                    can_min, can_max = 3.88, 4.50

        elif fascia_nativa == "D":

            can_min, can_max = 1.93, 3.87
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "TORRE A MARE SAN GIORGIO":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.51, 5.90
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.51, 5.90

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.51, 5.90 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.71, 5.50
                else:  # Fascia C
                    can_min, can_max = 3.70, 4.70


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "CARRASSI - SAN PASQUALE":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:  #
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 7.01, 7.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 7.01, 7.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 7.01, 7.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 6.01, 7.00
                else:  # Fascia C
                    can_min, can_max = 5.50, 6.00


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "POGGIOFRANCO - PICONE":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 6.88, 7.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.88, 7.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.88, 7.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 6.26, 6.87
                else:
                    can_min, can_max = 5.61, 6.25

        elif fascia_nativa == "D":


            can_min, can_max = 5.00, 5.60
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

if zona == "CARBONARA - CEGLIE - LOSETO":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 5.70
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 5.70

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 5.70 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.88, 5.25
                else:
                    can_min, can_max = 4.13, 4.87

        elif fascia_nativa == "D":


            can_min, can_max = 2.06, 4.12
            if parzialmente_ammobiliato or totalmente_ammobiliato:
                st.info("Nota: in fascia D l'accordo non prevede variazioni del canone per l'arredamento")


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")
if zona == "SANTO SPIRITO - PALESE":


    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.69, 6.12
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.69, 6.12

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.69, 6.12 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 5.13, 5.68
                else:
                    can_min, can_max = 2.56, 5.12


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} euro/mq - Canone Massimo: {can_max:.2f} euro/mq")

stima = st.button("Stima canone")
if stima:
    if superficie_calcolo <= 0:
        st.warning("Inserire la superficie dell'immobile prima di stimare il canone")
    elif can_min <= 0:
        st.warning("Completare correttamente la selezione delle caratteristiche prima di stimare il canone")
    else:

        can_mq_minimo = can_min * (1 + incremento_energetico) * (1 + maggiorazione_durata)
        can_mq_massimo = can_max * (1 + incremento_energetico) * (1 + maggiorazione_durata)
        can_finale_minimo = round(can_mq_minimo * superficie_calcolo, 2)
        can_finale_massimo = round(can_mq_massimo * superficie_calcolo, 2)
        st.success(f"Range stimato: minimo ->{can_finale_minimo} euro , massimo ->{can_finale_massimo} euro ")
