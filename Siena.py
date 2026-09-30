import streamlit as st
import math

st.title("Calcolatore Canone Concordato - Comune di Siena")


st.subheader("Categoria catastale ")
categoria_catastale = st.selectbox("Categoria catastale dell'unita' immobiliare", [
    "A/1", "A/2", "A/3", "A/4", "A/5", "A/7", "A/8", "A/9",
    "A/6 - non ammessa", "A/10 - non ammessa", "A/11 - non ammessa",
])
if "non ammessa" in categoria_catastale:
    st.warning("Sono ammesse ai contratti del presente accordo solo le unita' immobiliari destinate a "
               "civile abitazione delle categorie catastali A/1, A/2, A/3, A/4, A/5, A/7, A/8, A/9: "
               "la categoria selezionata e' esclusa.")


quartieri_zona2 = [
    "San Prospero", "Saragino", "Cappuccini", "Marciano", "Uncinello",
    "Stazione Ferroviaria", "Vico Alto", "Viale Bracci", "Scacciapensieri",
    "Malizia", "Ravacciano", "Madonnina Rossa", "Due Ponti", "Str. Di Busseto",
    "Derna", "Valli", "Coroncina", "Massetana Romana", "Colonna San Marco",
    "Pescaia", "Via Ricasoli", "Via Vittorio Emanuele", "Viale Cavour",
    "Palazzo dei Diavoli", "Via Celso Cittadini", "Via Quinto Settano",
    "Via Sansedoni", "Via Bernardo Tolomei", "Petriccio", "Acquacalda",
    "Policlinico", "San Miniato", "Stellino", "Montarioso",
]
quartieri_zona3 = [
    "Bottega Nuova", "Malafrasca", "Ponte a Bozzone", "Vico d'Arbia",
    "Pieve al Bozzone", "Presciano", "Taverne d'Arbia", "Ruffolo", "l'Abbadia",
    "Isola d'Arbia", "Costafabbri", "Costalpino", "Volte Basse", "S. Andrea",
    "S. Rocco a Pilli", "Terrenzano", "Montalbuccio", "Casciano delle Masse",
]

zone_siena = {
    "ZONA 1 - CENTRO STORICO": "Tutta l'area entro la cinta muraria della citta'.",
    "ZONA 2 - SEMICENTRALE": ", ".join(quartieri_zona2) + ".",
    "ZONA 3 - PERIFERICA": ", ".join(quartieri_zona3) + ".",
}

mappa_quartieri = {"Centro storico (entro la cinta muraria)": "ZONA 1 - CENTRO STORICO"}
for q in quartieri_zona2:
    mappa_quartieri[q] = "ZONA 2 - SEMICENTRALE"
for q in quartieri_zona3:
    mappa_quartieri[q] = "ZONA 3 - PERIFERICA"

opzioni_quartieri = (["Centro storico (entro la cinta muraria)"] +
                     sorted(quartieri_zona2 + quartieri_zona3, key=str.lower) +
                     ["Altro (selezione manuale della zona)"])

st.subheader("Quartiere e zona")
quartiere = st.selectbox("Quartiere / localita' di ubicazione dell'immobile", opzioni_quartieri)
if quartiere == "Altro (selezione manuale della zona)":
    st.caption("L'elenco dei quartieri della zona semicentrale e' esemplificativo (art. 4: 'ad esempio'): "
               "per le localita' non in elenco selezionare manualmente la zona di appartenenza.")
    zona = st.selectbox("Zona di ubicazione dell'immobile", list(zone_siena.keys()))
else:
    zona = mappa_quartieri[quartiere]
st.info(f"Zona applicata: {zona}")
st.caption(zone_siena[zona])

fasce_siena = {
    "ZONA 1 - CENTRO STORICO": {"A": (2.50, 10.84), "B": (2.50, 9.22), "C": (2.50, 8.13)},
    "ZONA 2 - SEMICENTRALE":   {"A": (2.50, 9.76),  "B": (2.50, 8.29), "C": (2.50, 7.32)},
    "ZONA 3 - PERIFERICA":     {"A": (2.50, 8.68),  "B": (2.50, 5.71), "C": (2.50, 5.04)},
}

st.subheader("Superficie convenzionale")
sup_A = st.number_input("Superficie interna utile abitativa in mq (area calpestabile, esclusi muri e palchi morti)", min_value=0.0)
sup_B = st.number_input("Autorimessa singola o box auto in mq (conteggiata al 50%)", min_value=0.0)
sup_C = st.number_input("Lastrici solari di uso esclusivo al piano attico in mq (25% fino ai mq utili, 5% sull'eccedenza)", min_value=0.0)
sup_D = st.number_input("Posto auto coperto in comune in mq (conteggiato al 30%)", min_value=0.0)
sup_E = st.number_input("Posto auto scoperto in comune in mq (conteggiato al 20%)", min_value=0.0)
sup_F = st.number_input(
    "Balconi, terrazze, lastrici solari non all'attico, cantine, soffitte in mq (conteggiati al 30%)", min_value=0.0,)
sup_G = st.number_input("Superficie scoperta di pertinenza in godimento esclusivo in mq (20%, con risultanza fino alla superficie utile)", min_value=0.0)
sup_H = st.number_input("Superficie scoperta in uso condominiale in mq (conteggiata al 2%)", min_value=0.0)
sup_vani_bassi = st.number_input(
    "Superficie interna dei vani con altezza utile inferiore a 1,70 m in mq (detratta al 30%)", min_value=0.0,
    help="La superficie interna utile abitativa (primo campo) considera gia' come non "
         "calpestabili le aree con altezza inferiore a 170 cm: compilare questo campo solo se la superficie e' stata "
         "misurata al lordo di tali vani.")

if sup_C <= sup_A:
    quota_C = sup_C * 0.25
else:
    quota_C = sup_A * 0.25 + (sup_C - sup_A) * 0.05

quota_G = min(sup_G * 0.20, sup_A)

superficie_base = (sup_A + sup_B * 0.50 + quota_C + sup_D * 0.30 +
                   sup_E * 0.20 + sup_F * 0.30 + quota_G + sup_H * 0.02)

if 0 < superficie_base <= 60:
    incremento_25 = st.checkbox(
        "Applica l'incremento del 25% per immobili con superficie fino a 60 mq(Art. 6)", value=True,
        help="La superficie POTRA' essere incrementata del 25% fino al massimo di 60 mq: "
             "e' una facolta' delle parti, non un obbligo. La superficie aumentata non puo' in ogni caso "
             "superare il limite di 60 mq.")
else:
    incremento_25 = False

if incremento_25:
    superficie_convenzionale = min(superficie_base * 1.25, 60.0)
else:
    superficie_convenzionale = superficie_base

superficie_convenzionale = max(superficie_convenzionale - sup_vani_bassi * 0.30, 0.0)

st.info(f"Superficie convenzionale: {superficie_convenzionale:.2f} mq")

st.subheader("Tipologia dell'alloggio ")
with st.expander("Criteri di classificazione "):
    st.markdown(
        "- **Tipologia A**: lavori ultimati entro 30 anni con ammodernamento degli impianti elettrico/idrico/sanitario; "
        "servizio igienico completo con almeno 4 apparecchi e finestra/areazione; cantina e/o garage e/o posto auto. "
        "Gli immobili nei centri storici si considerano di tipologia A anche senza cantina/garage/posto auto se in presenza "
        "di tutti gli altri requisiti.\n"
        "- **Tipologia B**: lavori ultimati oltre il 30 anno con ammodernamento degli impianti; servizio igienico completo "
        "(almeno 4 apparecchi) oppure incompleto/con meno di 4 apparecchi.\n"
        "- **Tipologia C**: lavori ultimati oltre il 50 anno e almeno due tra: assenza di riscaldamento; assenza "
        "contemporanea di garage, posto auto e cantina (tutti e tre); assenza del servizio igienico o non interno "
        "all'immobile; assenza di infissi efficienti."
    )
tipologia = st.selectbox("Tipologia (in base alle caratteristiche dell'unita' immobiliare)", ["A", "B", "C"])

st.subheader("Grandi proprieta' e alloggio sociale")
grande_proprieta = st.checkbox(
    "Locatore rientrante tra le grandi proprieta' o gli enti dell'Art. 17",
    help="Associazioni e fondazioni di previdenza, istituti di credito, enti previdenziali pubblici, compagnie "
         "assicurative, fondi immobiliari, enti locali, enti privatizzati, cooperative, soggetti giuridici o "
         "fisici detentori di piu' di 100 unita' immobiliari ad uso abitativo, anche ubicate in modo diffuso "
         "e frazionato sul territorio nazionale.")
if grande_proprieta:
    st.warning("Per le grandi proprieta' i canoni sono definiti in base ad appositi e specifici "
               "Accordi integrativi tra la proprieta' interessata e le organizzazioni firmatarie dell'accordo. "
               "I valori di questo calcolatore hanno quindi valore solo indicativo.")

alloggio_sociale = st.checkbox(
    "Alloggio sociale",
    help="Il canone massimo dell'alloggio sociale e' individuato all'interno delle fasce di oscillazione in "
         "misura non superiore ai valori degli immobili di tipologia B, tenuto conto delle agevolazioni "
         "pubbliche comunque spettanti al locatore. Restano ferme le modalita' di calcolo della superficie "
         "dell'art. 6.")

base_min, base_max = fasce_siena[zona][tipologia]

if alloggio_sociale:
    base_B_max = fasce_siena[zona]["B"][1]
    if base_max > base_B_max:
        base_max = base_B_max
        st.info(f"Alloggio sociale : canone base massimo limitato al valore della tipologia B "
                f"della zona ({base_B_max:.2f} euro/mq mensile).")
    st.caption("Le agevolazioni pubbliche spettanti al locatore costituiscono elemento oggettivo di ulteriore "
               "riduzione del canone massimo , non quantificata "
               "dall'accordo: in loro presenza il massimale indicato va ridotto di conseguenza.")

st.subheader("Maggiorazioni ")

tipo_contratto = st.selectbox("Tipo di contratto", [
    "Abitativo agevolato 3+2 (durata minima)",
    "Abitativo agevolato 4+2 (+4%)",
    "Abitativo agevolato 5+2 (+5%)",
    "Abitativo agevolato 6+2 e oltre (+10%)",
    "Transitorio (max 18 mesi)",
    "Studenti universitari (6 mesi - 3 anni)",
])
studenti = "Studenti" in tipo_contratto

arredo = st.radio(
    "Arredo, ["Non arredato", "Parzialmente arredato", "Completamente arredato"],
    help="Per i contratti studenti l'alloggio 'completamente ammobiliato' richiede: "
         "camera con letto, armadio, scrivania e sedia, lampada da tavolo, libreria; cucina con mobili per derrate "
         "alimentari, tavolo con sedie, angolo cottura; elettrodomestici (lavatrice, lavastoviglie, attrezzature "
         "per cucina, televisore); bagno con servizi.")
st.caption("Contratti ordinari/transitori: completo +15%, parziale +10%. "
           "Contratti per studenti universitari: completo +25%, parziale +15%.")

art9c2 = st.checkbox(
    "Immobile con TUTTE le caratteristiche dell'Art. 9 (+15%)",
    help="a) immobile nuovo ultimato/abitabile entro 10 anni dall'acquisto oppure ristrutturato/risanato con lavori "
         "ultimati entro 10 anni e ammodernamento impianti elettrico/idrico/sanitario; b) APE in classe da A a E; "
         "c) ascensore per unita' dal terzo piano in poi (per le unita' poste al di sotto del terzo piano il "
         "requisito dell'ascensore non e' pertinente e non preclude la maggiorazione). La maggiorazione richiede "
         "la presenza di tutte le caratteristiche ('nessuna esclusa').")

storico = st.checkbox(
    "Immobile di interesse storico-artistico (+15%)")

if art9c2 and storico:
    st.warning("E' prevista un unica maggiorazione del 15%: il vincolo storico-artistico e' una via "
               "alternativa di accesso alla stessa maggiorazione delle caratteristiche delineate dall' Art. 9 , che pertanto NON si cumula e viene applicata una sola volta.")

perc_arredo = 0.0
perc_altre = 0.0

if arredo == "Completamente arredato":
    perc_arredo = 0.25 if studenti else 0.15
elif arredo == "Parzialmente arredato":
    perc_arredo = 0.15 if studenti else 0.10

if art9c2 or storico:
    perc_altre += 0.15

if "4+2" in tipo_contratto:
    perc_altre += 0.04
elif "5+2" in tipo_contratto:
    perc_altre += 0.05
elif "6+2" in tipo_contratto:
    perc_altre += 0.10

perc = perc_arredo + perc_altre

magg_mq = base_max * perc
canone_mq_min = base_min + magg_mq
canone_mq_max = base_max + magg_mq

st.success(f"Tipologia {tipologia} - {zona}")
st.info(f"Canone base (fascia art. 5): {base_min:.2f} - {base_max:.2f} euro/mq mensile")
st.info(f"Maggiorazioni complessive (art. 11): +{perc * 100:.0f}% sul canone base")
st.info(f"Canone concordato: {canone_mq_min:.2f} - {canone_mq_max:.2f} euro/mq mensile")

st.subheader("Affitto di porzione di immobile ")
porzione = st.checkbox("Locazione di porzioni di immobile (calcolo del canone per singole camere)")

superfici_camere = []
if porzione:
    st.caption("Il canone dell'intero appartamento e' diviso per la somma delle superfici ad uso esclusivo: il "
               "valore mq/mese cosi' ottenuto, moltiplicato per la superficie di ciascuna camera, da' il canone "
               "massimo della singola porzione, comprensivo in misura proporzionale degli spazi comuni "
               ", che quindi NON vanno inseriti. Le eventuali pertinenze esclusive di una camera vanno "
               "sommate alla sua superficie. Vanno conteggiate anche le camere che il locatore "
               "riserva per se' o che non vengono locate.")
    n_camere = st.number_input("Numero di camere ad uso esclusivo (comprese quelle non locate)",
                               min_value=1, max_value=10, value=2, step=1)
    for i in range(int(n_camere)):
        sup_camera = st.number_input(
            f"Superficie ad uso esclusivo della camera {i + 1} in mq (comprese eventuali pertinenze esclusive)",
            min_value=0.0, key=f"camera_{i + 1}")
        superfici_camere.append(sup_camera)
    st.caption("E' ammesso locare le singole camere con tipologie contrattuali diverse: in tal caso "
               "ripetere il calcolo selezionando il tipo di contratto corrispondente. Per le porzioni autonome "
               "dotate di ingresso esclusivo e prive di parti comuni il canone si calcola "
               "direttamente sulla sola parte locata con i criteri ordinari.")

def arrotonda_euro(x):
    
    return int(math.floor(x + 0.5))

stima = st.button("Stima canone")
if stima:
    can_mensile_min = canone_mq_min * superficie_convenzionale
    can_mensile_max = canone_mq_max * superficie_convenzionale
    arr_min = arrotonda_euro(can_mensile_min)
    arr_max = arrotonda_euro(can_mensile_max)
    st.success(f"Canone MENSILE (arrotondato all'unita' di euro, art. 20): minimo -> {arr_min} euro , massimo -> {arr_max} euro")
    st.success(f"Canone ANNUO (12 mensilita' arrotondate): minimo -> {arr_min * 12} euro , massimo -> {arr_max * 12} euro")
    st.caption(f"Valori intermedi non arrotondati: canone mensile {can_mensile_min:.2f} - {can_mensile_max:.2f} euro ; "
               f"canone annuo {can_mensile_min * 12:.2f} - {can_mensile_max * 12:.2f} euro")

    if porzione:
        tot_camere = sum(superfici_camere)
        if tot_camere > 0:
            magg_riparto_mq = base_max * perc_altre
            can_riparto_min = (base_min + magg_riparto_mq) * superficie_convenzionale
            can_riparto_max = (base_max + magg_riparto_mq) * superficie_convenzionale
            
            val_mq_min = math.floor(can_riparto_min / tot_camere * 100) / 100.0
            val_mq_max = math.floor(can_riparto_max / tot_camere * 100) / 100.0
            st.info(f"Canone di riparto dell'intero appartamento senza maggiorazione arredo : "
                    f"{can_riparto_min:.2f} - {can_riparto_max:.2f} euro mensili")
            st.info(f"Valore mq/mese (canone / {tot_camere:.2f} mq di superfici esclusive): "
                    f"{val_mq_min:.2f} - {val_mq_max:.2f} euro")
            for i in range(len(superfici_camere)):
                cam_min = arrotonda_euro(val_mq_min * superfici_camere[i])
                cam_max = arrotonda_euro(val_mq_max * superfici_camere[i])
                st.success(f"Camera {i + 1} ({superfici_camere[i]:.2f} mq): canone mensile minimo -> {cam_min} euro , "
                           f"massimo -> {cam_max} euro ")
            st.caption("La somma dei canoni delle porzioni effettivamente locate non puo' in ogni caso superare il "
                       "canone dell'intero appartamento; le camere riservate al locatore o non locate "
                       "sono conteggiate nel riparto e poi scorporate .")
        else:
            st.warning("Inserire le superfici delle camere per calcolare il canone delle singole porzioni.")
