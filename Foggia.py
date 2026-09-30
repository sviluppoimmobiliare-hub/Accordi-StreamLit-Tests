import streamlit as st


valori_zone = {
    "Zona 1": {"A+": (1.61, 5.35), "A": (1.34, 4.46), "B": (1.24, 4.18), "C": (0.83, 3.07)},
    "Zona 2": {"A+": (1.49, 5.02), "A": (1.24, 4.18), "B": (1.14, 3.91), "C": (0.72, 2.79)},
    "Zona 3": {"A+": (1.37, 4.69), "A": (1.14, 3.91), "B": (1.03, 3.36), "C": (0.62, 2.51)},
    "Zona 4": {"A+": (0.86, 3.35), "A": (0.72, 2.79), "B": (0.62, 2.51), "C": (0.31, 1.95)}
}


confini_zone = {
    "Zona 1": "Area interna delimitata da: piazza Cavour, via Scillitani sino all'incrocio con via "
              "Montegrappa, via del Carso, via Re di Puglia, piazza Vittorio Veneto, via Manfredi, "
              "via Sant'Antonio, via Sant'Alfonso Maria de' Liguori sino all'incrocio con viale "
              "Candelaro, viale Candelaro, viale Ofanto sino all'incrocio con via Guglielmi, via "
              "Guglielmi, via Caggese sino all'incrocio con via Galliani, via Galliani verso piazza "
              "Cavour.",
    "Zona 2": "Dalla perimetrazione di viale Candelaro, viale Giotto sino all'incrocio con via "
              "Altamura, via Altamura, via Rovelli, via L. Perosi, via Martiri di via Fani, via P. "
              "Telesforo, via Natola, viale I Maggio, via degli Aviatori sino all'incrocio con via "
              "Einaudi, via Einaudi, via D'Addedda sino all'incrocio con via Lenotti, via Lenotti, "
              "via Smaldone sino all'incrocio con corso del Mezzogiorno, corso del Mezzogiorno "
              "verso viale Ofanto.",
    "Zona 3": "Tutte le vie restanti non ricomprese nella zona 1 e nella zona 2.",
    "Zona 4": "Zona agricola e frazioni."
}


st.title("Calcolatore canone concordato - Comune di Foggia")
st.caption("Accordo Territoriale sottoscritto il 06/03/2020 e depositato il 09/03/2020, che annulla e "
           "sostituisce quello del 28/10/2005. I valori delle tabelle non sono aggiornati con le "
           "variazioni ISTAT successive.")

st.subheader("Generalita'")

tipo_contratto = st.radio("Tipologia contrattuale:", [
    "Contratto agevolato (art. 2, comma 3) - allegato A",
    "Contratto transitorio ordinario (art. 5, comma 1) - allegato B",
    "Contratto transitorio per studenti universitari (art. 5, commi 2 e 3) - allegato C"])

zona = st.selectbox("Zona (Allegato 1):", list(valori_zone.keys()),
                    help="Se l'immobile ricade sulla linea di confine tra due zone si prende in "
                         "considerazione quella di maggior valore (punto 2 dell'accordo).")
st.caption(confini_zone[zona])

piano = st.number_input("Piano dell'appartamento (0 per il piano terra)",
                        min_value=0, max_value=30, value=1, step=1)
rialzato_giardino = st.checkbox("Piano rialzato con giardino")

mq_calpestabili = st.number_input("Superficie netta calpestabile dell'immobile in mq",
                                  min_value=0.0, step=1.0)



st.subheader("Superficie convenzionale (punto 6)")

mq_garage = st.number_input("Garage, box e posti auto accatastati - mq (calcolati al 50%)",
                            min_value=0.0, step=1.0)
mq_accessori = st.number_input("Terrazzi, balconi, lavanderie, cantine, porticati, verande, "
                               "ripostigli, tavernette e mansarde - mq (calcolati al 25%)",
                               min_value=0.0, step=1.0)
mq_posti_auto = st.number_input("Posti auto non accatastati ma assegnati da regolamento o delibera "
                                "condominiale - mq (calcolati al 20%)", min_value=0.0, step=1.0)
mq_verde = st.number_input("Verde e cortile in condominio, quota millesimale - mq (calcolati al 10%)",
                           min_value=0.0, step=1.0)

mq_convenzionali = (mq_calpestabili
                    + mq_garage * 0.50
                    + mq_accessori * 0.25
                    + mq_posti_auto * 0.20
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
elif mq_convenzionali <= 70.0:
    mq_finali = mq_convenzionali * 1.10
    if mq_finali > 70.0:
        mq_finali = 70.0

st.write(f"Superficie convenzionale: {mq_convenzionali:.2f} mq - superficie di calcolo: {mq_finali:.2f} mq")



st.subheader("Elementi essenziali (punto 4)")

ess1 = False
if piano >= 1 or rialzato_giardino == True:
    ess1 = True
if ess1 == True:
    st.write("Appartamento dal primo piano in poi o piano rialzato con giardino: elemento presente")
else:
    st.write("Appartamento dal primo piano in poi o piano rialzato con giardino: elemento assente")

ess2 = st.checkbox("Impianto di riscaldamento autonomo o centralizzato, ovvero impianto termico come "
                   "definito dalla L. 90/2013 e successive modificazioni")

ess3 = True
if piano > 2:
    ess3 = st.checkbox("Presenza di ascensore")
else:
    st.write("Ascensore: non richiesto per gli appartamenti fino al secondo piano")

elementi_essenziali = [ess1, ess2, ess3]
n_essenziali = sum(e for e in elementi_essenziali if e == True)



st.subheader("Elementi non essenziali (punto 4)")

nes1 = st.checkbox("1. Piano intermedio o piano rialzato con giardino",
                   help="L'accordo non definisce cosa si intenda per piano intermedio: la voce e' "
                        "lasciata alla valutazione delle parti.")
nes2 = st.checkbox("2. Presenza di condizionamento su almeno il 50% dei vani")
nes3 = st.checkbox("3. Doppio servizio")
nes4 = st.checkbox("4. Posto auto scoperto assegnato da delibera condominiale o box")
nes5 = st.checkbox("5. Doppia esposizione")
nes6 = st.checkbox("6. Cortile comune")
nes7 = st.checkbox("7. Cantina o soffitta")
nes8 = st.checkbox("8. Assenza totale di barriere architettoniche nell'edificio (L. 13/1989)")
nes9 = st.checkbox("9. Doppi vetri, vetri termici o doppi infissi su almeno il 50% dell'abitazione")
nes10 = st.checkbox("10. Sbarre anti-intrusione agli infissi su almeno il 50% dell'abitazione")
nes11 = st.checkbox("11. Porta blindata")
nes12 = st.checkbox("12. Sistema di allarme singolo e/o videocamera e/o impianti di sicurezza e/o "
                    "automazione (domotica)")
nes13 = st.checkbox("13. Impianto di videocitofono")
nes14 = st.checkbox("14. Copertura in fibra ottica")
nes15 = st.checkbox("15. Presenza di autoclave e/o riserva idrica condominiale o autonoma")
nes16 = st.checkbox("16. Dotazioni di fonti energetiche rinnovabili")
nes17 = st.checkbox("17. Terrazzo o giardino ad uso esclusivo di superficie non inferiore al 20% "
                    "dell'unita' immobiliare")

elementi_non_essenziali = [nes1, nes2, nes3, nes4, nes5, nes6, nes7, nes8, nes9, nes10, nes11,
                           nes12, nes13, nes14, nes15, nes16, nes17]
n_non_essenziali = sum(n for n in elementi_non_essenziali if n == True)

if n_essenziali < 3:
    fascia = "C"
elif n_non_essenziali >= 10:
    fascia = "A+"
elif n_non_essenziali >= 5:
    fascia = "A"
elif n_non_essenziali >= 1:
    fascia = "B"
else:
    fascia = "C"

st.info(f"Elementi essenziali presenti: {n_essenziali} su 3 - elementi non essenziali presenti: "
        f"{n_non_essenziali} su 17 - fascia {fascia}")



val_min, val_max = valori_zone[zona][fascia]


if tipo_contratto.startswith("Contratto transitorio per studenti"):
    immobile_vincolato = st.checkbox("Immobile di cui all'art. 1, comma 2, lettera a) della L. 431/98: "
                                     "i valori minimo e massimo aumentano del 5%")
    if immobile_vincolato == True:
        val_min = val_min + val_min * 0.05
        val_max = val_max + val_max * 0.05



st.subheader("Maggiorazioni (punto 8)")

moltiplicatore = 1.0

if tipo_contratto.startswith("Contratto agevolato"):
    durata = st.radio("Durata contrattuale:", [
        "Tre anni piu' due",
        "Quattro anni (aumento fino al 2%)",
        "Cinque anni (aumento fino al 4%)",
        "Sei anni o piu' (aumento fino al 6%)"])
    if durata.startswith("Quattro"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 2, 2)
        moltiplicatore = moltiplicatore * (1.0 + magg_durata / 100.0)
    elif durata.startswith("Cinque"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 4, 4)
        moltiplicatore = moltiplicatore * (1.0 + magg_durata / 100.0)
    elif durata.startswith("Sei"):
        magg_durata = st.slider("Aumento per la durata effettivamente concordato (%)", 0, 6, 6)
        moltiplicatore = moltiplicatore * (1.0 + magg_durata / 100.0)
else:
    st.caption("La maggiorazione per la durata non si applica: i contratti transitori ordinari durano "
               "al massimo diciotto mesi e quelli per studenti al massimo tre anni.")

arredo = st.radio("Arredamento:", [
    "Non ammobiliato",
    "Parzialmente ammobiliato con blocco cucina (aumento fino al 10%)",
    "Completamente ammobiliato (aumento fino al 20%)"],
    help="Si intende completamente ammobiliato l'immobile il cui arredo comprende i vani letto, il "
         "soggiorno, il bagno e la cucina, quest'ultima comprensiva di piano cottura, forno, "
         "frigorifero e lavatrice. Gli elettrodomestici devono essere efficienti e funzionali, "
         "televisore compreso.")
if arredo.startswith("Parzialmente"):
    magg_arredo = st.slider("Aumento per l'arredo effettivamente concordato (%)", 0, 10, 10)
    moltiplicatore = moltiplicatore * (1.0 + magg_arredo / 100.0)
elif arredo.startswith("Completamente"):
    magg_arredo = st.slider("Aumento per l'arredo effettivamente concordato (%)", 0, 20, 20)
    moltiplicatore = moltiplicatore * (1.0 + magg_arredo / 100.0)

classe = st.radio("Classe energetica:", [
    "E o inferiore (nessun aumento)",
    "D (+3%)",
    "C (+4%)",
    "B (+6%)",
    "A1, A2, A3 o A4 (+8%)"])
if classe.startswith("D "):
    moltiplicatore = moltiplicatore * 1.03
elif classe.startswith("C "):
    moltiplicatore = moltiplicatore * 1.04
elif classe.startswith("B "):
    moltiplicatore = moltiplicatore * 1.06
elif classe.startswith("A1"):
    moltiplicatore = moltiplicatore * 1.08



st.subheader("Locazione di porzione di immobile (punto 7)")

quota_porzione = 1.0
porzione = st.checkbox("Viene locata solo una porzione dell'immobile")
if porzione == True:
    mq_vani_locati = st.number_input("Superficie convenzionale dei vani ad uso esclusivo concessi in "
                                     "locazione - mq", min_value=0.0, step=1.0)
    mq_condivisi_totali = st.number_input("Superficie convenzionale totale delle parti e dei servizi "
                                          "condivisi - mq", min_value=0.0, step=1.0)
    vani_locati = st.number_input("Numero di vani ad uso esclusivo concessi in locazione",
                                  min_value=0, max_value=30, value=1, step=1)
    vani_totali = st.number_input("Numero totale di vani disponibili",
                                  min_value=1, max_value=30, value=1, step=1)
    mq_condivisi = mq_condivisi_totali * vani_locati / vani_totali
    if mq_convenzionali > 0.0:
        quota_porzione = (mq_vani_locati + mq_condivisi) / mq_convenzionali
    if quota_porzione > 1.0:
        quota_porzione = 1.0


canone_base_min = mq_finali * val_min * quota_porzione
canone_base_max = mq_finali * val_max * quota_porzione
canone_min = canone_base_min * moltiplicatore
canone_max = canone_base_max * moltiplicatore

stima = st.button("Stima il canone")

if stima:
    if mq_calpestabili <= 0.0:
        st.warning("Inserire la superficie netta calpestabile per ottenere la stima")
    elif porzione == True and mq_vani_locati <= 0.0:
        st.warning("Inserire la superficie dei vani locati per ottenere la stima")
    else:
        st.success(f"Canone mensile stimato: da {canone_min:.2f} euro a {canone_max:.2f} euro")
        st.write(f"{zona}, fascia {fascia} - valori applicati da {val_min:.2f} a {val_max:.2f} euro/mq")
        st.write(f"Canone base: da {canone_base_min:.2f} a {canone_base_max:.2f} euro")
        st.write(f"Moltiplicatore delle maggiorazioni progressive: {moltiplicatore:.4f} "
                 f"(pari a un aumento complessivo del {(moltiplicatore - 1.0) * 100:.2f} %)")
        if porzione == True:
            st.write(f"Quota della porzione locata sull'intero appartamento: {quota_porzione * 100:.1f} %")
