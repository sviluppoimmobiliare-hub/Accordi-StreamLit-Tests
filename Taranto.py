import streamlit as st

valori_aree = {
    "a) Paolo VI": {"A": (1.70, 2.10), "B": (2.20, 3.20), "C": (3.70, 4.90)},
    "b) Tamburi-Croce": {"A": (1.60, 2.20), "B": (2.30, 2.90), "C": (3.30, 4.70)},
    "c) Lido Azzurro": {"A": (1.80, 2.30), "B": (2.40, 2.90), "C": (3.30, 3.80)},
    "d) Isola-Porta Napoli": {"A": (1.30, 1.70), "B": (1.80, 2.80), "C": (3.30, 4.00)},
    "e) San Vito-Lama-Carelli": {"A": (1.90, 2.30), "B": (2.40, 3.80), "C": (4.20, 6.00)},
    "f) Talsano-San Donato": {"A": (1.90, 2.40), "B": (2.50, 3.80), "C": (4.20, 6.00)},
    "g) Salinella-Taranto 2 (contrada Toscano)": {"A": (1.90, 2.30), "B": (2.40, 3.90), "C": (4.30, 5.80)},
    "h) Borgo": {"A": (2.10, 2.80), "B": (2.90, 4.30), "C": (4.70, 6.80)},
    "i) Montegranaro": {"A": (2.20, 2.90), "B": (3.20, 4.10), "C": (4.70, 6.50)},
    "i) Solito Corvisea": {"A": (2.10, 2.90), "B": (3.10, 4.00), "C": (4.40, 5.80)},
    "i) Cesare Battisti": {"A": (2.00, 2.90), "B": (3.00, 3.80), "C": (4.40, 5.50)}
}


st.title("Calcolatore canone concordato - Comune di Taranto")
st.caption("Accordo Territoriale del 19/04/2018, in attuazione della legge 431/98 e del D.M. 16/01/2017. "
           "I valori delle tabelle non sono aggiornati con le variazioni ISTAT successive.")

st.subheader("Generalita'")

tipo_contratto = st.radio("Tipologia contrattuale (art. 10):", [
    "a) Contratto tre + due (art. 2, comma 3)",
    "b) Contratto ad uso transitorio (art. 5, comma 1)",
    "c) Contratto ad uso transitorio per studenti universitari (art. 5, commi 2 e 3)"])

area = st.selectbox(
    "Area omogenea (art. 1):",
    list(valori_aree.keys()),
    help="I confini si intendono sulla linea di mezzeria delle varie strade. Se un edificio e' "
         "attraversato dalla linea di confine, l'intero edificio rientra nella zona di maggiore "
         "valore. L'area Borgo ha come confine corso Due Mari, via Roma, lungomare Vittorio "
         "Emanuele III e viale Virgilio angolo via Leonida e via Pitagora. Le ultime tre voci "
         "sono le tre righe di valori in cui l'Allegato 1 suddivide l'area i) dell'art. 1 "
         "(Italia-Montegranaro; Solito-Corvisea; Tre Carrare-Battisti).")

mq_calpestabili = st.number_input(
    "Superficie calpestabile dell'alloggio in mq (escluse le mura, i palchi morti e tutte le aree "
    "con altezza inferiore a 240 cm)",
    min_value=0.0, step=1.0)


st.subheader("Superficie convenzionale (art. 12)")

mq_autorimessa = st.number_input("Autorimesse ad uso esclusivo - mq (calcolati al 50%)",
                                 min_value=0.0, step=1.0)
mq_posto_auto = st.number_input("Posto macchina in autorimesse di uso comune - mq (calcolati al 20%)",
                                min_value=0.0, step=1.0)
mq_accessori = st.number_input("Balconi, terrazze, cantine e altri accessori simili - mq (calcolati al 25%)",
                               min_value=0.0, step=1.0)
mq_scoperta = st.number_input("Superficie scoperta di pertinenza in godimento esclusivo del conduttore - "
                              "mq (calcolati al 15%)", min_value=0.0, step=1.0)
mq_verde = st.number_input("Superficie condominiale a verde corrispondente alla quota millesimale - "
                           "mq (calcolati al 10%)", min_value=0.0, step=1.0)

mq_convenzionali = (mq_calpestabili
                    + mq_autorimessa * 0.50
                    + mq_posto_auto * 0.20
                    + mq_accessori * 0.25
                    + mq_scoperta * 0.15
                    + mq_verde * 0.10)

mq_finali = mq_convenzionali
if mq_convenzionali <= 38.0:
    mq_finali = mq_convenzionali * 1.20
    if mq_finali > 38.0:
        mq_finali = 38.0
elif mq_convenzionali <= 55.0:
    mq_finali = mq_convenzionali * 1.15
    if mq_finali > 55.0:
        mq_finali = 55.0

st.write(f"Superficie convenzionale: {mq_convenzionali:.2f} mq - superficie di calcolo: {mq_finali:.2f} mq")



st.subheader("Parametri (art. 11)")
st.caption("Gli elementi si considerano solo se installati a spese del proprietario.")

par1 = st.checkbox("1. Tipologia catastale A/1, A/2, A/3, A/7, A/8 o A/9")
par2 = st.checkbox("2. Autorimessa singola o posto auto")
par3 = st.checkbox("3. Ascensore")
par4 = st.checkbox("4. Riscaldamento autonomo o centralizzato")
par5 = st.checkbox("5. Porta blindata o cancello e doppi vetri")
par6 = st.checkbox("6. Impianto di condizionamento")
par7 = st.checkbox("7. Area verde condominiale o esclusiva")
par8 = st.checkbox("8. Doppi servizi")
par9 = st.checkbox("9. Vasca idromassaggio")
par10 = st.checkbox("10. Filodiffusione audio")
par11 = st.checkbox("11. Citofono e/o impianto videocitofonico")
par12 = st.checkbox("12. Cantina")
par13 = st.checkbox("13. Attico o terrazzo o balcone")
par14 = st.checkbox("14. Costruzione completamente ristrutturata nei cinque anni antecedenti alla "
                    "decorrenza del contratto di locazione")
par15 = st.checkbox("15. Allacciamento gas metano")
par16 = st.checkbox("16. Portierato")
par17 = st.checkbox("17. Assenza di barriere architettoniche")
par18 = st.checkbox("18. Classe di efficientamento energetico dell'alloggio di tipo D o superiore")
par19 = st.checkbox("19. Antenna centralizzata")
par20 = st.checkbox("20. Alloggio nuovo completamente ultimato e abitabile entro i dieci anni dalla "
                    "stipula del contratto di acquisto")
par21 = st.checkbox("21. Impianto antincendio condominiale")
par22 = st.checkbox("22. Impianto di allarme")
par23 = st.checkbox("23. Cassetta di sicurezza o cassaforte")
par24 = st.checkbox("24. Autoclave e/o riserva idrica")
par25 = st.checkbox("25. Costruzione post 1990")
par26 = st.checkbox("26. Impianto elettrico a norma certificato")

parametri = [par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13,
             par14, par15, par16, par17, par18, par19, par20, par21, par22, par23, par24, par25, par26]
n_parametri = sum(p for p in parametri if p == True)

if n_parametri <= 5:
    fascia = "A"
elif n_parametri <= 9:
    fascia = "B"
else:
    fascia = "C"

st.info(f"Parametri presenti: {n_parametri} - fascia {fascia}")


st.subheader("Condizioni generali dello stabile (art. 13)")

sta1 = st.checkbox("a) Portone di accesso funzionante con adeguato dispositivo di chiusura e apertura "
                   "da ciascuna unita' immobiliare")
sta2 = st.checkbox("b) Impianto citofonico funzionante")
sta3 = st.checkbox("c) Pavimentazione dell'androne senza evidenti sconnessioni")
sta4 = st.checkbox("d) Rivestimento delle pareti dell'androne e del vano scale senza distacchi di intonaci")
sta5 = st.checkbox("e) Rivestimento dei gradini con alzate e pedate senza marmi con evidenti sconnessioni")
sta6 = st.checkbox("f) Presenza di ringhiere stabili")
sta7 = st.checkbox("g) Finestroni del vano scale funzionanti, senza problemi di chiusura o di "
                   "infiltrazione d'acqua")
sta8 = st.checkbox("h) Funzionalita' delle porte di accesso ai locali condominiali (vano ascensore, "
                   "autoclave, sala riunioni e simili)")
sta9 = st.checkbox("i) Assenza di barriere architettoniche")
sta10 = st.checkbox("j) Impianti conformi alle normative vigenti")

condizioni_stabile = [sta1, sta2, sta3, sta4, sta5, sta6, sta7, sta8, sta9, sta10]
n_stabile = sum(s for s in condizioni_stabile if s == True)

if n_stabile <= 4:
    stato_stabile = "degrado"
elif n_stabile <= 7:
    stato_stabile = "normali"
else:
    stato_stabile = "pregio"

st.info(f"Condizioni dello stabile presenti: {n_stabile} - stabile in condizioni di {stato_stabile}")

buone_condizioni = st.checkbox(
    "L'alloggio e' in buone condizioni",
    help="L'alloggio si intende in buone condizioni quando ha: pavimentazione in piano, senza "
         "dislivelli e sconnessioni; rivestimenti del vano cucina e del bagno senza distacchi o "
         "mancanze; infissi interni ed esterni muniti di dispositivi di chiusura e apertura "
         "funzionanti; infissi esterni corredati da avvolgibili o altri dispositivi di oscuramento "
         "funzionanti; impianto di adduzione e di scarico dell'acqua funzionante; impianti igienici "
         "presenti nell'appartamento. Il dato serve per l'attestazione di rispondenza e non incide "
         "sul calcolo del canone.")


alloggio_sociale = st.checkbox("Alloggio sociale: il canone non puo' superare i valori della fascia A "
                               "(art. 5)")
if alloggio_sociale == True:
    fascia = "A"

val_min, val_max = valori_aree[area][fascia]


if stato_stabile == "degrado" and fascia == "A":
    val_min = val_min - val_min * 0.05
    val_max = val_max - val_max * 0.05
    st.caption("Stabile in condizioni di degrado: i valori della fascia A sono ridotti del 5%.")
elif stato_stabile == "pregio" and fascia == "C":
    val_min = val_min + val_min * 0.05
    val_max = val_max + val_max * 0.05
    st.caption("Stabile in condizioni di pregio: i valori della fascia C sono aumentati del 5%.")



st.subheader("Condizioni particolari di variazione del canone (art. 15)")

perc_totale = 0.0

pregio_catastale = st.checkbox("a) Immobile di pregio, appartenente alle categorie catastali A/1, A/7, "
                              "A/8 o A/9 (+8% sui valori minimo e massimo)")
if pregio_catastale == True:
    perc_totale = perc_totale + 0.08

arredo = st.radio("b) Arredamento dell'appartamento, a cura e spese della parte locatrice:", [
    "Non arredato",
    "Completamente ammobiliato (aumento fino al 30%)",
    "Parzialmente arredato (aumento fino al 15%)"])
if arredo.startswith("Completamente"):
    perc_arredo = st.slider("Aumento per l'arredo effettivamente concordato (%)", 0, 30, 30)
    perc_totale = perc_totale + perc_arredo / 100.0
elif arredo.startswith("Parzialmente"):
    perc_arredo = st.slider("Aumento per l'arredo effettivamente concordato (%)", 0, 15, 15)
    perc_totale = perc_totale + perc_arredo / 100.0


if tipo_contratto.startswith("a) Contratto tre"):
    st.subheader("Durata contrattuale (art. 2)")
    durata = st.radio("Durata del contratto:", [
        "Tre anni con rinnovo di ulteriori due anni",
        "Quattro anni con rinnovo di ulteriori due anni (aumento fino al 4%)",
        "Cinque anni con rinnovo di ulteriori due anni (aumento fino al 6%)",
        "Sei anni e oltre con rinnovo di ulteriori due anni (aumento fino al 7%)"])
    if durata.startswith("Quattro"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 4, 4)
        perc_totale = perc_totale + magg_durata / 100.0
    elif durata.startswith("Cinque"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 6, 6)
        perc_totale = perc_totale + magg_durata / 100.0
    elif durata.startswith("Sei"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 7, 7)
        perc_totale = perc_totale + magg_durata / 100.0


if tipo_contratto.startswith("c) Contratto"):
    perc_totale = perc_totale - 0.05
    st.caption("Contratto per studenti universitari: al canone si applica una riduzione del 5%.")


st.subheader("Locazione di porzione dell'immobile (art. 12)")

mq_porzione = 0.0
mq_condivisi = 0.0
quota_porzione = 1.0

porzione = st.checkbox("Viene locata solo una porzione dell'immobile")
if porzione == True:
    mq_porzione = st.number_input("Superficie convenzionale della parte locata in via esclusiva - mq",
                                  min_value=0.0, step=1.0)
    mq_condivisi = st.number_input("Superficie convenzionale delle parti e dei servizi condivisi "
                                   "attribuita alla porzione - mq", min_value=0.0, step=1.0)
    if mq_convenzionali > 0.0:
        quota_porzione = (mq_porzione + mq_condivisi) / mq_convenzionali
    if quota_porzione > 1.0:
        quota_porzione = 1.0


canone_base_min = mq_finali * val_min * quota_porzione
canone_base_max = mq_finali * val_max * quota_porzione
canone_min = canone_base_min + canone_base_min * perc_totale
canone_max = canone_base_max + canone_base_max * perc_totale

stima = st.button("Stima il canone")

if stima:
    if mq_calpestabili <= 0.0:
        st.warning("Inserire la superficie calpestabile dell'alloggio per ottenere la stima")
    elif porzione == True and mq_porzione + mq_condivisi <= 0.0:
        st.warning("Inserire la superficie della porzione locata per ottenere la stima")
    else:
        st.success(f"Canone mensile stimato: da {canone_min:.2f} euro a {canone_max:.2f} euro")
        st.write(f"Fascia {fascia}, area {area} - valori applicati da {val_min:.2f} a {val_max:.2f} euro/mq")
        st.write(f"Canone base: da {canone_base_min:.2f} a {canone_base_max:.2f} euro")
        st.write(f"Percentuale totale di variazione applicata: {perc_totale * 100:.1f} %")
        if porzione == True:
            st.write(f"Quota della porzione locata sull'intero alloggio: {quota_porzione * 100:.1f} %")
