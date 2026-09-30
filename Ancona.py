import streamlit as st

st.title("Calcolatore Canone Concordato - Comune di Ancona")



zone_ancona = {
    "CENTRO e PREGIO": "Passetto - Rione Adriatico - C.so Garibaldi - C.so Matteotti - S. Margherita - "
                       "V.le Vittoria (B1) - Rione San Pietro - Cardeto - Capodimonte (B2) - "
                       "Santo Stefano - Borgo Rodi (B3) - Pietralacroce (D4)",
    "SEMICENTRO (C3-D1-D2-C4)": "Palombare - Pinocchio - Posatora (C3) - B. Bianche - Monte Dago - "
                                "Ponterosso - Passo Varano - Q1 - Q2 (D1) - Torrette - Palombina - "
                                "Collemarino (D2) - Grazie - Tavernelle (C4)",
    "SEMICENTRO (C1-C2-B7)": "Piano S. Lazzaro - M. d. Resistenza - Rione Archi (C1-C2) - "
                             "Rione Monte Marino - Rione Montirozzo (B7)",
    "PERIFERICA-SUBURBANA": "Loc. Candia - Baraccola (D5-E5)",
    "AGRICOLA EST": "Frazioni del Parco Conero - Varano - Montacuto - Poggio - Massignano (R1)",
    "AGRICOLA OVEST": "Altre frazioni - Aspio - Montesicuro - Sappanico - Paterno - Gallignano (R2)"
}


fasce_ancona = {
    "CENTRO e PREGIO":          {"Inferiore": 80.0, "Media": 90.0, "Superiore": 100.0},
    "SEMICENTRO (C3-D1-D2-C4)": {"Inferiore": 70.0, "Media": 80.0, "Superiore": 90.0},
    "SEMICENTRO (C1-C2-B7)":    {"Inferiore": 65.0, "Media": 75.0, "Superiore": 85.0},
    "PERIFERICA-SUBURBANA":     {"Inferiore": 60.0, "Media": 70.0, "Superiore": 80.0},
    "AGRICOLA EST":             {"Inferiore": 50.0, "Media": 60.0, "Superiore": 70.0},
    "AGRICOLA OVEST":           {"Inferiore": 40.0, "Media": 50.0, "Superiore": 60.0}
}

zona = st.selectbox("Selezionare la zona", list(zone_ancona.keys()))
st.caption(zone_ancona[zona])

st.subheader("Superficie convenzionale ")
sup_calp = st.number_input("a - Superficie calpestabile dei vani principali e degli accessori a servizio diretto, "
                           "al netto dei muri perimetrali ed interni (mq)", min_value=0.0)
sup_acc_com = st.number_input("b - Vani accessori a servizio indiretto (soffitte, cantine e simili) COMUNICANTI "
                              "con i vani principali e di caratteristiche omogenee (conteggiati al 30%)",
                              min_value=0.0,
                              help="La parte con altezza inferiore a m 1,70 va prima computata al 30%.")
sup_acc_non = st.number_input("b - Vani accessori a servizio indiretto NON comunicanti (conteggiati al 25%)",
                              min_value=0.0,
                              help="La parte con altezza inferiore a m 1,70 va prima computata al 30%.")
sup_balc_com = st.number_input("c - Balconi, terrazze e simili di pertinenza esclusiva COMUNICANTI "
                               "(conteggiati al 25%)", min_value=0.0)
sup_balc_non = st.number_input("c - Balconi, terrazze e simili di pertinenza esclusiva NON comunicanti "
                               "(conteggiati al 10%)", min_value=0.0)
sup_verde = st.number_input("d - Aree scoperte a verde in godimento esclusivo (10% fino alla superficie "
                            "convenzionale di cui al punto a, 2% oltre)", min_value=0.0)
sup_garage = st.number_input("e - Posto auto coperto o garage ad uso esclusivo (conteggiato al 50%)", min_value=0.0)
sup_posto_scop = st.number_input("f - Posto auto scoperto condominiale assegnato (conteggiato al 20%)", min_value=0.0)

if 0 < sup_calp < 46:
    quota_a = sup_calp * 1.30                                   
elif 46 <= sup_calp < 65:
    quota_a = sup_calp * (65 - sup_calp) / 65 + sup_calp        
elif sup_calp > 95:
    quota_a = 95 + (sup_calp - 95) * 0.50                       
else:
    quota_a = sup_calp


if sup_verde <= quota_a:
    quota_verde = sup_verde * 0.10
else:
    quota_verde = quota_a * 0.10 + (sup_verde - quota_a) * 0.02

superficie_convenzionale = (quota_a + sup_acc_com * 0.30 + sup_acc_non * 0.25 +
                            sup_balc_com * 0.25 + sup_balc_non * 0.10 +
                            quota_verde + sup_garage * 0.50 + sup_posto_scop * 0.20)

st.info(f"Superficie convenzionale: {superficie_convenzionale:.2f} mq")

st.subheader("a) Dotazione di pertinenze (max 21 punti)")
pertinenze = [
    ("Garage in uso esclusivo", 5),
    ("Posto auto coperto riservato", 3),
    ("Posto auto scoperto riservato", 2),
    ("Cantina di superficie di almeno 4 mq", 3),
    ("Soffitta praticabile di superficie di almeno 4 mq", 2),
    ("Ripostiglio esterno, sottoscala, soffitta o cantina di superficie inferiore a 4 mq", 1),
    ("Area a verde in godimento esclusivo", 2),
    ("Lavatoio o stenditoio in godimento esclusivo", 1)
]
punti_a = 0
for label, punti in pertinenze:
    if st.checkbox(label):
        punti_a += punti

balconi = st.radio("Balconi, terrazze o lastrici solari in uso esclusivo", [
    "Assenti",
    "Balconi/terrazzi/lastrico solare di superficie complessiva inferiore a 10 mq (+1)",
    "Terrazza o lastrico solare, o piu' balconi per una superficie totale maggiore di 10 mq (+2)"
])
if "(+1)" in balconi:
    punti_a += 1
elif "(+2)" in balconi:
    punti_a += 2

st.subheader("Stato di conservazione dell'immobile e degli impianti (max 12 punti)")
st.caption("2 = buone o nuove; 1 = normali o discrete, in ogni caso funzionanti; "
           "0 = mediocri o scadenti, difettose o deteriorate")
elementi_conservazione = ["Pavimenti",
                          "Pareti, soffitti e tinteggiatura",
                          "Infissi",
                          "Impianto idrico e servizi igienici e sanitari",
                          "Accessi, scale, ascensore",
                          "Facciate, coperture e parti comuni in genere"]
punti_b = 0
for elemento in elementi_conservazione:
    scelta = st.selectbox(elemento, ["Buone o nuove (2)", "Normali o discrete (1)", "Mediocri o scadenti (0)"],
                          index=1)
    if scelta.startswith("Buone"):
        punti_b += 2
    elif scelta.startswith("Normali"):
        punti_b += 1

st.subheader("c) Dotazione di servizi e accessori (max 28 punti)")
servizi = [
    ("Ascensore", 2),
    ("Assenza di barriere architettoniche nell'edificio (L. 13/1989)", 2),
    ("Assenza di barriere architettoniche nell'abitazione (L. 13/1989)", 1),
    ("Riscaldamento autonomo o contabilizzato", 1),
    ("Doppi vetri, vetri termici o doppie finestre su almeno il 50% degli infissi", 1),
    ("Cucina abitabile (superficie minima 9 mq piu' finestra)", 2),
    ("Doppi servizi", 3),
    ("Porta blindata e/o barre anti-intrusione a infissi", 1),
    ("Sistema di allarme singolo e/o videocamera e/o impianti di sicurezza/domotica", 2),
    ("Sistema di allarme condominiale e/o videocamera e/o impianti di sicurezza/domotica", 1),
    ("Portiere", 1),
    ("Condizionamento aria su almeno il 50% dei vani", 1),
    ("Impianto TV autonomo o centralizzato", 1),
    ("Impianto antenna parabolica e/o collegamento in rete", 1),
    ("Dotazione di fonti energetiche rinnovabili", 2)
]
punti_c = 0
for label, punti in servizi:
    if st.checkbox(label):
        punti_c += punti

citofono = st.radio("Citofonia", ["Assente", "Impianto di citofono (+1)", "Impianto di video-citofono (+2)"])
if "(+1)" in citofono:
    punti_c += 1
elif "(+2)" in citofono:
    punti_c += 2

ape = st.radio("Classe energetica APE", ["A - B (+4)", "C - D - E (+2)", "F - G (+0)"])
if ape.startswith("A"):
    punti_c += 4
elif ape.startswith("C"):
    punti_c += 2


def fascia_pertinenze(p):
    if p <= 5:
        return "Inferiore"
    if p <= 10:
        return "Media"
    return "Superiore"


def fascia_conservazione(p):
    if p <= 5:
        return "Inferiore"
    if p <= 9:
        return "Media"
    return "Superiore"


def fascia_servizi(p):
    if p <= 7:
        return "Inferiore"
    if p <= 15:
        return "Media"
    return "Superiore"


fascia_a = fascia_pertinenze(punti_a)
fascia_b = fascia_conservazione(punti_b)
fascia_c = fascia_servizi(punti_c)

vmax_a = fasce_ancona[zona][fascia_a]
vmax_b = fasce_ancona[zona][fascia_b]
vmax_c = fasce_ancona[zona][fascia_c]

can_max = (2 * vmax_a + 1 * vmax_b + 2 * vmax_c) / 5
can_min = can_max * 0.60

st.success(f"Fasce individuate: pertinenze -> {fascia_a} ({punti_a} p.) | "
           f"conservazione -> {fascia_b} ({punti_b} p.) | servizi -> {fascia_c} ({punti_c} p.)")
st.info(f"Valore base attribuito: minimo {can_min:.2f} - massimo {can_max:.2f} euro/mq annuo")

st.subheader("Correttivi")
st.caption("Le percentuali di questo punto si sommano algebricamente tra loro e si applicano una sola volta "
           "ai valori minimo e massimo ricavati.")
correttivi = 0.0

if st.checkbox("Alloggio in immobile intensivo, oltre 8 alloggi nello stesso fabbricato (-10%)"):
    correttivi -= 10

st.markdown("**Spazi comuni:**")
spazi_comuni = [
    ("Cortili con eventuale piantumazione e/o parcheggio in uso comune (+1%)", 1),
    ("Aree verdi (giardino, orto) in uso comune (+2%)", 2),
    ("Stenditoi/lavatoi comuni (+1%)", 1),
    ("Lastrici solari agibili in uso comune (+1%)", 1),
    ("Aree condominiali comuni, androni o ripostigli (+1%)", 1),
    ("Abitazione AUTONOMA: alloggio singolo o con ingresso indipendente, anche a schiera (+5%)", 5)
]
for label, perc in spazi_comuni:
    if st.checkbox(label):
        correttivi += perc

categoria = st.radio("Categoria catastale", [
    "A/2 (+0%)",
    "A/7 villini, oppure A/1, A/8, A/9 di cui all'art. 1 c. 2 L. 431/98 (+10%)",
    "A/3 (-2%)",
    "A/4, A/5, A/6 (-4%)"
])
if "+10%" in categoria:
    correttivi += 10
elif "-2%" in categoria:
    correttivi -= 2
elif "-4%" in categoria:
    correttivi -= 4

vetusta = st.radio("Vetusta' (anno di costruzione o di restauro/completa ristrutturazione con adeguamento "
                   "antisismico, come da permesso di costruire)", [
    "Dal 2000 in poi (0%)",
    "Dal 1975 al 1999 (-4%)",
    "Dal 1955 al 1974 (-8%)",
    "Fino al 1955 (-10%)",
    "Prima del 1935 con stato di conservazione in condizioni di degrado (-20%)"
])
riduzioni_vetusta = {
    "Dal 2000 in poi (0%)": 0.0,
    "Dal 1975 al 1999 (-4%)": -4.0,
    "Dal 1955 al 1974 (-8%)": -8.0,
    "Fino al 1955 (-10%)": -10.0,
    "Prima del 1935 con stato di conservazione in condizioni di degrado (-20%)": -20.0
}
riduzione_vetusta = riduzioni_vetusta[vetusta]
if riduzione_vetusta < 0:
    if st.checkbox("Interventi di manutenzione straordinaria effettuati dopo il 2000 "
                   "(la riduzione per vetusta' si riduce del 50%)"):
        riduzione_vetusta = riduzione_vetusta / 2
correttivi += riduzione_vetusta

st.markdown("**Carenza di elementi essenziali:**")
if st.checkbox("Assenza di servizi igienici interni all'abitazione (-15%)"):
    correttivi -= 15
if st.checkbox("Assenza di impianto di riscaldamento esteso a tutti i vani (-12%)"):
    correttivi -= 12
if st.checkbox("Assenza di allacciamento alla rete fognaria (-4%)"):
    correttivi -= 4

piano = st.radio("Piano dell'appartamento", [
    "Piano terra, 1 o 2 piano senza ascensore (0%)",
    "Piano intermedio o ultimo con ascensore (+2%)",
    "Piano seminterrato (-4%)",
    "3 piano senza ascensore (-4%)",
    "Oltre il 3 piano senza ascensore (-6%)"
])
percentuali_piano = {
    "Piano terra, 1 o 2 piano senza ascensore (0%)": 0.0,
    "Piano intermedio o ultimo con ascensore (+2%)": 2.0,
    "Piano seminterrato (-4%)": -4.0,
    "3 piano senza ascensore (-4%)": -4.0,
    "Oltre il 3 piano senza ascensore (-6%)": -6.0
}
correttivi += percentuali_piano[piano]

st.info(f"Somma algebrica dei correttivi: {correttivi:+.1f}%")

# MOBILIO (punto B5)
st.subheader("Mobilio")
mobilio = st.radio("Arredamento", [
    "Non ammobiliato",
    "Parzialmente ammobiliato, es. solo cucina, bagno ed elettrodomestici essenziali (+10/20%)",
    "Ammobiliato (fino a +25%)"
])
perc_mobilio = 0.0
if mobilio.startswith("Parzialmente"):
    perc_mobilio = st.slider("Incremento proporzionato alla quota di mobilio presente (%)", 10, 20, 15)
elif mobilio.startswith("Ammobiliato"):
    perc_mobilio = st.slider("Incremento per alloggio ammobiliato (%)", 0, 25, 25)
if perc_mobilio > 0:
    if st.checkbox("Mobilio scadente (la percentuale viene ridotta del 20%)"):
        perc_mobilio = perc_mobilio * 0.80

st.subheader("Tipo e durata del contratto")
tipo_contratto = st.selectbox("Contratto", [
    "Abitativo 3 anni + 2",
    "Abitativo 4 anni + 2 (+3%)",
    "Abitativo 5 anni + 2 (+5%)",
    "Abitativo 6 anni + 2 (+7%)",
    "Transitorio (1-18 mesi)",
    "Studenti universitari fuori sede, fino a 9 mesi",
    "Studenti universitari fuori sede, da 10 a 12 mesi (+5%)",
    "Studenti universitari fuori sede, da 13 a 24 mesi (+8%)",
    "Studenti universitari fuori sede, da 25 a 36 mesi (+10%)"
])
percentuali_durata = {
    "Abitativo 3 anni + 2": 0.0,
    "Abitativo 4 anni + 2 (+3%)": 3.0,
    "Abitativo 5 anni + 2 (+5%)": 5.0,
    "Abitativo 6 anni + 2 (+7%)": 7.0,
    "Transitorio (1-18 mesi)": 0.0,
    "Studenti universitari fuori sede, fino a 9 mesi": 0.0,
    "Studenti universitari fuori sede, da 10 a 12 mesi (+5%)": 5.0,
    "Studenti universitari fuori sede, da 13 a 24 mesi (+8%)": 8.0,
    "Studenti universitari fuori sede, da 25 a 36 mesi (+10%)": 10.0
}
perc_durata = percentuali_durata[tipo_contratto]

perc_zona_univ = 0.0
if "Studenti" in tipo_contratto:
    if st.checkbox("Alloggio situato in zona universitaria o limitrofa alle sedi universitarie (+5%)"):
        perc_zona_univ = 5.0

stima = st.button("Stima canone")
if stima:
    mq_min = can_min * (1 + correttivi / 100)
    mq_max = can_max * (1 + correttivi / 100)

    mq_min *= (1 + perc_mobilio / 100)
    mq_max *= (1 + perc_mobilio / 100)
    mq_min *= (1 + (perc_durata + perc_zona_univ) / 100)
    mq_max *= (1 + (perc_durata + perc_zona_univ) / 100)

    can_annuo_min = round(mq_min * superficie_convenzionale, 2)
    can_annuo_max = round(mq_max * superficie_convenzionale, 2)
    can_mensile_min = round(can_annuo_min / 12, 2)
    can_mensile_max = round(can_annuo_max / 12, 2)

    st.success(f"Canone ANNUO stimato: minimo -> {can_annuo_min} euro , massimo -> {can_annuo_max} euro")
    st.success(f"Canone MENSILE stimato: minimo -> {can_mensile_min} euro , massimo -> {can_mensile_max} euro")
    st.caption("Il canone effettivo e' concordato tra le parti entro la forbice minimo-massimo.")
