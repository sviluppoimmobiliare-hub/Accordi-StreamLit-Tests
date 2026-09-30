import streamlit as st

st.title("Calcolatore Canone Concordato - Comune di Firenze")


dettaglio_zone = {
    "Centro Storico": "CENTRO",
    "Lungarno": "CENTRO",
    "Piazza Ferrucci": "CENTRO",
    "Bobolino": "DI PREGIO",
    "Due Strade": "DI PREGIO",
    "Marignolle": "DI PREGIO",
    "La Pietra": "DI PREGIO",
    "Careggi": "DI PREGIO",
    "Settignano": "DI PREGIO",
    "Poggetto": "INTERMEDIA A",
    "Cure": "INTERMEDIA A",
    "Campo di Marte": "INTERMEDIA A",
    "Madonnone/Bellariva": "INTERMEDIA A",
    "Bandino": "INTERMEDIA A",
    "Nave a Rovezzano": "INTERMEDIA A",
    "Novoli": "INTERMEDIA A",
    "Coverciano": "INTERMEDIA A",
    "Varlungo": "INTERMEDIA A",
    "San Jacopino": "INTERMEDIA B",
    "Dalmazia": "INTERMEDIA B",
    "Cascine del Riccio": "INTERMEDIA B",
    "Galluzzo": "INTERMEDIA B",
    "Legnaia": "PERIFERICA A",
    "Isolotto": "PERIFERICA A",
    "Argingrosso": "PERIFERICA A",
    "Castello": "PERIFERICA A",
    "Piagge": "PERIFERICA B",
    "Peretola": "PERIFERICA B",
    "Mantignano": "PERIFERICA B",
    "Cupolina": "PERIFERICA B"
}

microzone_map = {
    "CENTRO": "1-2-3",
    "DI PREGIO": "4-5-6-12-25-30",
    "INTERMEDIA A": "11-13-14-15-16-17-23-26-27",
    "INTERMEDIA B": "9-10-18-19",
    "PERIFERICA A": "7-8-20-24",
    "PERIFERICA B": "21-22-28-29"
}

nome_quartiere = st.selectbox("Selezionare il quartiere / zona", list(dettaglio_zone.keys()))
zona = dettaglio_zone[nome_quartiere] 

st.caption(f"**Classificazione assegnata:** {zona} (Microzone associate: {microzone_map[zona]})")

fasce_firenze = {
    "CENTRO":       {"A": (2.00, 13.00), "B": (2.00, 11.00), "C": (2.00, 7.00)},
    "DI PREGIO":    {"A": (2.00, 13.50), "B": (2.00, 12.00), "C": (2.00, 7.50)},
    "INTERMEDIA A": {"A": (2.00, 10.20), "B": (2.00, 9.00),  "C": (2.00, 5.50)},
    "INTERMEDIA B": {"A": (2.00, 9.70),  "B": (2.00, 8.70),  "C": (2.00, 5.50)},
    "PERIFERICA A": {"A": (2.00, 9.20),  "B": (2.00, 8.30),  "C": (2.00, 5.50)},
    "PERIFERICA B": {"A": (2.00, 8.75),  "B": (2.00, 8.10),  "C": (2.00, 5.00)}
}


caratteristiche_tipologia_B = [
    "a - Riscaldamento completo di elementi radianti e/o sistemi alternativi, efficiente ed a norma",
    "b - Servizio igienico principale con almeno quattro apparecchi, fornito di finestra o areazione forzata",
    "c - Impianto idrico idoneo ed efficiente",
    "d - Impianto elettrico a norma, consentito dalle vigenti norme",
    "e - Ascensore per unità immobiliari poste oltre il terzo piano fuori terra",
    "f - Infissi ed affissi efficienti con chiusura atta a garantire la tenuta agli agenti atmosferici",
    "g - Citofono con apri porta efficiente"
]

non_determinanti = [caratteristiche_tipologia_B[4], caratteristiche_tipologia_B[6]]

elementi_tipologia_A = [
    "1 - Apparecchi di condizionamento d'aria nell'unità immobiliare (non richiesto se immobile vincolato o cat. A/8, A/9)",
    "2 - Rifiniture di particolare pregio",
    "3 - Doppi servizi igienici (secondo servizio con almeno 3 apparecchi se sup. > 80 mq; servizio finestrato se sup. < 80 mq)",
    "4 - Spazi per uso parcheggio con effettiva disponibilità, assegnati catastalmente o da regolamento condominiale",
    "5 - Spazi esterni ad uso esclusivo di metratura pari almeno ad 1/3 della superficie calpestabile",
    "6 - Sistema di allarme e/o sistemi di anti effrazione quali inferriate",
    "7 - Servizio di portierato o impianto di videosorveglianza",
    "8 - Sistema di connessione internet in fibra ottica di tipo FTTH",
    "9 - Portone o portoncino blindato",
    "10 - Ascensore per unità immobiliari poste oltre il secondo piano",
    "11 - Spazi verdi condominiali",
    "12 - Impianto fotovoltaico e/o solare termico"
]

st.subheader("Superficie convenzionale (Art. 6)")
sup_A = st.number_input("A - Superficie interna utile abitativa calpestabile in mq (escluse mura e aree con altezza inferiore a 240 cm)", min_value=0.0)
sup_A1 = st.number_input("A1 - Superficie delle aree interne con altezza compresa fra 180 e 240 cm (conteggiata al 30%)", min_value=0.0)
sup_B = st.number_input("B - Superficie utile delle autorimesse singole o box auto (conteggiata al 50%)", min_value=0.0)
sup_C = st.number_input("C - Superficie dei lastrici solari di uso esclusivo al piano attico (25% fino ai mq calpestabili, 5% sull'eccedenza)", min_value=0.0)
sup_D = st.number_input("D - Superficie dei posti auto coperti o scoperti in area di proprietà esclusiva del locatore (conteggiata al 30%)", min_value=0.0)
sup_E = st.number_input("E - Superficie del posto auto in autorimesse comuni coperte, delimitato ed assegnato senza identificativo catastale (conteggiata al 25%)", min_value=0.0)
sup_F = st.number_input("F - Superficie utile del posto auto in spazi comuni scoperti, delimitato ed assegnato senza identificativo catastale (conteggiata al 20%)", min_value=0.0)
sup_G = st.number_input("G - Superficie utile del posto auto in spazi comuni scoperti con rotazione turnaria (conteggiata al 5%)", min_value=0.0)
sup_H = st.number_input("H - Superficie utile di balconi, terrazze, lastrici solari non all'attico, cantine (conteggiata al 25%)", min_value=0.0)
sup_I = st.number_input("I - Superficie scoperta (corti, giardini ecc.) di pertinenza in godimento esclusivo (10% fino ai mq calpestabili, 2% sull'eccedenza)", min_value=0.0)

if sup_C <= sup_A:
    quota_C = sup_C * 0.25
else:
    quota_C = sup_A * 0.25 + (sup_C - sup_A) * 0.05

if sup_I <= sup_A:
    quota_I = sup_I * 0.10
else:
    quota_I = sup_A * 0.10 + (sup_I - sup_A) * 0.02

superficie_convenzionale = (sup_A + sup_A1 * 0.30 + sup_B * 0.50 + quota_C + sup_D * 0.30 +
                            sup_E * 0.25 + sup_F * 0.20 + sup_G * 0.05 + sup_H * 0.25 + quota_I)

applica_incremento_piccole = False
if 0 < sup_A <= 65:
    applica_incremento_piccole = st.checkbox(
        "Applicare l'incremento per piccole superfici (Art. 6)",
        value=True,
        help="Facolta' prevista dall'Accordo (la superficie potra' essere incrementata, non e' un obbligo): "
             "+20% fino a 63 mq se il calpestabile e' fino a 60 mq, +5% fino a 65 mq se il calpestabile e' tra 60 e 65 mq"
    )

if applica_incremento_piccole:
    if 0 < sup_A <= 60:
        superficie_convenzionale = max(superficie_convenzionale, min(superficie_convenzionale * 1.20, 63.00))
    elif 60 < sup_A <= 65:
        superficie_convenzionale = max(superficie_convenzionale, min(superficie_convenzionale * 1.05, 65.00))

st.info(f"Superficie convenzionale: {superficie_convenzionale:.2f} mq")

st.subheader("Selezionare le caratteristiche dell'immobile (Tipologia B)")
valori_checkbox_B = {}

for elemento in caratteristiche_tipologia_B:
    valori_checkbox_B[elemento] = st.checkbox(label=elemento, value=False)

counter_B = list(valori_checkbox_B.values()).count(True)

st.subheader("Requisiti Tipologia A ")
nuovo_o_ristrutturato = st.checkbox(
    "Immobile costruito o oggetto di ristrutturazione e/o risanamento ultimati entro gli ultimi 10 anni, con i requisiti dell'Art. 8 lett. a)",
    help="Interventi che abbiano coinvolto in toto gli impianti elettrico, idrico e sanitario, con sostituzione degli infissi esterni e APE migliorativo. "
         "L'unità deve inoltre possedere: riscaldamento efficiente a norma con caldaia di vetustà non superiore a 10 anni, servizio igienico principale con almeno 4 apparecchi "
         "finestrato o con areazione forzata, impianto idrico idoneo, impianto elettrico post L. 46/90 certificato, ascensore oltre il 2° piano, ambienti a norma, "
         "infissi efficienti, citofono con apri porta, condizionamento diffuso in tutti i locali, rifiniture di buona fattura, doppi servizi se superficie >= 80 mq"
)

st.markdown("Elementi aggiuntivi (almeno **6**, uniti ai requisiti della Tipologia B, classificano l'alloggio in Tipologia A):")
valori_checkbox_A = {}

for elemento in elementi_tipologia_A:
    valori_checkbox_A[elemento] = st.checkbox(label=elemento, value=False)

immobile_vincolato = st.checkbox(
    "Immobile vincolato o di categoria catastale A/8 o A/9",
    help="Per questi immobili il condizionamento d'aria (elemento 1) non e' richiesto e viene considerato "
         "automaticamente presente ai fini del conteggio dei 6 elementi"
)

counter_A = list(valori_checkbox_A.values()).count(True)

if immobile_vincolato and not valori_checkbox_A[elementi_tipologia_A[0]]:
    counter_A += 1

mancanti_determinanti = 0
for elemento in caratteristiche_tipologia_B:
    if elemento not in non_determinanti and not valori_checkbox_B[elemento]:
        mancanti_determinanti += 1

if counter_B >= 6:
    tipologia_base = "B"
elif mancanti_determinanti < 2:
    tipologia_base = "B"
else:
    tipologia_base = "C"

tipologia = tipologia_base
if nuovo_o_ristrutturato:
    tipologia = "A"
elif tipologia_base == "B" and counter_A >= 6:
    tipologia = "A"

st.subheader("Maggiorazioni")

arredamento = st.radio(
    "Immobile arredato (Art. 9, punto 1)",
    ["Non arredato",
     "Arredato per 1/2 dei vani locati (max +7%)",
     "Arredato per 3/4 dei vani locati (max +10%)",
     "Completamente arredato (max +15%)"],
    help="L'arredo deve essere funzionale ed efficiente; per la maggiorazione massima e' "
         "indispensabile arredo idoneo per ogni vano utile locato. Le percentuali sono tetti massimi "
         "entro cui le parti concordano l'incremento effettivo"
)

tetti_arredo = {
    "Non arredato": 0.0,
    "Arredato per 1/2 dei vani locati (max +7%)": 7.0,
    "Arredato per 3/4 dei vani locati (max +10%)": 10.0,
    "Completamente arredato (max +15%)": 15.0
}
tetto_arredo = tetti_arredo[arredamento]

perc_arredo = 0.0
if tetto_arredo > 0:
    perc_arredo = st.slider(
        "Percentuale di maggiorazione per arredo concordata tra le parti (%)",
        min_value=0.0, max_value=tetto_arredo, value=tetto_arredo, step=0.5
    )

pregio_431 = st.checkbox(
    "Immobile di particolare pregio ex art. 1, comma 2, lett. a) L. 431/98 (+15% sulle fasce)",
    help="Immobili vincolati o di categoria catastale A/1, A/8, A/9 (Art. 9, punto 2)"
)
categoria_A7 = st.checkbox(
    "Immobile di categoria catastale A/7 (+10% sulle fasce)",
    help="Art. 9, punto 2"
)

classe_energetica = st.selectbox(
    "Prestazione energetica rilevabile dal certificato APE (Art. 9, punto 3)",
    ["G / F / Non disponibile",
     "E (+2%)",
     "D (+4%)",
     "C (+6%)",
     "B (+8%)",
     "A1 (+10%)",
     "A2 (+12%)",
     "A3 (+14%)",
     "A4 (+15%)"]
)

incrementi_energetici = {
    "G / F / Non disponibile": 1.00,
    "E (+2%)": 1.02,
    "D (+4%)": 1.04,
    "C (+6%)": 1.06,
    "B (+8%)": 1.08,
    "A1 (+10%)": 1.10,
    "A2 (+12%)": 1.12,
    "A3 (+14%)": 1.14,
    "A4 (+15%)": 1.15
}

tipo_contratto = st.selectbox(
    "Tipo e durata del contratto (Artt. 11, 12, 13)",
    ["Agevolato 3+2 anni",
     "Agevolato 4 anni +2 (+4,50%)",
     "Agevolato 5 anni +2 (+6%)",
     "Agevolato 6 o più anni (+7,5%)",
     "Transitorio ordinario (1-18 mesi)",
     "Transitorio per studenti universitari (max +15%)"]
)

perc_studenti = 0.0
if tipo_contratto == "Transitorio per studenti universitari (max +15%)":
    perc_studenti = st.slider(
        "Percentuale di maggiorazione per contratto studenti concordata tra le parti (%)",
        min_value=0.0, max_value=15.0, value=15.0, step=0.5
    )

perc_transitorio_studio = 0.0
if tipo_contratto == "Transitorio ordinario (1-18 mesi)":
    transitorio_studio = st.checkbox(
        "Contratto sottoscritto con la motivazione di cui all'Art. 12, comma 2, lett. a) (max +5% nei valori minimi e massimi)",
        help="Motivi di studio, apprendistato, formazione e aggiornamento professionale: la sussistenza deve essere verificata tramite Attestazione Bilaterale obbligatoria"
    )
    if transitorio_studio:
        perc_transitorio_studio = st.slider(
            "Percentuale di maggiorazione per motivazione di studio concordata tra le parti (%)",
            min_value=0.0, max_value=5.0, value=5.0, step=0.5
        )

can_min = 0.0
can_max = 0.0
calcolo_valido = True

if pregio_431 and categoria_A7:
    calcolo_valido = False
    st.warning("L'immobile non può essere di particolare pregio ex L. 431/98 e di categoria A/7 allo stesso tempo")
else:
    can_min, can_max = fasce_firenze[zona][tipologia]

    moltiplicatori = []

    if pregio_431:
        moltiplicatori.append(1.15)
    elif categoria_A7:
        moltiplicatori.append(1.10)

    if perc_arredo > 0:
        moltiplicatori.append(1 + perc_arredo / 100)

    moltiplicatori.append(incrementi_energetici[classe_energetica])

    if tipo_contratto == "Agevolato 4 anni +2 (+4,50%)":
        moltiplicatori.append(1.045)
    elif tipo_contratto == "Agevolato 5 anni +2 (+6%)":
        moltiplicatori.append(1.06)
    elif tipo_contratto == "Agevolato 6 o più anni (+7,5%)":
        moltiplicatori.append(1.075)

    if perc_studenti > 0:
        moltiplicatori.append(1 + perc_studenti / 100)
    if perc_transitorio_studio > 0:
        moltiplicatori.append(1 + perc_transitorio_studio / 100)

    for moltiplicatore in moltiplicatori:
        can_min *= moltiplicatore
        can_max *= moltiplicatore

    st.success(f"Assegnata: TIPOLOGIA {tipologia}")
    st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

stima = st.button("Stima canone")
if stima:
    if not calcolo_valido:
        st.warning("Correggere le selezioni incompatibili (immobile di pregio ex L. 431/98 e categoria A/7) prima di stimare il canone")
    else:
        can_finale_minimo = round(can_min * superficie_convenzionale, 2)
        can_finale_massimo = round(can_max * superficie_convenzionale, 2)
        st.success(f"Range stimato: minimo ->{can_finale_minimo} euro/mese , massimo ->{can_finale_massimo} euro/mese ")

