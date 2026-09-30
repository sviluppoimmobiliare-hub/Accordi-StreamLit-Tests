import streamlit as st

valori_a2 = {
    "1 - Centro": (33.10, 72.50),
    "2 - Panoramica": (53.10, 92.70),
    "3 - Via Crocifissa": (47.40, 71.10),
    "4 - Via Veneto": (49.80, 72.50),
    "5 - Brescia Due": (46.00, 70.10),
    "6 - Viale Piave": (38.90, 69.20),
    "7 - Q.re Abba / S. Anna": (36.50, 61.20),
    "8 - Fiumicello": (40.50, 61.30),
    "9 - Noce / Folzano": (32.80, 56.90),
    "10 - Vill. Prealpino": (43.00, 59.00),
    "11 - Vill. Badia / Violino": (30.50, 59.90),
    "12 - S. Eufemia": (43.10, 62.70),
    "13 - San Polo": (37.60, 61.90),
    "14 - Casazza": (41.70, 58.60),
    "15/20 - San Polino": (37.20, 57.40)
}

valori_a3 = {
    "1 - Centro": (27.80, 60.90),
    "2 - Panoramica": (53.10, 92.60),
    "3 - Via Crocifissa": (46.50, 69.70),
    "4 - Via Veneto": (43.80, 63.80),
    "5 - Brescia Due": (40.60, 61.80),
    "6 - Viale Piave": (32.30, 57.30),
    "7 - Q.re Abba / S. Anna": (36.60, 61.30),
    "8 - Fiumicello": (38.40, 58.10),
    "9 - Noce / Folzano": (31.60, 54.80),
    "10 - Vill. Prealpino": (41.50, 57.00),
    "11 - Vill. Badia / Violino": (29.80, 58.70),
    "12 - S. Eufemia": (39.20, 57.00),
    "13 - San Polo": (37.20, 61.40),
    "14 - Casazza": (40.50, 57.00),
    "15/20 - San Polino": (35.20, 54.30)
}


st.title("Calcolatore canone concordato - Comune di Brescia")


st.subheader("Generalita'")

tipo_contratto = st.radio("Tipologia contrattuale:", [
    "Contratto agevolato (art. 2, comma 3) ",
    "Contratto transitorio ordinario (art. 5, comma 1) ",
    "Contratto transitorio per studenti universitari (art. 5, commi 2 e 3) "])

categoria = st.radio("Categoria catastale dell'immobile:", [
    "A/1, A/2, A/7, A/8, A/9 o A/11 ",
    "A/3, A/4, A/5 o A/6 "])

zona = st.selectbox("Area omogenea :", list(valori_a2.keys()))

piano = st.number_input("Piano dell'appartamento (0 per piano terra)",
                        min_value=0, max_value=40, value=1, step=1)
edificio_alto = st.checkbox("L'edificio ha piu' di due piani fuori terra")


st.subheader("Superficie")

porzione = st.checkbox("Viene locata solo una porzione dell'immobile ")

if porzione == True:
    mq_esclusiva = st.number_input("Superficie utile dei vani locati ad uso esclusivo - mq",
                                   min_value=0.0, step=1.0)
    mq_condivise = st.number_input("Superficie utile totale delle parti e dei servizi condivisi - mq",
                                   min_value=0.0, step=1.0)
    stanze_locate = st.number_input("Numero di stanze ad uso esclusivo locate",
                                    min_value=0, max_value=30, value=1, step=1)
    stanze_totali = st.number_input("Numero totale di stanze ad uso esclusivo presenti nell'immobile",
                                    min_value=1, max_value=30, value=1, step=1)
    mq_utile = mq_esclusiva + mq_condivise * stanze_locate / stanze_totali
else:
    fonte = st.radio("Dato di partenza per la superficie utile:", [
        "Superficie utile riscaldata risultante dall'APE",
        "Superficie catastale netta (se nell'immobile ci sono locali non riscaldati, ad esempio "
        "ripostigli o magazzini, non compresi nel dato dell'APE)"],
        help="L'accordo prevede in via esclusiva il dato dell'APE in corso di validita'. Si passa "
             "alla superficie catastale netta soltanto quando l'immobile ha locali non riscaldati che "
             "non rientrano in quel dato.")
    mq_utile = st.number_input("Superficie utile - mq", min_value=0.0, step=1.0)

mq_principale = mq_utile * 1.125

mq_maggiorata = mq_principale
if mq_principale <= 60.0:
    mq_maggiorata = mq_principale * 1.20
    if mq_maggiorata > 72.59:
        mq_maggiorata = 72.59
elif mq_principale <= 65.0:
    mq_maggiorata = mq_principale * 1.10
    if mq_maggiorata > 72.59:
        mq_maggiorata = 72.59

st.write("Pertinenze, calcolate sulla superficie utile non maggiorata:")
mq_autorimessa = st.number_input("Autorimesse ad uso esclusivo - mq (calcolate al 50%)",
                                 min_value=0.0, step=1.0)
mq_posto_auto = st.number_input("Posto macchina in autorimesse di uso comune - mq (calcolato al 25%)",
                                min_value=0.0, step=1.0)
mq_accessori = st.number_input("Balconi, terrazze, cantine e solai - mq (calcolati al 25%)",
                               min_value=0.0, step=1.0)
mq_giardino = st.number_input("Giardino e/o cortile esclusivo - mq (calcolato al 10% solo se "
                              "superiore a 10 mq)", min_value=0.0, step=1.0)

mq_giardino_conv = 0.0
if mq_giardino > 10.0:
    mq_giardino_conv = mq_giardino * 0.10

mq_finali = (mq_maggiorata + mq_autorimessa * 0.50 + mq_posto_auto * 0.25
             + mq_accessori * 0.25 + mq_giardino_conv)

st.write(f"Superficie principale maggiorata: {mq_maggiorata:.2f} mq - superficie di calcolo "
         f"comprese le pertinenze: {mq_finali:.2f} mq")


st.subheader("Elementi per l'applicazione del valore massimo ")

mx1 = st.checkbox("1. Impianto di riscaldamento autonomo o centralizzato")
mx2 = st.checkbox("2. Box o posto auto")
mx3 = st.checkbox("3. Cantina o soffitta o solaio ad uso esclusivo e agevolmente fruibile")
mx4 = st.checkbox("4. Giardino privato o condominiale, terrazza condominiale attrezzata oppure area "
                  "parcabile per ciclomotori e biciclette, ad esempio un cortile")
mx5 = st.checkbox("5. Immobile ultimato, ristrutturato oppure sottoposto a manutenzione costante "
                  "negli ultimi 10 anni")
mx6 = st.checkbox("6. Classe di efficienza energetica non inferiore alla D")

mx7 = True
if piano > 2 and edificio_alto == True:
    mx7 = st.checkbox("7. Presenza di ascensore")
else:
    st.write("7. Ascensore: richiesto solo per gli edifici superiori a due piani fuori terra e per "
             "le unita' situate oltre il secondo piano")

elementi_massimo = [mx1, mx2, mx3, mx4, mx5, mx6, mx7]
n_massimo = sum(e for e in elementi_massimo if e == True)

if n_massimo == 7:
    st.info("Tutti gli elementi sono presenti: il valore massimo della fascia e' applicabile")
else:
    st.info(f"Elementi presenti: {n_massimo} su 7 - il valore massimo della fascia non e' applicabile, "
            f"il canone va concordato al di sotto di esso")


st.subheader("Elementi che impongono il valore minimo (punto A.8)")

neg1 = st.checkbox("Stabile o alloggio la cui ristrutturazione e' antecedente agli ultimi 30 anni, "
                   "oppure nello stesso periodo non e' avvenuta alcuna manutenzione")
neg2 = st.checkbox("Mancanza di impianto di riscaldamento autonomo o centralizzato")
neg3 = st.checkbox("Assenza di acqua corrente")
neg4 = st.checkbox("Assenza di bagno e servizi igienici")

condizioni_negative = [neg1, neg2, neg3, neg4]
n_negative = sum(c for c in condizioni_negative if c == True)

st.subheader("Maggiorazioni")

perc_totale = 0.0

arredo = st.radio("Arredamento (Allegato 4, punti b e c):", [
    "Non arredato",
    "Parzialmente arredato (fino al 10%)",
    "Completamente arredato (fino al 20%)"],
    help="Il massimo si applica solo con arredamento nuovo o in ottime condizioni di conservazione ed "
         "elettrodomestici perfettamente funzionanti. Per il parzialmente arredato serve inoltre che "
         "sia interamente ammobiliato il vano cucina e interamente arredato almeno un altro vano.")
if arredo.startswith("Parzialmente"):
    magg_arredo = st.slider("Maggiorazione per l'arredo effettivamente concordata (%)", 0, 10, 10)
    perc_totale = perc_totale + magg_arredo / 100.0
elif arredo.startswith("Completamente"):
    magg_arredo = st.slider("Maggiorazione per l'arredo effettivamente concordata (%)", 0, 20, 20)
    perc_totale = perc_totale + magg_arredo / 100.0

classe = st.radio("Classe energetica da A1 ad A4 :", [
    "Nessuna delle classi da A1 ad A4",
    "A1 (massimo 2,5%)",
    "A2 (massimo 5%)",
    "A3 (massimo 7,5%)",
    "A4 (massimo 10%)"])
if classe.startswith("A1"):
    magg_classe = st.slider("Maggiorazione per la classe energetica concordata (per mille)", 0, 25, 25)
    perc_totale = perc_totale + magg_classe / 1000.0
elif classe.startswith("A2"):
    magg_classe = st.slider("Maggiorazione per la classe energetica concordata (per mille)", 0, 50, 50)
    perc_totale = perc_totale + magg_classe / 1000.0
elif classe.startswith("A3"):
    magg_classe = st.slider("Maggiorazione per la classe energetica concordata (per mille)", 0, 75, 75)
    perc_totale = perc_totale + magg_classe / 1000.0
elif classe.startswith("A4"):
    magg_classe = st.slider("Maggiorazione per la classe energetica concordata (per mille)", 0, 100, 100)
    perc_totale = perc_totale + magg_classe / 1000.0

metro = st.checkbox("e) Immobile in prossimita' di una fermata della metropolitana, a una distanza "
                    "massima di percorrenza di 600 metri (fino al 5%)")
if metro == True:
    magg_metro = st.slider("Maggiorazione per la vicinanza alla metropolitana concordata (%)", 0, 5, 5)
    perc_totale = perc_totale + magg_metro / 100.0

interventi = st.radio("Interventi sull'immobile :", [
    "Nessuno di questi interventi",
    "f) Completamente ristrutturato anche nell'isolamento termico dopo il 2011, con passaggio in "
    "classe energetica pari o superiore a D (+10%)",
    "g) Edificato dopo il 2011 e progettato con isolamento termico che lo colloca in classe "
    "energetica pari o superiore a D (+10%)",
    "h) Completamente ristrutturato dopo il 1968, senza interventi di efficientamento energetico (+5%)"])
if interventi.startswith("f)") or interventi.startswith("g)"):
    perc_totale = perc_totale + 0.10
elif interventi.startswith("h)"):
    perc_totale = perc_totale + 0.05

magg_i = st.checkbox("i) Impianto fisso di condizionamento dell'aria, pompa di calore o "
                     "raffrescamento in almeno la meta' dei vani (+2%)")
if magg_i == True:
    perc_totale = perc_totale + 0.02

magg_l = st.checkbox("l) Stabile con impianti per il superamento delle barriere architettoniche: "
                     "montascale fruibile e funzionante e totale assenza di barriere (+2%)")
if magg_l == True:
    perc_totale = perc_totale + 0.02

if interventi.startswith("Nessuno") or interventi.startswith("h)"):
    magg_m = st.checkbox("m) Impianto fotovoltaico o solare termico che copre interamente il "
                         "fabbisogno per l'acqua calda e almeno in parte quello per riscaldare o "
                         "raffrescare l'immobile (+1%)")
    if magg_m == True:
        perc_totale = perc_totale + 0.01

magg_n = st.checkbox("n) Presenza di impianti sportivi, piscina o palestra (+5%)")
if magg_n == True:
    perc_totale = perc_totale + 0.05

if tipo_contratto.startswith("Contratto agevolato"):
    durata = st.radio("Durata del primo periodo contrattuale:", [
        "Tre anni",
        "Quattro anni (+3,00%)",
        "Cinque anni (+5,50%)",
        "Sei anni (+8,00%)",
        "Superiore a sei anni (+10,50%)"])
    if durata.startswith("Quattro"):
        perc_totale = perc_totale + 0.03
    elif durata.startswith("Cinque"):
        perc_totale = perc_totale + 0.055
    elif durata.startswith("Sei"):
        perc_totale = perc_totale + 0.08
    elif durata.startswith("Superiore"):
        perc_totale = perc_totale + 0.105
else:
    st.caption("La maggiorazione per la durata non si applica: i contratti transitori ordinari durano "
               "al massimo diciotto mesi e quelli per studenti al massimo tre anni.")

if tipo_contratto.startswith("Contratto transitorio per studenti"):
    st.caption("Per i contratti destinati agli studenti universitari le fasce di oscillazione non "
               "subiscono alcun aumento per gli immobili vincolati (punto C.5).")
else:
    vincolato = st.checkbox("Immobile vincolato ai sensi dell'art. 1, comma 2, lettera a) della "
                            "L. 431/98 e della L. 1/6/1939 (+20%)")
    if vincolato == True:
        perc_totale = perc_totale + 0.20

riduzione = st.slider("Riduzione del valore minimo (massimo 30%)", 0, 30, 0,
                      help="Punto A.8: zone degradate e prive di dotazioni infrastrutturali. "
                           "Punto H.2: condizioni sociali o reddituali particolarmente disagiate del "
                           "conduttore, precarie condizioni dell'immobile, scarsa qualita' ambientale, "
                           "oneri condominiali elevati, situazioni generali di emergenza. La riduzione "
                           "va motivata nel contratto e indicata nell'attestazione di rispondenza.")


if categoria.startswith("A/1"):
    val_min, val_max = valori_a2[zona]
else:
    val_min, val_max = valori_a3[zona]

val_min = val_min + val_min * perc_totale
val_max = val_max + val_max * perc_totale
val_min = val_min - val_min * riduzione / 100.0

if n_negative >= 1:
    val_max = val_min

canone_annuo_min = mq_finali * val_min
canone_annuo_max = mq_finali * val_max

stima = st.button("Stima il canone")

if stima:
    if mq_finali <= 0.0:
        st.warning("Inserire la superficie dell'immobile per ottenere la stima")
    else:
        st.success(f"Canone mensile stimato: da {canone_annuo_min / 12.0:.2f} euro a "
                   f"{canone_annuo_max / 12.0:.2f} euro")
        st.write(f"Canone annuo: da {canone_annuo_min:.2f} a {canone_annuo_max:.2f} euro")
        st.write(f"Area {zona} - valori annui applicati da {val_min:.2f} a {val_max:.2f} euro/mq")
        st.write(f"Percentuale totale di maggiorazione applicata: {perc_totale * 100:.2f} %")
        if n_negative >= 1:
            st.warning(f"Sono presenti {n_negative} degli elementi del punto A.8: si applica il valore "
                       f"minimo della fascia")
        elif n_massimo < 7:
            st.caption("Non essendo presenti tutti e sette gli elementi dell'Allegato 4 punto a, il "
                       "valore massimo indicato non e' applicabile: il canone va concordato al di "
                       "sotto di esso.")
