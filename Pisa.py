import streamlit as st

zonizzazione = {
    
    "Lungarno Simonelli (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Pacinotti (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Mediceo (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Buozzi (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Sonnino (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Gambacorti (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Galilei (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Lungarno Fibonacci (oltre il 50% delle finestre sul lungarno)": "Pregio",
    "Marina di Pisa - lungomare o piazza con affaccio sul mare": "Pregio",
    "Tirrenia - viale del Tirreno con affaccio sul mare": "Pregio",
    "Calambrone - viale del Tirreno con affaccio sul mare": "Pregio",
    
    "S. Antonio, quartiere storico fino alla ferrovia": "A",
    "S. Martino, quartiere storico": "A",
    "S. Maria, quartiere storico fino alla ferrovia": "A",
    "S. Francesco, compresa la zona tra via di Pratale a nord, via Battelli e via De Amicis a est": "A",
    "Porta a Lucca, tra via di Gello a est, via Tino da Camaino a ovest, via Contessa Matilde e "
    "via del Brennero a sud, via G. Falcone a nord (esclusa la zona Piazzali)": "A",
    "Viale delle Piagge fino al tondo": "A",
    "Barbaricina, tra via Aurelia a est, via del Capannone, via T. Rook, via F. Tesio a ovest "
    "e via delle Cascine a nord": "A",
    "Marina di Pisa, non lungomare": "A",
    "Tirrenia, non lungomare": "A",
    "Calambrone, non lungomare": "A",
   
    "S. Marco, nella zona delimitata dalla ferrovia e dalla S.G.C. FI-PI-LI": "B",
    "S. Giusto, nella zona delimitata dalla ferrovia e dalla S.G.C. FI-PI-LI": "B",
    "Porta Fiorentina, tra le ex mura urbane a nord, la ferrovia a sud, via Pilla - via vecchia "
    "tranvia a sud e l'Arno a ovest (esclusa la zona da via Catalani a via Colombo)": "B",
    "Porta a Mare, tra via A. Moro, via Livornese fino al ponte del CEP e l'Arno": "B",
    "Barbaricina, tra via delle Cascine e l'Arno e a ovest di via Boccherini (escluso quanto in "
    "zona A)": "B",
    "Zona Impianti Sportivi, fino a via di Campaldo a nord, via Pietrasantina, via del "
    "Marmigliano, ferrovia a est e via Aurelia a ovest": "B",
    "Zona Piazzali, tra via U. Rindi a nord, via Piave a est e via Contessa Matilde a sud": "B",
    "Zona tra via di Gello a ovest, via Lucchese a est, via Paparelli a sud e via Chiarugi - "
    "Caserma dei Paracadutisti a nord": "B",
    "Pratale e Don Bosco, tra via Battelli e via De Amicis a ovest, via Luzzatto e via Nenni a "
    "est e il viale delle Piagge a sud": "B",
    "S. Michele, fino a via Mons. Manghi e via Padre Pio a est": "B",
    "Porta a Piagge": "B",
    "Cisanello": "B",
    "Pisanova, esclusa via Paolo VI": "B",
    "La Vettola": "B",
    "S. Piero, dalla superstrada fino a S. Piero tra via E. Scauro, via Castagnolo e via Livornese": "B",
    
    "Gagno": "C",
    "I Passi": "C",
    "Pisanova, limitatamente a via Paolo VI": "C",
    "S. Biagio, vie Mazzei, Taddei, Simon e Martin Lutero": "C",
    "Riglione": "C",
    "Oratoio": "C",
    "Putignano": "C",
    "S. Ermete": "C",
    "S. Giusto a sud della S.G.C. FI-PI-LI": "C",
    "Porta a Mare, escluso quanto in zona B": "C",
    "Luicchio": "C",
    "CEP, tra via Pergolesi - Pierin del Vaga a nord, via Tiziano Vecellio a ovest e via "
    "Boccherini a est": "C",
    "Zona stazione, da via Colombo a via Catalani": "C",
    
    "Zone artigianali e agricole": "D",
    "Ospedaletto": "D",
    "Coltano": "D"
}

localita_lontane = [
    "Putignano", "Riglione", "Oratoio",
    "S. Piero, dalla superstrada fino a S. Piero tra via E. Scauro, via Castagnolo e via Livornese",
    "Marina di Pisa - lungomare o piazza con affaccio sul mare", "Marina di Pisa, non lungomare",
    "Tirrenia - viale del Tirreno con affaccio sul mare", "Tirrenia, non lungomare",
    "Calambrone - viale del Tirreno con affaccio sul mare", "Calambrone, non lungomare",
    "La Vettola"
]

fasce_tipo_A = {
    "Pregio": [7.0, 8.0, 8.0, 10.0],
    "A": [6.5, 7.5, 7.5, 8.5],
    "B": [4.8, 5.8, 5.8, 6.8],
    "C": [4.5, 5.5, 5.5, 6.5],
    "D": [4.0, 5.0, 5.0, 6.1]
}

fasce_tipo_B = {
    "Pregio": [6.5, 7.6, 7.6, 8.5],
    "A": [5.8, 6.7, 6.7, 7.6],
    "B": [4.7, 5.7, 5.7, 6.7],
    "C": [4.0, 5.0, 5.0, 6.0],
    "D": [3.5, 4.5, 4.5, 5.4]
}

fasce_tipo_C = {
    "Pregio": [5.0, 6.0, 6.0, 6.9],
    "A": [4.2, 5.2, 5.2, 6.1],
    "B": [4.0, 4.7, 4.7, 5.5],
    "C": [3.5, 4.1, 4.1, 4.7],
    "D": [3.5, 4.1, 4.1, 4.7]
}


st.title("Calcolatore canone concordato - Comune di Pisa")


st.subheader("Generalita'")

tipo_contratto = st.radio("Tipologia contrattuale:", [
    "Contratto agevolato",
    "Contratto transitorio ordinario",
    "Contratto transitorio per studenti universitari "])

if tipo_contratto.startswith("Contratto transitorio ordinario"):
    st.caption("Per i contratti fino a 30 giorni il canone e' lasciato alla libera contrattazione "
               "delle parti: il calcolatore vale per quelli da 31 giorni a 18 mesi.")

localita = st.selectbox("Localita' (art. 2):", list(zonizzazione.keys()),
                        help="Gli alloggi situati nelle vie di confine tra due zone rientrano nella "
                             "zona con il valore al mq piu' elevato.")
zona = zonizzazione[localita]
st.info("Zona: " + zona)

st.subheader("Superficie convenzionale")

mq_utile = st.number_input("a) Superficie interna utile dell'alloggio - mq", min_value=0.0, step=1.0)
mq_autorimessa = st.number_input("b) Autorimessa singola - mq (calcolata al 60%)", min_value=0.0, step=1.0)
mq_coperto = st.number_input("c) Posto auto coperto di proprieta' esclusiva - mq (calcolato al 40%)",
                             min_value=0.0, step=1.0)
mq_comune = st.number_input("d) Posto auto di effettiva disponibilita' in area comune - mq "
                            "(calcolato al 30%)", min_value=0.0, step=1.0)
mq_scoperto = st.number_input("e) Posto auto scoperto di proprieta' esclusiva - mq (calcolato al 20%)",
                              min_value=0.0, step=1.0)
mq_accessori = st.number_input("f) Balconi, terrazze, cantine e altri accessori simili - mq "
                               "(calcolati al 25%)", min_value=0.0, step=1.0)
mq_giardino = st.number_input("g, h, i) Giardino in godimento esclusivo - mq (10% fino a 100 mq, "
                              "15% da 101 a 200 mq, 20% oltre 200 mq)", min_value=0.0, step=1.0)
mq_area_scoperta = st.number_input("j) Area scoperta di pertinenza in godimento esclusivo, non a "
                                   "giardino - mq (10%, solo se non inferiore a 100 mq)",
                                   min_value=0.0, step=1.0)

if mq_utile <= 45.0:
    mq_utile_corretta = mq_utile * 1.20
    if mq_utile_corretta > 49.60:
        mq_utile_corretta = 49.60
elif mq_utile <= 70.0:
    mq_utile_corretta = mq_utile * 1.10
    if mq_utile_corretta > 70.0:
        mq_utile_corretta = 70.0
elif mq_utile <= 110.0:
    mq_utile_corretta = mq_utile
else:
    mq_utile_corretta = mq_utile * 0.90
    if mq_utile_corretta < 110.0:
        mq_utile_corretta = 110.0

if mq_giardino <= 100.0:
    mq_giardino_conv = mq_giardino * 0.10
elif mq_giardino <= 200.0:
    mq_giardino_conv = mq_giardino * 0.15
else:
    mq_giardino_conv = mq_giardino * 0.20

mq_area_scoperta_conv = 0.0
if mq_area_scoperta >= 100.0:
    mq_area_scoperta_conv = mq_area_scoperta * 0.10

mq_finali = (mq_utile_corretta
             + mq_autorimessa * 0.60
             + mq_coperto * 0.40
             + mq_comune * 0.30
             + mq_scoperto * 0.20
             + mq_accessori * 0.25
             + mq_giardino_conv
             + mq_area_scoperta_conv)

st.write(f"Superficie interna corretta: {mq_utile_corretta:.2f} mq - superficie convenzionale: "
         f"{mq_finali:.2f} mq")

porzione = st.checkbox("Viene locata solo una porzione dell'immobile")
quota_porzione = 1.0
if porzione == True:
    mq_esclusivi = st.number_input("Superficie della porzione locata ad uso esclusivo - mq",
                                   min_value=0.0, step=1.0)
    mq_spazi_comuni = st.number_input("Superficie degli spazi comuni dell'immobile - mq",
                                      min_value=0.0, step=1.0)
    occupanti = st.number_input("Numero degli occupanti dell'immobile", min_value=1, max_value=20,
                                value=1, step=1)
    if mq_utile > 0.0:
        quota_porzione = (mq_esclusivi + mq_spazi_comuni / occupanti) / mq_utile
    if quota_porzione > 1.0:
        quota_porzione = 1.0
    st.caption("Il coefficiente correttivo della superficie si applica sul canone dell'intero "
               "immobile, che poi viene frazionato.")


st.subheader("Classificazione dell'immobile (art. 5)")

categoria = st.radio("Categoria catastale:", [
    "A/7 - villa o villetta",
    "A/2 o A/3 - appartamento",
    "Altra categoria"])

anni = st.number_input("Anni dalla costruzione, oppure dall'ultima ristrutturazione interna", min_value=0, max_value=300, value=20, step=1)

car_a = st.checkbox("a) Impianto idrico idoneo ed efficiente")
car_b = st.checkbox("b) Impianto elettrico a norma")

riscaldamento = st.radio("Riscaldamento:", [
    "Efficiente e a norma in tutti i vani utili",
    "Efficiente e a norma, ma non in tutti i vani utili",
    "Assente o non a norma"])

servizi = st.radio("Servizi igienici:", [
    "1) Doppi servizi con il secondo di almeno 3 elementi, oppure unico servizio con antibagno, "
    "almeno 4 elementi sanitari e finestra",
    "2) Servizio interno con almeno 4 elementi sanitari, con finestra o aerazione forzata",
    "3) Servizio interno con almeno 3 elementi sanitari, con finestra o aerazione forzata",
    "4) Un solo servizio con meno di 2 elementi sanitari, oppure esterno all'alloggio, oppure "
    "alloggio dichiarato antigienico",
    "5) Nessuno dei casi precedenti"])

car_e = st.checkbox("e) Spazi esterni ad uso esclusivo (garage, terrazze, logge, cantine) oltre il "
                    "15% della superficie utile")
car_f = st.checkbox("f) Spazi per parcheggio con effettiva disponibilita'")
car_h = st.checkbox("h) Sistemi funzionanti di condizionamento d'aria")
car_i = st.checkbox("i) Ascensore (per le unita' oltre il 3 piano fuori terra)")

car_g = False
if mq_utile > 0.0 and mq_giardino > mq_utile * 0.40:
    car_g = True

car_c = False
if riscaldamento.startswith("Efficiente e a norma in tutti"):
    car_c = True
car_d = False
if servizi.startswith("1)"):
    car_d = True

caratteristiche_A = [car_a, car_b, car_c, car_d, car_e, car_f, car_g, car_h, car_i]
n_caratteristiche = sum(x for x in caratteristiche_A if x == True)

abbattimento_50 = False
if car_a == False or car_b == False:
    tipo = "nessuno"
elif (categoria.startswith("Altra") == False and car_c == True and n_caratteristiche >= 6):
    tipo = "A"
elif riscaldamento.startswith("Assente") == False and (servizi.startswith("1)") or servizi.startswith("2)")):
    tipo = "B"
elif servizi.startswith("1)") or servizi.startswith("2)") or servizi.startswith("3)"):
    tipo = "C"
elif servizi.startswith("4)"):
    tipo = "C"
    abbattimento_50 = True
else:
    tipo = "nessuno"

if tipo == "nessuno":
    st.warning("L'alloggio non rientra in nessuno dei tipi A, B o C: l'accordo richiede almeno "
               "impianto idrico idoneo ed efficiente, impianto elettrico a norma e un servizio "
               "igienico con i requisiti del Tipo C")
else:
    st.info(f"Caratteristiche del Tipo A presenti: {n_caratteristiche} su 9 - l'alloggio e' di "
            f"Tipo {tipo}")


if tipo == "A":
    valori = fasce_tipo_A[zona]
    vecchio = anni > 10
elif tipo == "B":
    valori = fasce_tipo_B[zona]
    vecchio = anni > 25
else:
    valori = fasce_tipo_C[zona]
    vecchio = anni > 50

if vecchio == True:
    val_min = valori[0]
    val_max = valori[1]
else:
    val_min = valori[2]
    val_max = valori[3]

if abbattimento_50 == True:
    val_min = val_min * 0.50
    val_max = val_min
    st.caption("Servizio igienico insufficiente o esterno: si applica il 50% del valore minimo.")


st.subheader("Maggiorazioni e riduzioni")

perc_totale = 0.0

if tipo == "B":
    rifinitura = False
    if mq_giardino > mq_utile and mq_utile > 0.0:
        rifinitura = True
    if car_d == True or car_h == True or car_i == True:
        rifinitura = True
    if rifinitura == True:
        magg_pregio = st.checkbox("Tipo B con almeno una rifinitura di pregio: giardino esclusivo "
                                  "piu' grande dell'alloggio, doppi servizi, condizionamento o "
                                  "ascensore (+5%)")
        if magg_pregio == True:
            perc_totale = perc_totale + 0.05

popolare = st.checkbox("Edificio popolare (ex ATER o simili), costruito con piani PEEP o con "
                       "convenzioni o agevolazioni di enti pubblici o istituti previdenziali (-20%)")
if popolare == True:
    perc_totale = perc_totale - 0.20

classe = st.checkbox("Classe energetica A, B o C (+5%)")
if classe == True:
    perc_totale = perc_totale + 0.05

if tipo_contratto.startswith("Contratto agevolato"):
    durata = st.radio("Durata del contratto:", [
        "Tre anni",
        "Quattro anni (+2%)",
        "Cinque anni (+4%)",
        "Sei anni o piu' (+6%)"])
    if durata.startswith("Quattro"):
        perc_totale = perc_totale + 0.02
    elif durata.startswith("Cinque"):
        perc_totale = perc_totale + 0.04
    elif durata.startswith("Sei"):
        perc_totale = perc_totale + 0.06

if tipo_contratto.startswith("Contratto transitorio ordinario"):
    perc_totale = perc_totale + 0.05
    st.caption("Contratto transitorio: le fasce di oscillazione sono aumentate del 5%.")

if tipo_contratto.startswith("Contratto transitorio per studenti"):
    arredo_studenti = st.radio("Arredamento :", [
        "Non ammobiliato, oppure senza tutti gli arredi del punto A",
        "A) Ammobiliato con cucina completa e, per ogni studente, letto, comodino, armadio, "
        "scrivania con sedie, libreria e lampada (+10%)",
        "B) Arredi del punto A piu' almeno due tra divano o due poltrone, televisore, wi-fi, "
        "lavastoviglie, condizionamento (+15%)"])
    if arredo_studenti.startswith("A)"):
        perc_totale = perc_totale + 0.10
    elif arredo_studenti.startswith("B)"):
        perc_totale = perc_totale + 0.15
    breve = st.checkbox("Durata del contratto inferiore a 12 mesi (-10%)")
    if breve == True:
        perc_totale = perc_totale - 0.10
    if localita in localita_lontane:
        perc_totale = perc_totale - 0.10
        st.caption("Localita' troppo distante dalle sedi universitarie: coefficiente correttivo di "
                   "0,9 (Capitolo III, punto 5).")
else:
    arredato = st.checkbox("Unita' immobiliare arredata")
    if arredato == True:
        magg_arredo = st.slider("Aumento per l'arredo concordato in base a quantita' e qualita' (%)",
                                0, 20, 20)
        perc_totale = perc_totale + magg_arredo / 100.0

sociale = st.checkbox("Alloggio sociale: riduzione di almeno il 20% del canone")
if sociale == True:
    perc_totale = perc_totale - 0.20


val_min = val_min + val_min * perc_totale
val_max = val_max + val_max * perc_totale

canone_min = mq_finali * val_min * quota_porzione
canone_max = mq_finali * val_max * quota_porzione

stima = st.button("Stima il canone")

if stima:
    if tipo == "nessuno":
        st.warning("L'alloggio non e' classificabile secondo l'art. 5: il canone non si puo' calcolare")
    elif mq_utile <= 0.0:
        st.warning("Inserire la superficie interna utile per ottenere la stima")
    else:
        st.success(f"Canone mensile stimato: da {canone_min:.2f} euro a {canone_max:.2f} euro")
        if vecchio == True:
            colonna = "edificio piu' vecchio della soglia"
        else:
            colonna = "edificio piu' recente della soglia"
        st.write(f"Zona {zona}, Tipo {tipo}, {colonna} - valori applicati da {val_min:.2f} a "
                 f"{val_max:.2f} euro/mq al mese")
        st.write(f"Percentuale totale di maggiorazioni e riduzioni: {perc_totale * 100:.1f} %")
        if porzione == True:
            st.write(f"Quota della porzione locata sull'intero immobile: {quota_porzione * 100:.1f} %")

