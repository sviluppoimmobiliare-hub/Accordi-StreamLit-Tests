import streamlit as st


valori_zone = {
    "B01": (34.56, 143.61), "B02": (34.56, 143.61), "B03": (26.78, 101.94),
    "B04": (35.19, 146.22), "B05": (26.78, 101.94), "B06": (30.98, 124.07),
    "C01": (43.95, 100.07), "C02": (37.20, 117.15), "C03": (37.31, 105.90),
    "C04": (37.20, 121.36), "C05": (34.46, 131.76), "C05A": (40.63, 162.21),
    "C06": (42.15, 168.65), "C09": (37.20, 105.90), "C11": (32.74, 133.08),
    "C12": (32.74, 133.08), "C13": (30.87, 100.62), "C13A": (36.80, 136.83),
    "C14": (43.88, 100.07), "C15": (37.90, 92.77), "C16": (37.90, 92.77),
    "C17": (37.90, 92.77), "C18": (36.01, 92.77), "C19": (37.82, 98.39),
    "C20": (37.20, 98.97), "C20A": (36.69, 117.15), "C21": (36.01, 92.77),
    "C22": (39.62, 103.99), "C23": (36.01, 92.77), "C24": (39.62, 103.99),
    "D01": (41.20, 97.95), "D02": (33.29, 82.75), "D03": (37.00, 93.45),
    "D04": (37.00, 93.45), "D05": (37.00, 93.45), "D06": (37.00, 93.45),
    "D07": (37.00, 93.45), "D08": (37.00, 93.45), "D09": (37.00, 83.17),
    "D10": (37.00, 83.17), "D11": (37.00, 83.17), "D12": (37.00, 93.45),
    "D13": (37.20, 116.68), "D14": (37.31, 97.95), "D15": (41.20, 97.95),
    "D16": (37.20, 116.68), "D17": (37.20, 116.68), "D18": (34.46, 131.76),
    "D20": (34.46, 162.21), "D21": (34.46, 137.02), "D22": (42.16, 176.44),
    "D23": (36.01, 92.77), "D24": (42.16, 176.44), "D25": (37.90, 88.25),
    "D26": (37.90, 88.25), "D27": (36.00, 75.71), "D28": (37.90, 88.25),
    "D29": (37.90, 88.25), "D30": (36.00, 75.71), "D31": (37.90, 88.25),
    "D32": (37.90, 88.25), "D33": (41.20, 91.64), "D34": (41.20, 91.64),
    "D35": (41.20, 91.64), "D36": (41.20, 91.64), "D37": (41.20, 91.64),
    "D38": (41.20, 91.64), "D39": (41.20, 91.64), "D40": (39.14, 109.61),
    "D41": (39.14, 89.06), "D41A": (39.14, 109.61), "D42": (39.14, 109.61),
    "D43": (39.14, 99.54), "D44": (31.32, 85.20), "D45": (39.14, 95.60),
    "D46": (31.32, 85.20), "D47": (36.41, 89.28), "D48": (37.90, 88.35),
    "D49": (39.14, 95.60), "E1": (37.90, 88.25), "R1": (33.29, 82.75),
    "R2": (31.32, 92.23), "R3": (39.00, 82.49), "R5": (34.95, 79.33),
    "R6": (39.00, 82.49)
}

zone_da_verificare = ["D41", "D41A", "D47", "D48", "D49"]


st.title("Calcolatore canone concordato - Comune di Genova")


st.subheader("Generalita'")

tipo_contratto = st.radio("Tipologia contrattuale:", [
    "Contratto agevolato 3 + 2",
    "Contratto transitorio ordinario",
    "Contratto transitorio per studenti universitari "])

zona = st.selectbox("Zona (zonizzazione del Geoportale del Comune di Genova):",
                    list(valori_zone.keys()))

if zona in zone_da_verificare:
    st.warning("Il valore massimo di questa zona e' parzialmente coperto da un timbro nella "
               )

piano = st.number_input("Piano dell'appartamento (0 per il piano terra)",
                        min_value=0, max_value=40, value=1, step=1)

st.subheader("Superficie")

metodo = st.radio("Come viene determinata la superficie:", [
    "Superficie catastale risultante dalla visura aggiornata",
    "Calcolo secondo i criteri dell'Allegato 3"])

if metodo.startswith("Superficie catastale"):
    mq_convenzionali = st.number_input("Superficie catastale da visura - mq", min_value=0.0, step=1.0)
else:
    mq_principali = st.number_input("Vani principali e vani accessori a servizio diretto: bagni, "
                                    "ripostigli, ingressi, corridoi e simili - mq (calcolati al 100%)",
                                    min_value=0.0, step=1.0,
                                    help="Non entrano nel computo i locali con altezza utile inferiore "
                                         "a 1,50 m. Le scale e le rampe interne si computano in misura "
                                         "pari alla loro proiezione orizzontale.")
    da_ape = st.checkbox("La superficie deriva dall'Attestato di Prestazione Energetica e va "
                         "maggiorata del 20%")
    if da_ape == True:
        mq_principali = mq_principali * 1.20

    mq_cantine = st.number_input("Vani accessori a servizio indiretto: soffitte, cantine e simili - mq",
                                 min_value=0.0, step=1.0)
    cantine_comunicanti = st.checkbox("Le cantine e le soffitte sono comunicanti con i vani principali "
                                      "(50% invece del 25%)")
    if cantine_comunicanti == True:
        mq_cantine_conv = mq_cantine * 0.50
    else:
        mq_cantine_conv = mq_cantine * 0.25

    mq_balconi = st.number_input("Balconi, terrazze e simili di pertinenza esclusiva - mq",
                                 min_value=0.0, step=1.0)
    balconi_comunicanti = st.checkbox("I balconi e le terrazze sono comunicanti con i vani principali "
                                      "(30% e 10% invece del 15% e 5%)")
    if balconi_comunicanti == True:
        prima_quota = 0.30
        seconda_quota = 0.10
    else:
        prima_quota = 0.15
        seconda_quota = 0.05
    if mq_balconi <= 25.0:
        mq_balconi_conv = mq_balconi * prima_quota
    else:
        mq_balconi_conv = 25.0 * prima_quota + (mq_balconi - 25.0) * seconda_quota

    mq_scoperta = st.number_input("Area scoperta o assimilabile di pertinenza esclusiva, compreso il "
                                  "posto auto scoperto - mq", min_value=0.0, step=1.0)
    if mq_scoperta <= mq_principali:
        mq_scoperta_conv = mq_scoperta * 0.10
    else:
        mq_scoperta_conv = mq_principali * 0.10 + (mq_scoperta - mq_principali) * 0.02

    mq_autorimessa = st.number_input("Box o autorimessa di pertinenza esclusiva - mq (calcolati al 50%)",
                                     min_value=0.0, step=1.0)

    mq_convenzionali = (mq_principali + mq_cantine_conv + mq_balconi_conv
                        + mq_scoperta_conv + mq_autorimessa * 0.50)

porzione = st.checkbox("Viene locata solo una porzione dell'immobile")

if porzione == True:
    mq_porzione = st.number_input("Mq della porzione locata", min_value=0.0, step=1.0)
    mq_parti_comuni = st.number_input("Mq della quota di parti, accessori e servizi condivisi",
                                      min_value=0.0, step=1.0)
    mq_finali = mq_porzione + mq_parti_comuni
    st.caption("In caso di locazione di porzione di immobile gli incrementi di superficie non si "
               "applicano. La somma dei canoni delle diverse porzioni non puo' superare il canone "
               "calcolato per l'intero immobile.")
else:
    mq_porzione = 0.0
    mq_finali = mq_convenzionali
    if mq_convenzionali < 45.0:
        mq_finali = mq_convenzionali * 1.30
        if mq_finali > 54.0:
            mq_finali = 54.0
    elif mq_convenzionali <= 60.0:
        mq_finali = mq_convenzionali * 1.20
        if mq_finali > 67.0:
            mq_finali = 67.0
    elif mq_convenzionali >= 61.0 and mq_convenzionali <= 69.0:
        mq_finali = mq_convenzionali * 1.10
        if mq_finali > 70.0:
            mq_finali = 70.0
    elif mq_convenzionali > 100.0:
        mq_finali = 100.0 + (mq_convenzionali - 100.0) * 0.70

st.write(f"Superficie convenzionale: {mq_convenzionali:.2f} mq - superficie di calcolo: {mq_finali:.2f} mq")


st.subheader("Elementi caratteristici")

el1 = True
if piano > 1:
    el1 = st.checkbox("1. Impianto di ascensore")
else:
    st.write("1. Impianto di ascensore: caratteristica considerata presente per gli alloggi ubicati "
             "non oltre il primo piano")

el2 = st.checkbox("2. Impianto di riscaldamento centralizzato, autonomo, a piastre radianti o a pompa "
                  "di calore (obbligatorio per le sottofasce superiori alla prima)")
el3 = st.checkbox("3. Impianto di raffrescamento")
el4 = st.checkbox("4. Servizio igienico con doccia o vasca da bagno (obbligatorio per le sottofasce "
                  "superiori alla prima)")
el5 = st.checkbox("5. Balcone con profondita' minima di 0,80 m, oppure terrazzo o giardino "
                  "pertinenziale di superficie almeno pari a 10 mq")
el6 = st.checkbox("6. Doppi servizi igienici")
el7 = st.checkbox("7. Doppi vetri ad almeno il 90% delle finestre e/o porta blindata")
el8 = st.checkbox("8. Cantina e/o soffitta")
el9 = st.checkbox("9. Servizio di portineria")
el10 = st.checkbox("10. Area verde di uso comune di superficie almeno pari al triplo della superficie "
                   "coperta dell'immobile, oppure impianto sportivo")
el11 = st.checkbox("11. Strutture o interventi atti al superamento delle barriere architettoniche nel "
                   "condominio")
el12 = st.checkbox("12. Spazio scoperto condominiale per posteggio di uso comune, in numero pari ad "
                   "almeno il 50% delle unita' immobiliari del condominio")
el13 = st.checkbox("13. Box pertinenziale e/o posto auto esclusivo")
el14 = st.checkbox("14. Classe energetica da certificazione APE da A sino a D comprese")
el15 = st.checkbox("15. Edificio ultimato da non oltre 10 anni")
el16 = st.checkbox("16. Edificio oggetto di integrale ristrutturazione (L. 457/78, art. 31 lett. c), "
                   "ultimato da non oltre 10 anni")
el17 = st.checkbox("17. Intervento di manutenzione straordinaria del fabbricato (L. 457/78, art. 31 "
                   "lett. b), ultimato da non oltre 10 anni")
el18 = st.checkbox("18. Ristrutturazione interna (L. 457/78, art. 31 lett. b) o rifacimento integrale "
                   "di bagno e cucina, esclusi gli impianti, ultimati da non oltre 10 anni")
el19 = st.checkbox("19. Esposizione a levante/mezzogiorno o mezzogiorno/ponente di almeno la meta' dei "
                   "vani, esclusi i servizi e i cavedi")
el20 = st.checkbox("20. Vista mare da almeno due finestre")
el21 = st.checkbox("21. Distanza dal mare inferiore a 300 m")

elementi = [el1, el2, el3, el4, el5, el6, el7, el8, el9, el10, el11,
            el12, el13, el14, el15, el16, el17, el18, el19, el20, el21]
n_elementi = sum(e for e in elementi if e == True)

if el2 == False or el4 == False:
    sottofascia = 1
elif n_elementi >= 9:
    sottofascia = 3
elif n_elementi >= 3:
    sottofascia = 2
else:
    sottofascia = 1

if (el2 == False or el4 == False) and n_elementi >= 3:
    st.info(f"Elementi presenti: {n_elementi} su 21 - prima sottofascia: mancano l'elemento 2 e/o "
            f"l'elemento 4, obbligatori per accedere alle sottofasce superiori")
else:
    st.info(f"Elementi presenti: {n_elementi} su 21 - sottofascia {sottofascia}")


zona_min, zona_max = valori_zone[zona]
ampiezza = (zona_max - zona_min) / 3.0

if sottofascia == 1:
    val_min = zona_min
    val_max = zona_min + ampiezza
elif sottofascia == 2:
    val_min = zona_min + ampiezza
    val_max = zona_min + ampiezza * 2.0
else:
    val_min = zona_min + ampiezza * 2.0
    val_max = zona_max

st.subheader("Maggiorazioni")

perc_totale = 0.0

arredo = st.radio("Arredamento:", [
    "Non arredato",
    "Parzialmente arredato (+6%)",
    "Completamente arredato (+12%)"],
    help="Per completamente arredato si intende l'alloggio fornito in tutti i vani di mobilio "
         "efficiente e funzionante: cucina o angolo cottura con mobili contenitori, tavolo, sedie, "
         "frigorifero e piano cottura; camere con armadio e letti completi di materassi; adeguati "
         "apparati di illuminazione in tutti gli ambienti; lavabiancheria. Per parzialmente arredato "
         "devono risultare arredati almeno la cucina o angolo cottura e la meta' dei restanti vani utili.")
perc_arredo = 0.0
if arredo.startswith("Parzialmente"):
    perc_arredo = 0.06
elif arredo.startswith("Completamente"):
    perc_arredo = 0.12

if tipo_contratto.startswith("Contratto transitorio ordinario"):
    perc_base = 0.10 + perc_arredo
    if perc_base > 0.16:
        perc_base = 0.16
        st.caption("L'aumento del 10% previsto per i contratti transitori sommato a quello per "
                   "l'arredo e' stato limitato al 16% complessivo.")
    perc_totale = perc_totale + perc_base
else:
    perc_totale = perc_totale + perc_arredo

if tipo_contratto.startswith("Contratto agevolato"):
    durata = st.radio("Durata contrattuale :", [
        "Tre anni piu' due",
        "Quattro anni piu' due (+2%)",
        "Cinque anni piu' due (+4%)",
        "Sei anni piu' due (+6%)"])
    if durata.startswith("Quattro"):
        perc_totale = perc_totale + 0.02
    elif durata.startswith("Cinque"):
        perc_totale = perc_totale + 0.04
    elif durata.startswith("Sei"):
        perc_totale = perc_totale + 0.06
else:
    st.caption("La maggiorazione per la durata non si applica: il punto 4 e' escluso per "
               "i contratti transitori ordinari e per quelli per studenti universitari.")

vincolo = st.radio("Immobili vincolati:", [
    "Nessun vincolo",
    "Il vincolo riguarda solo il fabbricato (+15%)",
    "Il vincolo riguarda specificamente l'appartamento locato (+30%)"],
    help="Riguarda gli immobili di cui all'art. 1 comma 2 lettera a) della L. 431/98, soggetti ai "
         "vincoli della L. 1089/1939 o inclusi nelle categorie catastali A/1, A/8 e A/9. Queste "
         "maggiorazioni si sommano a quelle per maggior durata e arredo.")
if vincolo.startswith("Il vincolo riguarda solo"):
    perc_totale = perc_totale + 0.15
elif vincolo.startswith("Il vincolo riguarda specificamente"):
    perc_totale = perc_totale + 0.30


val_min = val_min + val_min * perc_totale
val_max = val_max + val_max * perc_totale
minimo_assoluto = zona_min + zona_min * perc_totale

canone_annuo_min = mq_finali * val_min
canone_annuo_max = mq_finali * val_max
canone_minimo_assoluto = mq_finali * minimo_assoluto

stima = st.button("Stima il canone")

if stima:
    if porzione == False and mq_convenzionali <= 0.0:
        st.warning("Inserire la superficie dell'immobile per ottenere la stima")
    elif porzione == True and mq_finali <= 0.0:
        st.warning("Inserire la superficie della porzione locata per ottenere la stima")
    else:
        st.success(f"Canone mensile stimato: da {canone_annuo_min / 12.0:.2f} euro a "
                   f"{canone_annuo_max / 12.0:.2f} euro")
        st.write(f"Canone annuo: da {canone_annuo_min:.2f} a {canone_annuo_max:.2f} euro")
        st.write(f"Zona {zona}, sottofascia {sottofascia} - valori annui applicati da {val_min:.2f} a "
                 f"{val_max:.2f} euro/mq")
        st.write(f"Percentuale totale di maggiorazione applicata: {perc_totale * 100:.1f} %")
        st.write(f"Limite minimo assoluto della zona: {canone_minimo_assoluto / 12.0:.2f} euro al mese "
                 f"({minimo_assoluto:.2f} euro/mq annui)")
        st.caption("Il canone non puo' eccedere il valore massimo della sottofascia, mentre e' "
                   "consentito concordare un valore inferiore al minimo della sottofascia purche' non "
                   "inferiore al limite minimo assoluto della zona.")
