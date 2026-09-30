import streamlit as st

st.title("Calcolatore Canone Concordato - Comune di Bergamo")


aree_bergamo = {
    "AREA 1 (arancione)": "Papa Giovanni, Stazione, Quarenghi (in parte), Scotti, Tasso, Ghislandi",
    "AREA 2 (verde)": "Citta' Alta e colli, XXIV Maggio, Vittorio Emanuele, Verdi, Pignolo (interamente)",
    "AREA 3 (rosa)": "Stadio, Baioni-Valtesse, Monterosso, parte di Corridoni e S. Caterina",
    "AREA 4 (giallo)": "Longuelo, Loreto, Broseta (in parte), S. Bernardino, Moroni, S. Giovanni Bosco, "
                       "Promessi Sposi, Borgo Palazzo (in parte), Redona",
    "AREA 5 (azzurro)": "Sud della citta' limitrofa a Treviolo, Lallio, Azzano S. Paolo, Orio al Serio"
}

fasce_bergamo = {
    "AREA 1 (arancione)": {1: (48.00, 68.00), 2: (68.01, 110.00), 3: (110.01, 135.00)},
    "AREA 2 (verde)":     {1: (48.00, 68.00), 2: (68.01, 120.00), 3: (120.01, 150.00)},
    "AREA 3 (rosa)":      {1: (43.00, 60.00), 2: (60.01, 100.00), 3: (100.01, 120.00)},
    "AREA 4 (giallo)":    {1: (43.00, 60.00), 2: (60.01, 90.00),  3: (90.01, 115.00)},
    "AREA 5 (azzurro)":   {1: (37.00, 52.00), 2: (52.01, 85.00),  3: (85.01, 105.00)}
}

dotazioni_bergamo = [
    "Autorimessa singola o posto auto coperto o scoperto",                                 # 0
    "Cortile comune",                                                                      # 1
    "Cantina o sottotetto o soffitta",                                                     # 2
    "Impianto di acqua corrente, allacciamento gas ed impianti elettrici efficienti",      # 3
    "Impianto di riscaldamento autonomo o centralizzato",                                  # 4
    "Impianto di riscaldamento autonomo con termoregolazione o di condizionamento",        # 5
    "Ascensore (fabbricato con almeno 3 piani f.t., per unita' oltre il 3 livello)",        # 6
    "Area verde di pertinenza o condominiale, oppure aree attrezzate",                     # 7
    "Impianti o strutture per accesso ai disabili",                                        # 8
    "Ulteriore posto auto o box",                                                          # 9
    "Impianti sportivi di pertinenza dell'immobile",                                        # 10
    "Dotazione di mobilio",                                                                # 11
    "Bagno completo",                                                                       # 12
    "Doppi servizi",                                                                        # 13
    "Porta blindata",                                                                      # 14
    "Doppi vetri",                                                                           # 15
    "Servizio di portineria o impianto di videocitofono",                                   # 16
    "Balconi e/o terrazze di almeno 8 mq",                                                 # 17
    "Unita' ultimata o completamente ristrutturata negli ultimi 10 anni",                  # 18
    "Antenna centralizzata o altro idoneo impianto di rice-trasmissione",                  # 19
    "Vicinanza ai servizi essenziali"                                                      # 20
]

obbligatori_sf3 = [0, 2, 3, 6, 7, 12]   
obbligatori_sf2 = [2, 3, 6, 12]         

lista_aree = list(aree_bergamo.keys())
area = st.selectbox("Selezionare l'area omogenea", lista_aree)
st.caption(aree_bergamo[area])
st.caption("Deroghe: via Pignolo e via T. Tasso sono assegnate interamente all'AREA 2.")

st.subheader("Superficie computabile")
sup_a = st.number_input("a - Locali abitativi, intera superficie (100%) - incl. taverne, mansarde e sottotetti "
                        "abitabili comunicanti, esclusi i muri perimetrali esterni e in comune", min_value=0.0)
sup_b = st.number_input("b - Box e autorimesse / locali per rimesse di veicoli (conteggiati al 70%)", min_value=0.0)
sup_c = st.number_input("c - Posti auto coperti o scoperti (conteggiati al 50%)", min_value=0.0)
sup_d = st.number_input("d - Soffitte, cantine e simili (compresi taverne e mansarde soppalchi sprovvisti di "
                        "abitabilita') COMUNICANTI con i locali abitativi (conteggiati al 50%)", min_value=0.0)
sup_d_bis = st.number_input("d bis - Soffitte, cantine e simili NON comunicanti con i locali abitativi "
                            "(conteggiati al 25%)", min_value=0.0)
sup_e = st.number_input("e - Balconi, terrazze e simili di pertinenza esclusiva COMUNICANTI (30% fino a mq 25, "
                        "10% sulla quota eccedente)", min_value=0.0)
sup_e_bis = st.number_input("e bis - Balconi, terrazze e simili di pertinenza esclusiva NON comunicanti "
                            "(15% fino a mq 25, 5% sulla quota eccedente)", min_value=0.0)
sup_f = st.number_input("f - Area scoperta di pertinenza esclusiva (10% fino alla superficie dei locali abitativi "
                        "di cui al punto a, 2% sulle superfici eccedenti)", min_value=0.0)


if sup_e <= 25:
    quota_e = sup_e * 0.30
else:
    quota_e = 25 * 0.30 + (sup_e - 25) * 0.10

if sup_e_bis <= 25:
    quota_e_bis = sup_e_bis * 0.15
else:
    quota_e_bis = 25 * 0.15 + (sup_e_bis - 25) * 0.05

if sup_f <= sup_a:
    quota_f = sup_f * 0.10
else:
    quota_f = sup_a * 0.10 + (sup_f - sup_a) * 0.02

superficie_computabile = (sup_a + sup_b * 0.70 + sup_c * 0.50 + sup_d * 0.50 +
                          sup_d_bis * 0.25 + quota_e + quota_e_bis + quota_f)

st.info(f"Superficie computabile: {superficie_computabile:.2f} mq  "
        f"(tolleranza +/- 7%: {superficie_computabile * 0.93:.2f} - {superficie_computabile * 1.07:.2f} mq)")

st.subheader("Selezionare le dotazioni dell'immobile (individuazione della sub-fascia)")
valori_dotazioni = []
for elemento in dotazioni_bergamo:
    valori_dotazioni.append(st.checkbox(label=elemento, value=False))


riscaldamento = valori_dotazioni[4] or valori_dotazioni[5]
n_totale = sum(valori_dotazioni)

st.markdown("**Casi particolari (Annotazioni particolari del prospetto):**")
piano_entro_secondo = st.checkbox(
    "Unita' posta ad un piano entro il secondo (escluso piano terra e rialzato): l'ascensore non viene conteggiato",
    help="In tal caso l'elemento ascensore non e' considerato: la sub-fascia 3 richiede 10 elementi (6 obbligatori) "
         "e la sub-fascia 2 richiede 6 elementi (4 obbligatori)."
)
restaurata_borghi = st.checkbox(
    "Unita' restaurata in borgo storico, Citta' Alta o Parco dei Colli (o ricondotta a condizioni simili)",
    help="In tal caso gli elementi indispensabili autorimessa/posto auto, ascensore e verde possono essere "
         "sostituiti da altrettanti elementi opzionali."
)

obl_sf3 = list(obbligatori_sf3)
obl_sf2 = list(obbligatori_sf2)

if piano_entro_secondo:
    if valori_dotazioni[6]:
        n_totale -= 1                      #ascensore non conteggiata
    if 6 in obl_sf3:
        obl_sf3.remove(6)
    if 6 in obl_sf2:
        obl_sf2.remove(6)
    req_sf3_totale, req_sf2_totale = 10, 6
else:
    req_sf3_totale, req_sf2_totale = 11, 7

if restaurata_borghi:
    for i in (0, 6, 7):                     # autorimessa, ascensore, verde 
        if i in obl_sf3:
            obl_sf3.remove(i)
    if 6 in obl_sf2:
        obl_sf2.remove(6)

tutti_obbligatori_sf3 = riscaldamento and all(valori_dotazioni[i] for i in obl_sf3)
tutti_obbligatori_sf2 = riscaldamento and all(valori_dotazioni[i] for i in obl_sf2)

if tutti_obbligatori_sf3 and n_totale >= req_sf3_totale:
    sub_fascia = 3
elif tutti_obbligatori_sf2 and n_totale >= req_sf2_totale:
    sub_fascia = 2
else:
    sub_fascia = 1

st.caption("L'individuazione della sub-fascia e' indicativa: la collocazione definitiva e il canone vanno "
           "verificati con le Organizzazioni firmatarie tramite l'attestazione di rispondenza, in particolare "
           "in prossimita' del valore massimo di fascia.")

st.subheader("Maggiorazioni")
st.caption("Le maggiorazioni per durata, arredo e superficie ridotta sono cumulabili e si applicano al canone base "
           "in maniera progressiva: ogni aumento percentuale si applica sul canone gia' aumentato dal precedente.")

arredamento = st.radio(
    "Immobile arredato",
    ["Non arredato",
     "Parzialmente arredato",
     "Completamente arredato (+15%)"],
    help="Per l'arredo completo la maggiorazione massima e' del 15%. Per l'arredo parziale la maggiorazione deve "
         "essere inferiore al massimo e proporzionale all'arredo presente; e' comunque indispensabile una cucina o "
         "angolo cottura totalmente attrezzata di elettrodomestici e mobili."
)

perc_arredo_parziale = 0
if arredamento == "Parzialmente arredato":
    perc_arredo_parziale = st.slider("Percentuale di maggiorazione per arredo parziale (deve essere inferiore al 15%)",
                                     min_value=0, max_value=14, value=7)

tipo_contratto = st.selectbox(
    "Tipologia e durata del contratto",
    ["A - Uso abitativo ordinario, durata 3 anni",
     "A - Uso abitativo ordinario, durata 4 anni",
     "A - Uso abitativo ordinario, durata 5 anni",
     "A - Uso abitativo ordinario, durata 6 anni e oltre",
     "B - Transitorio ad uso abitativo, max 18 mesi (+5%)",
     "C - Studenti universitari fuori sede, 6 mesi - 3 anni (+5%)",
     "D - Alloggio sociale (D.M. 22/04/2008)"],
    help="Per i contratti di tipo A la maggiorazione per durata superiore ai 3 anni (V2) e' maggiore per gli "
         "immobili con superficie inferiore a mq 64 (calcolata sulla superficie di cui alla lettera a)."
)

classe_energetica = st.selectbox(
    "Classe energetica (APE)",
    ["A4", "A3", "A2", "A1", "B", "C", "D", "E", "F", "G"],
    help="Per le sub-fasce 2 e 3, gli immobili in classe E, F o G non possono utilizzare il valore massimo di fascia: "
         "il canone massimo e' ridotto del 4% (riduzione da applicare prima delle maggiorazioni)."
)

locatore_pubblico = st.checkbox(
    "Locatore Comune o Ente pubblico (anche partecipato o fondazione a prevalenza pubblica) (-30% sulle fasce)",
    help="Facolta' di ridurre di un ulteriore 30% i valori delle fasce di oscillazione, ad eccezione del valore "
         "minimo della sub-fascia 1 (limite minimo invalicabile)."
)

# CALCOLO DEL CANONE
can_min, can_max = fasce_bergamo[area][sub_fascia]

if classe_energetica in ["E", "F", "G"] and sub_fascia in [2, 3]:
    can_max = can_max * 0.96

if locatore_pubblico:
    min_sf1_area = fasce_bergamo[area][1][0]
    can_min = max(can_min * 0.70, min_sf1_area)
    can_max = can_max * 0.70

moltiplicatori = []

if 0 < sup_a < 52:
    moltiplicatori.append(1.20)
elif 52 <= sup_a <= 64:
    moltiplicatori.append(1.10)

if arredamento == "Completamente arredato (+15%)":
    moltiplicatori.append(1.15)
elif arredamento == "Parzialmente arredato" and perc_arredo_parziale > 0:
    moltiplicatori.append(1 + perc_arredo_parziale / 100)

piccolo_64 = 0 < sup_a < 64
if tipo_contratto == "A - Uso abitativo ordinario, durata 4 anni":
    moltiplicatori.append(1.05 if piccolo_64 else 1.04)
elif tipo_contratto == "A - Uso abitativo ordinario, durata 5 anni":
    moltiplicatori.append(1.08 if piccolo_64 else 1.06)
elif tipo_contratto == "A - Uso abitativo ordinario, durata 6 anni e oltre":
    moltiplicatori.append(1.10 if piccolo_64 else 1.08)
elif tipo_contratto == "B - Transitorio ad uso abitativo, max 18 mesi (+5%)":
    moltiplicatori.append(1.05)
elif tipo_contratto == "C - Studenti universitari fuori sede, 6 mesi - 3 anni (+5%)":
    moltiplicatori.append(1.05)



for moltiplicatore in moltiplicatori:
    can_min *= moltiplicatore
    can_max *= moltiplicatore

st.success(f"Assegnata: SUB-FASCIA {sub_fascia}")
st.info(f"Canone Minimo: {can_min:.2f} euro/mq annuo - Canone Massimo: {can_max:.2f} euro/mq annuo")

stima = st.button("Stima canone")
if stima:
    can_annuo_min = round(can_min * superficie_computabile, 2)
    can_annuo_max = round(can_max * superficie_computabile, 2)
    can_mensile_min = round(can_annuo_min / 12, 2)
    can_mensile_max = round(can_annuo_max / 12, 2)
    st.success(f"Canone ANNUO stimato: minimo -> {can_annuo_min} euro , massimo -> {can_annuo_max} euro")
    st.success(f"Canone MENSILE stimato: minimo -> {can_mensile_min} euro , massimo -> {can_mensile_max} euro")

