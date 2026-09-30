import streamlit as st

stradario_lecce = {
    1: [
        "VIA DUCA DEGLI ABRUZZI", "VIA ACAJA", "CORTE CONTE ACCARDO", "PIAZZETTA GIULIO ANT. ACQUAVIVA",
        "PIAZZA SS. ADDOLARATA", "CORTE DEGLI ADORNI", "VIA IMPERATORE ADRIANO", "CORTE DEGLI AIELLI",
        "VIA DEGLI ALAMI", "VIA VITTORIO ALFIERI", "VIA DEGLI AMMIRATI", "CORTE DEGLI ANDRANO",
        "CORTE DEGLI ANNIBALDI", "VIA DEGLI ANTOGLIETTA", "ARCO DI PRATO", "ARCO DI TRIONFO",
        "VIA GIACOMO ARDITI", "VIA SAN FRANCESCO ASSISI", "VIA FILIPPO BACILE", "VICO LA BAGLIVA DIETRO",
        "PIAZZETTA GIORGIO BAGLIVI", "VIA QUINTO FABIO BALBO", "CORTE DEI BALDUINI", "VIA GIROLAMO BALDUINI",
        "VIA ABRAMO BALMES", "CORTE GIUSEPPE EUGENIO BALSAMO", "VIA VINCENZO BALSAMO", "CORTE CAPPELLA BARLIERA",
        "CORTE DEI BARONI", "VIA MARCO BASSEO", "VIA CESARE BATTISTI", "VIA PADOVANO BAX",
        "VIA BECCHERIE VECCHIE", "VIA PIETRO BELLI", "VIA FRANCESCO BERNARDINI", "VIA MARIO BERNARDINI",
        "VIA ROBERTO DI BICCARI", "CORTE SAN BLASIO", "VIA GIOVANNI BOCCACCIO", "VICO BOEMONDO",
        "VIA DELLE BOMBARDE", "PIAZZETTA BONIFACIO IX", "CORTE DEI BONSECOLO", "PIAZZA FILIPPO BOTTAZZI",
        "VIA ULDERIGO BOTTI", "VIA MARINO BRANCACCIO", "VIA GUALTIERO DI BRIENNE", "VIA GAETANO BRUNETTI",
        "CORTE GILBERTO BRUNSWICH", "CORTE DEI BUCCARELLI", "VIA ANT. COSTAN. CASETTI", "VIA FRANCESCO CASOTTI",
        "VIA ISABELLA CASTRIOTA", "VIA NICOLA CATALDI", "CORTE SAN CATALDO", "VICO DELLA CAVALLERIZZA",
        "PIAZZA D'ITALIA", "PIAZZA DUOMO", "VIA REGINA ELENA", "VIA SERAFINO ELMO", "VIA QUINTO ENNIO",
        "PIAZZETTA LUCIO EPULIONE", "CORTE DEI FALCONI", "VIA VITO FAZZI", "VICO DEI FEDELE",
        "VIA GIAC. ANT. FERRARI", "VICO DEI FIESCHI", "VIA FABIO FILZI", "PIAZZETTA GIOVANNI DEI FIORENTINI",
        "CORTE ANTONIO DELLA FLORA", "CORTE FLORIO", "VIA CASALE FORNELLO", "VIA ANTONIO GALATEO",
        "VIA MAGGIORE GALLIANO", "VIA GIUSEPPE GARIBALDI", "CORTE SAN PIETRO GARZYA", "VIA CONTE GAUFRIDO",
        "CORTE DEI GENOVESI", "VIA GIOVANNI GENTILE", "CORTE DEI GHOTI", "VIA SS. GIACOMO E FILIPPO",
        "VIA CORRADO GIAQUINTO", "CORTE DEI GIORGI", "VIA DELLE GIRAVOLTE", "CORTE DEI GIUDICI",
        "VICO SAN GIUSTO", "VIA GOBETTI", "VIA SALVATORE GRANDE", "VIA ASCANIO GRANDI", "VIA FRANCESCO GUARINI",
        "VICO DEI GUIDANI", "PIAZZETTA PAUL HARRYS", "VIA IDOMENEO", "PIAZZETTA INNOCENZO XII",
        "CORTE SANTA IRENE", "VIA REGINA ISABELLA", "VIALE JAPIGIA", "VIA ALFONSO LAMARMORA",
        "VIA ACHILLE LARDUCCI", "VIA LAZIO", "VIA S. LEONARDO CONSERVATORIO", "VIALE GIACOMO LEOPARDI",
        "VIALE LO RE FRANCESCO", "VIA FERRANTE LOFFREDA", "PIAZZETTA LONGOBARDI", "CORTE DEI LUBELLI",
        "VIA LUBELLO", "VIA CESARE AUGUSTO LUCREZIO", "VIA XXV LUGLIO", "VIA MALENNIO", "CORTE DEI MALEPIERI",
        "VIA GUGLIELMO IL MALO", "VIA ANDREA MANTEGNA", "VIA GIUSEPPE MANTOVANO", "VIA ALESSANDRO MANZONI",
        "VIA SINDACO MARANGIO", "VIALE MARCHE", "VIA GUGLIELMO MARCONI", "VIALE DEL MARE",
        "VIA LUDOVICO MAREMONTI", "CORTE DEI MARESGALLI", "PIAZZETTA REGINA MARIA", "VIA BRACCIO MARTELLO",
        "VIA MATTEO DA LECCE", "VIA GIACOMO MATTEOTTI", "VICO BONAVENTURA DEI MATTHEI", "PIAZZA GIUSEPPE MAZZINI",
        "CORTE DEI MEMOLI", "CORTE DEI MESAGNESI", "VIA SEPOLCRI MESSAPICI", "CORTE METTOLA", "CORTE MIALI",
        "VICO ARCO DEI MILANESI", "VICO MONDO NUOVO", "CORTE DEI MONTEFUSCOLI", "CORTE DEI MORICINO",
        "CORTE DEI MUSCO", "CORTE NHOI", "VIA QUATTRO NOVEMBRE", "VIA GUGLIELMO OBERDAN", "PIAZZA SANTO ORONZO",
        "PIAZZETTA GIOV. ANT. ORSINI DEL BALZO", "VIALE OTRANTO", "PIAZZETTA ANTONIO PANZERA",
        "VIA SANTA MARIA DEL PARADISO", "VIA DEL PARCO TORRE", "VIA GIUSEPPE PARINI", "CORTE ANGELO PATARNELLO",
        "VIA DEI PATITARI", "VICO DIETRO LO OSPEDALE DEI PELLEGRINI", "VIA FRATELLI PELUSO", "VICO DEI PENSINI",
        "VIA DEI PERRONI", "VIA ERMENEGILDO PERSONÈ", "PIAZZETTA DEI PERUZZI", "VIA FRANCESCO PETRARCA",
        "VICO SOTTARRANEI", "CORTE DEGLI SPINOLA", "VIA VITO MARIO STAMPACCHIA", "VIA MADONNA DEGLI STUDENTI",
        "VIA LUIGI STURZO", "VIA MATTEO TAFURO", "PIAZZA TANCREDI", "CORTE DEI TARALLI", "VIA TORQUATO TASSO",
        "VIA DEL TEATRO ROMANO", "CORTE DEL TELEGRAFO AD ASTA", "VIA TEMPLARI", "VIA DEL THEUTRA", "VIA ORONZO TISO",
        "CORTE DEI TOLOMEI", "VIALE DELLA UNIVERSITA'", "CORTE VENTURA", "PIAZZA VITTORIO EMANUELE II",
        "CORSO VITTORIO EMANUELE III", "CORTE ROBERTO VOLTURIO", "VIA GIUSEPPE ZANARDELLI", "CORTE DEI ZIANI",
        "VIA GIUS. MARIA ZUCCARO"
    ],
    2: [
        "VIA DELL'ABATE ANTONIO", "VIA CESARE ABBA", "VIA ABRUZZI", "VIA ADDA", "VIA ADIGE", "VIA ADRIATICA",
        "VIA ADUA", "VIA AMBA ALAGI", "VIA DOM. TOMMASO ALBANESE", "PIAZZA DANTE ALIGHERI", "VIA CORRADO ALVARO",
        "VIA VINCENZO AMPOLO", "VIA NICOLA ANDRIA", "VIA LIVIO ANDRONICO", "VIA DELLE ANIME", "VIA ARCHITA DA TARANTO",
        "VIA GAETANO ARGENTO", "VIA ARNO", "VIA ASTI", "VIA FRANCESCO ANTONIO ASTORE", "VIA RICCARDO BACCHELLI",
        "VIA CASALE BAGNARA", "VIA PIERO BARGELLINI", "VIA BASENTO", "VIA DEI BASILIANI", "VIA BASILICATA",
        "VIA BATTAGLINI", "PIAZZA SAN GIOVANNI BATTISTA", "VIA GIUSEPPE BATTISTA", "VIA BELLINZONA",
        "VIA VITO BERNARDINO", "VIA DALMAZIO BIRAGO", "VIA NINO BIXIO", "VIA VITTORIO BODINI",
        "VIA BONAVENTURA DA LAMA",
        "VIA BERNARDINO BONIFACIO", "VIA DON BOSCO", "VIA ENRICO BOZZI", "VIA BERNARDINO BRACCIO", "VIA BRADANO",
        "VIA GIORDANO BRUNO", "VIA EMAN. MARIA BUCCARELLI", "VIA MICHELANGELO BUONARROTI", "VIA MONTE SEI BUSI",
        "VIA LUIGI CADORNA", "VIA PASQUALE CAFARO", "VIA CALABRIA", "VIA FRANCESCO CALASSO", "VIA BRUNO CANTOBELLI",
        "VIA GIOVANDOME. CATALANO", "VIA VECCHIA CAVALLINO", "VIA CAVOUR", "VIA ANTONIO CECCHI", "VIA PASQUALE CECERE",
        "VIA CECINA", "VIA VINCENZO CEPOLLA", "VIA FORTUNATO CESARI", "VIA GIUSEPPE CHIRIATTI", "VIA ISIDORO CHIRULLI",
        "VIA IGNAZIO CIAIA", "VIA VINCENZO CIARDO", "VIA FRANCESCO CILEA", "VIA GIUSEPPE CINO", "VIA PAOLO COLACI",
        "VIA QUINTO MARIO CORRADO", "VIA CORSICA", "VIA CORVAGLIA", "VIA BENEDETTO CROCE", "VIA NICOLO' DA LEQUILE",
        "VIA CARLO DALLA CHIESA", "VIA DALMAZIA", "VIA ETTORE D'AMORE", "VIA DOMENICO DE ANGELIS",
        "VIA ORONZO DE DONNO",
        "VIA ALCIDE DE GASPERI", "VIA COSIMO DE GIORGI", "VIA GIUSTINO DE IACOBIS", "VIA FRANCESCO DE MURA",
        "VIA ENRICO DE NICOLA", "PIAZZETTA SAN VINCENZO DE' PAOLI", "VIA FRANCESCO D'ELIA", "VIA GIOVANNI DI CASTRI",
        "VIA MARIO DI LECCE", "VIA ARMANDO DIAZ", "VIA AURELIANO DIMITRI", "VIA COSTANTINO DIMITRI", "VIA DOGALI",
        "VIA GAETANO DONIZETTI", "VIA D'OTRANTO MARTIRI", "VIA DUCAS ORSINI", "VIA LUIGI EINAUDI", "VIA EMILIA",
        "VIA DEI FERRARI", "VIA DEI FIORI", "VIA FIUME", "VIA VITO FORNARI", "VIA AMILCARE FOSCARINI",
        "VIA GALILEO GALILEI", "VIA ORONZO GARGIULO", "VIA GARIGLIANO", "VIA VESPASIANO GENUINO", "VIA GIUSEPPE GHEZZI",
        "VIA GORIZIA", "VIA ANTONIO GRAMSCI", "VIA MONTE GRAPPA", "VIA GIUSEPPE GRASSI", "VIA LUIGI GUACCI",
        "VIA GIOVANNI GUERRIERI", "VIA SANTA MARIA DELL' IDRIA", "VIA INDIPENDENZA", "VIA ISONZO",
        "VIA GIANCARLO LAZARI", "VIA LIRI", "VIALE DELLA LIBERTA'", "VIA LOMBARDIA", "VIA GIUSEPPE MAGGIO",
        "VIA MAURO MANIERI", "VIA ANTONIO MANNARINO", "VIA GIROLAMO MARCIANO'", "VIA PIETRO MARTI",
        "VIA SALVATORE MARTINI", "VIA MARTINO MARINOSCI", "VIA E.A. MARIO", "VIA GIOV. LEON. MARUGI", "VIA CARLO MASSA",
        "VIA MASSAGLIA", "VIA ORONZO MASSARI", "VIA SAVERIO MERCADANTE", "VIA PIETRO MIGALI", "VIA MINCIO",
        "VIA EUGENIO MONTALE", "VIA MONTELLO", "VIA ALDO MORO", "VIA MARIO NACCI", "VIA NIZZA", "VIA GIOVANNI NOCCO",
        "VIA GAETANO DELLA NOCE", "VIA OFANTO", "VIA ORTIGARA", "VIA OSLAVIA", "VIA GIUSEPPE PALAMA",
        "VIA BALDASSARRE PAPADIA", "VIA GASPARE PAPATODERO", "VIA LUIGI PAPPACODA", "PIAZZA DEI PARTIGIANI",
        "VIA ANDREA PENNETTERA", "VIA LUDOVICO PEPE", "VIA ARMANDO PEROTTI", "VIA VINCENZO PERSANO",
        "VIA DIEGO PERSONE'",
        "VIA MASSENZIO PICCINNI", "VIA PIEMONTE", "VIA PITAGORA", "VIA PO", "VIA FRANCESCO POLI", "VIA PORDENONE",
        "VIA POZZUOLO", "VIA GIOVANNI PRESTA", "VIA ANTONIO PROFILO", "VIA ORONZO QUARTA", "VIA CESARE RAHO",
        "VIA BARTOLOMEO RAVENNA", "VIA EGIDIO REALE", "VIA BERNARDINO PADRE REALINO", "VIA REDIPUGLIA",
        "VIA FRANCESCO RIGLIACO", "VIA CAP. RITUCCI", "VIA SALVATOR ROSA", "VIA ANTONIO ROSMINI",
        "VIA GIOACCHINO ROSSINI", "VIA RAFFAELE RUBINI", "PIAZZALE RUDIAE", "VIA RUDIAE", "VIA VINCENZO SABATO",
        "VIA MONTE SABOTINO", "VIA SAGRADO", "VIA CARLO SALERNI", "VIA DEI SALESIANI", "VIA GAETANO SALVEMINI",
        "VIA VECCHIA SAN CESARIO", "VIA SAN CESARIO", "VIALE SAN NICOLA", "VIA SAN PIETRO IN LAMA", "VIA SANT'ELIA",
        "VIA RAFFAELLO SANZIO", "VIA MICHELE SAPONARO", "VIA GIUSEPPE SARAGAT", "VIA GIUSEPPE SARNO",
        "VIA SAN DOMENICO SAVIO", "VIA OTTAVIO SCALFO", "VIA FRANCESCO SCARPA", "VIA DEGLI SCARPARI",
        "VIA GIAN MARIA SCUPOLA", "VIA SELE", "VIA SETTELACQUARE", "VIA ANDREA SOZZO", "VIA SPALATO",
        "VIA SILVIO SPAVENTA", "VIALE DELLO STADIO", "VIA GIOVANNI STANO", "VIA PAOLO STOMEO", "VIA FRANCESCO STORELLA",
        "VIA SUPERSTRADA", "VIA VOLTURNO", "VIA ANTONIO ZIMBALO", "VIA GIUSEPPE ZIMBALO", "VIA TOMMASO TRAETTA",
        "VIA TRENTO", "VIA TRIESTE", "VIA FRANCESCO TRINCHERA", "VIA SALVATORE TRINCHESE", "VIA GIAMBATTISTA DEL TUFO",
        "VIA FILIPPO TURATI", "VIA UDINE", "VIA UMBRIA", "VIA DI USSANO", "VIA DI VALESIO", "VIA GIULIO CESARE VANINI",
        "VIA TIZIANO VECELLIO", "VIA VITTORIO VENETO", "VIA PIETRO VINCENTI", "VIA ORDINE DI VITTORIO VENETO",
        "VIA SAN GIOV. MARIA VIANNEY", "VIA S. LIGUORI DELLE VITE"
    ],
    3: [
        "VIA BELISARIO ACQUAVIVA", "PIAZZALE ATTILIO ADAMO", "PIAZZALE ADRIANO", "STRADA ADRIATICA SOLICARA",
        "VIA AGRI",
        "VIA DELL'AGRICOLTURA", "VIA AGRIGENTO", "VIA FEDELE ALBANESE", "VICO LEANDRO DEGLI ALBANESI",
        "VIA DEGLI ALBERICI", "PIAZZETTA ALBERTI", "VIA ALESSANDRIA", "VIA ROBERTO ALMAGIA'", "VIA ANCONA",
        "VIA II TRAVERSA ANDRIANI", "VIA VINCENZO ANDRIANI", "VIA ANIENE", "VIA PRAZIO ANTINORI",
        "VIA CLEMENTE ANTONACI",
        "VIA GIUSEPPE APRILE", "VIA LUCIO APULEIO", "VIA ARCHIMEDE", "VIA AREZZO", "VIA NICOLA ARGENTIERI",
        "VIA ARGENTINA", "PIAZZA NICODEMO ARGENTO", "VIA LUDOVICO ARIOSTO", "CORTE DELLE ARMELLINE",
        "VIA ARNESANO 1 TRAV SX", "STRADA ESTERNA ARNESANO", "VIA ARNESANO TRAV IPPODROMO", "VIA ARNESANO",
        "VIA ARNESANO COOPERATIVA VIVALDI", "VIA DELL'ARTIGIANATO", "VIA ASCOLI PICENO", "PIAZZETTA DUCA DI ATENE",
        "VIA MARCO AURELIO", "VIA AUSONIO", "VIA AVELLINO", "VIA GUGLIELMO BAFFIN", "VIA ADRIANO BALBI",
        "VIA NUZZO BARBA",
        "VIA CARLO BARBIERI", "VIA BARI", "VIA AGNESE BATTISTA", "VIA BELICE", "VIA VINCENZO BELLINI",
        "VIA VITTORE BELLIO",
        "VIA BELLUNO", "ZONA BELSITO", "VIA COSTANTINO BELTRAMI", "VIA DELLE BENEDETTINE", "VIA BENEVENTO",
        "VIA BERGAMO",
        "VIA BERING", "VIA BERNARDINI", "VIA COSIMO BERTACCHI", "VIA DEI PITTORI BIANCHI", "VIA ATTILIO BIASCO",
        "VIA BIFERNO", "VIA BIZAMANO", "VIA ARRIGO BOITO", "PIAZZALE BOLOGNA", "VIA BOLZANO", "VIA BORMIDA",
        "VIA ANTONIO BORTONE", "VIA VITTORIO BOTTEGO", "VIA SANDRO BOTTICELLI", "VIA GIACOMO BOVE", "VIA LIBERO BOVIO",
        "VIA BENEDETTO BRIN", "VIA MARGARITO DA BRINDISI", "VIA GIACOMO BRUCE", "VIA ANTONIO BRUNI",
        "VIA PLACIDO BUFFELLI",
        "VIA DINO BUZZATI", "VIA DA CA' MOSTO", "VIA SEBASTIANO CABOTO", "VIA CAGLIARI", "VIA CAIROLI",
        "VIA POMPONIO CALIO'", "VIA ESTERNA CALIO'", "VIA CALORE", "VIA CALTANISETTA", "VIA CALVANI",
        "VIA FRANCESCO CAMASSA", "VIA CAMPANIA", "VIA MANFREDO CAMPERIO", "VIA CAMPI", "VIA CAMPOBASSO",
        "VIA GIUSEPPE CANDIDO", "VIA FRANC. SAVERIO CANDIDO", "VIA AMBROGIO CANTARINI", "VIA RICCIOTTO CANUDO",
        "VIA CORRADO CAPECE", "VIA LUIGI CAPUANA", "VIA NICOLA CAPUTI", "VIA ANTONIO CARACCIO",
        "VIA FERRANTE CARACCIOLO",
        "VIA ALFONSO SOZY CARAFA", "PIAZZA VINCENZO CARDARELLI", "VIA ENNIO CARLINO", "VIA LUIGI CARLUCCIO",
        "VIA VITO CARLUCCIO", "VIA VECCHIA CARMIANO", "VIA CARSO", "VIA GIACOMO CARTIER", "LOCALITA' CASA SIMINI",
        "LOCALITA' CASALABATE", "VIA GAETANO CASATI", "VIA FRANCESCO SAVERIO CASAVOLA", "VIA FRANCO CASAVOLA",
        "VIA GIUSEPPE CASCIARO", "VIA CASERTA", "VIA GIUSEPPE CASTIGLIONE", "VIA ALFREDO CATALANI", "VIA CATANIA",
        "VIA CATANZARO 1 TRAVERSA", "VIA CATANZARO", "VIA VALERIO CATULLO", "VIA GUIDO CAVALCANTI",
        "VIA PIETRO CAVALLO",
        "VIA FELICE CAVALLOTTI", "VIA PIETRO CAVOTI", "VIA CEFALONIA", "VIA CERRATE", "VIA CHIETI", "VIA CIMAROSA",
        "VIA COSENZA", "VIA CREMONA", "VIA CUNEO", "VIA CUOCO", "VIA D'ACQUISTO", "VIA DAL POZZO TOSCANELLI",
        "VIA D'ANDREA",
        "VIA DANIELE", "VIA D'ARAGONA", "VIA D'ARPE", "VIA D'ASTORE", "VIA DE AGOSTINI", "VIA DE BLASI",
        "VIA DE PASCALIS",
        "VIA DE RINALDIS", "VIA DE ROMA", "VIA DE ROSIS", "VIA DE SIMONE", "VIA DELEDDA", "VIA DELLA VEDOVA",
        "VIA DI GIACOMO", "VIA DI PALMA", "VIA DONNO", "VIA DORIA", "VIA DORSO", "VIA DUBROVINIK", "VIA EBOLI",
        "VIA ELIA", "VIA EREDIA", "VIA ERRIQUEZ", "VIA ESTRAFALLACES", "VIA EUIPPA", "VIA FALCO", "VIA FANULI",
        "VIA FERMI", "VIA FERRANDI", "VIA FERRANDO", "VIA FERRARA", "VIA FIORE", "VIA FIORINI", "VIA FIRENZE",
        "VIA FLACCO", "VIA FLASCASSOVITTI", "VIA FLEMING", "VIA FLUMENDOSA", "VIA FOGAZZARO", "VIA FOGGIA",
        "VIA FONDONE",
        "VIA FONTANA", "VIA FORLANINI", "VIA FORLI'", "VIA FORTORE", "VIA FOSCOLO", "VIA FREUD", "VIA FRIGOLE",
        "VIA FRIULI", "VIA FULCIGNANO", "VIA GABRIELI", "VIA GAGLIARDO", "VIA GALATINO", "VIA GALLO", "VIA GASTALDI",
        "VIA GEMITO", "VIA GENOVA", "VIA GENTILE", "VIA GESSI", "VIA GIAMMATTEO", "VIA GIANCANE", "VIA GIDIULI",
        "VIA GIGLI", "VIA GIGLIOLI", "VIA DELLE GINESTRE", "VIA GIOIA", "VIA GIORDANO", "VIA GIOTTO", "VIA GIOVENALE",
        "VIA GIURGOLA", "VIA GIUSTI", "VIA GOLDONI", "VIA GOZZANO", "VIA GRIMALDI", "VIA GROSSETO", "VIA GUARIGLIA",
        "VIA GUERRAZZI", "VIA IMPERIA", "VIA INDONATORI", "VIA INDRACCOLO", "VIA INDUSTRIA", "ZONA INDUSTRIALE",
        "VIA INFANTINO", "VIA ISARCO", "VIA ITACA", "LUNGOMARE MARINAI D'ITALIA", "VIA KEPLERO", "VIA LA LIZZA",
        "VIA LA SPEZIA", "CONTRADA LAMA", "VIA LATINA", "VIA MAESTRI DEL LAVORO", "VIA LENIO", "VIA LEONCAVALLO",
        "VIA LEONE", "VIA LEPANTO", "STRADA ESTERNA LEQUILE", "VIA LEQUILE", "STRADA ESTERNA LEUCA", "VIA LEUCA",
        "CORTE SAN LEUCIO", "CORTE DEI LEVANTO", "VIALE DELLA LIBERTA'", "VIA LIBERTINI", "PIAZZA LIBERTINI",
        "CORTE VINCENZO LICCI", "VIA SAN LIGORIO", "VIA LIGURIA", "PIAZZETTA GIUSEPPE LILLO", "VIA FILIPPO LIPPI",
        "VIA LIVENZA", "VIA LIVORNO", "VIA VECCHIA LIZZANELLO", "VIA ESTERNA LO PAPA", "VIA ALBERICO LONGO",
        "VIA BARTOLO LONGO", "VIA LUCCA", "PIAZZETTA FORMOSO LUCE", "VIA BRUNO LUCREZI", "VIA LUPIAE",
        "VIA SINDACO LUPINACCI", "VIA ENRICO LUPINACCI", "VIA EUGENIO MACCAGNANI", "ZONA MACCHITELLI",
        "VIA NICCOLO' MACHIAVELLI", "VIA FERDINANDO MAGELLANO", "VIA XXIV MAGGIO", "VIA LUIGI MAGGIULLI",
        "VIA GIOVANNI MAGINI", "VIA ALBERTO MAGNAGHI", "VIA ALESSANDRO MALASPINA", "VIA ANTONIO MALASPINA",
        "VIA STRADA ESTERNA MALECARNE", "VIA GIUSEPPE MALECORE", "VIA LANCILLOTTO MALOCELLO", "VIA MALTA",
        "VIA GIUSEPPE MANFREDI", "VIA MANGIONELLO", "VIA FERNANDO MANNO", "VIA MANTOVA", "VIA GIUSEPPE MANZO",
        "VIA GIACOMO MARALDI", "VIA LUIGI MARIANO", "VIA GIOVANNI MARINELLI", "VIA FRANCESCO MARMOCCHI",
        "VIA GAETANO MARTINEZ", "VIA LUIGI MARTUCCI", "VIA MASACCIO", "VIA ALDO MASCIULLO", "VIA MICHELE MASSARI",
        "VIA MATERA", "VIA PELLEGRINO MATTEUCCI", "VIA MEDAGLIE D'ORO", "VIA EVANGELISTA MENGA", "VIA MERCATORE",
        "VIA MERINE", "VIA GREGORIO MESSERE", "VIA MESSINA", "VIA METAURO", "VIA ANTONIO MEUCCI", "VIA GIOVANNI MIANI",
        "VIA MICELLI", "VIA SAN MICHELE MONTE", "VIA PIETRO MICHELI", "VIA ANTONIO MIGLIETTA", "PIAZZALE MILANO",
        "VIA TITO MINNITI", "VIALE DON MINZONI", "VIA DEI MOCENIGO", "VIA MOLISE", "VIA BIVIO MONTERONI",
        "VIA ESTERNA MONTERONI", "VIA MONTERONI", "VIA MONTONE", "VIA MORELLI", "VIA MORI", "VIA BONAVENTURA MOROSINI",
        "VIA MARIO MOSCARDINO", "VIA GIUSEPPE MOSCATI", "VIA GIUSEPPE MOSCHETTINI", "VIA WOLFANG MOZART",
        "VIA FILIPPO MURATORE", "VIA NICOLA NACUCCHI", "PIAZZA NAPOLI", "VIA CRISTOFORO NEGRI", "CORTE PIER DI NEGRO",
        "VIA SAN NICOLA", "VIA UMBERTO NOBILE", "VIA NOVARA", "VIA ESTERNA NOVOLI", "VIA NUORO",
        "VIA TRIFONE NUTRICATI",
        "VIA DELL'OCCHIATA", "VIA OGLIO", "VIA DEGLI OLITA", "VIA OMBRONE", "VIA DEGLI OREFICI", "VIA EMANUELE ORFANO",
        "VIA FUORI LE MURA SANTO ORONZO", "VIA DEGLI OROPELLAI", "VIA RAMONDELLO ORSINI", "VIA GUGLIELMOTTO D'OTRANTO",
        "VIA PUBLIO OVIDIO NASONE", "VIA PACELLI", "VIA MARCO PACUVIO", "LOCALITA' MEZZAGRANDE PADOVA",
        "VIA NICOLO' PAGANINI",
        "VIA VITTORIO PAGANO", "ZONA PAGLIARONE", "VIA GUGLIELMO PAISIELLO", "VIA PALADINI",
        "VIA LUISA AMALIA PALADINI",
        "VIA ALDO PALAZZESCHI", "VICO DEI PALEOLI", "VIA PALERMO", "PIAZZA DEL PALIO", "CORTE DEI PALMA",
        "VIA CAMILLO GIOVANNI PALMA", "VIA GIUSEPPE PALMIERI", "VIA DEI PALUMBO", "VIA MICHELE PALUMBO",
        "VIA PIETRO PALUMBO",
        "ZONA PAMPOLI", "VIA SALVATORE PANAREO", "VIA PANARO", "VIA LEONE PANCALDO", "CORTE DEI PANDOLFI",
        "VICO PANEVINO",
        "VIA PANTALEONE", "VIA PANTELLERIA", "VIA PAPINI", "VIA ORONZO PARLANGELI", "VIA PARMA",
        "VIA FRANCESCO PASANISI",
        "VIA GIOVANNI PASCOLI", "VIA EMANUELE PASSABY", "VIA LUIGI PASTEUR", "VIA PATRASSO", "VIA PAVIA",
        "PIAZZETTA GIUSEPPE PELLEGRINO", "VIA SILVIO PELLICO", "VIA LORENZO PEROSI", "LOCALITA' MEZZAGRANDE PERUGIA",
        "VIA PESARO", "VIA PESCARA", "VIA GIUSEPPE PETRAGLIONE", "CORTE DEI PETRAROLI", "VIA FRANCESCO PETRELLI",
        "VIA ARCIVES. PETRONELLI", "CORTE PETTI", "VIA DI PETTORANO", "VIA PIACENZA", "VIA CARLO PIAGGIA", "VIA PIAVE",
        "VIA MARIA FRANCESCO PIAVE", "VIA FRANCESCO ANTONIO PICCINNI", "VIA ALDO PICCINNO", "VIA ANTONIO PIGAFETTA",
        "VIA PINTO", "LARGO SAN PIO X", "VIA GUIDO PIOVENE", "VIA LUIGI PIRANDELLO", "PIAZZALE PISA",
        "VIA CARLO PISACANE",
        "VIA GIUSEPPE PISANELLI", "STRADA ESTERNA PISELLO", "VIA PISTOIA", "VIA DEL PITTACCIO", "VIA FRANCESCO PIZARRO",
        "VIA IDELBRANDO PIZZETTI", "VIA MARCO POLO", "VIA AMILCARE PONCHELLI", "VIA PORCIGLIANO",
        "VIA ODORICO DA PORDENONE",
        "VIA FILIPPO PORENA", "VIA CARLO PORTA", "VIA AMLETO POSO", "VIA POTENZA", "VIA LEONARDO PRATO", "VIA PREMUDA",
        "VIA VITTORIO PRIOLO", "VIA PROPERZIO", "VICO NOBILISSIMI DEI PROTO", "VIA GIACOMO PUCCINI", "VIA PUGLIA",
        "VIA SAN CESARIO QUASIMODO", "PIAZZA QUASIMODO", "VIA SALVATORE RAELI", "VIA VITO RAGUSA", "VICINALE RAMANNO",
        "VIA RAPOLLA", "CORTE GUIDONE DA RAVENNA", "VICO DEI RAYNO'", "VIA GEREMIA RE", "VIA CLEMENTE REBORA",
        "VIA NICOLOSO DA RECCO", "VIA RENO", "VIA ANTONIO RENZO", "VIA DELLA REPUBBLICA", "VIA OTTORINO RESPIGHI",
        "VIA PAOLO REVELLI", "VIA FRANCESCO RIBEZZO", "PIAZZETTA GABRIELE RICCARDI", "VIA GIUSEPPE RICCHIERI",
        "VIA MATTEO RICCI", "VIA RIETI", "VIA DEL RISORGIMENTO", "VIA CAPITANO RIVABELLA", "CORTE DEI RIVOLA",
        "VIA CONTE ROBERTO", "CORTE RODI", "VIA ROMA", "VIA LIBORIO ROMANO", "CORTE DEI ROMITI", "VIA ROSSI",
        "VIA BENIAMINO ROSSI", "VIA ROVIGO", "VIA FRANCESCO RUBICHI", "VIA RICHEL RUBICHI", "VIA RUBICONE",
        "VIA GAETANO RUCCO", "VIA CARLO RUSSI", "VIA UMBERTO SABA", "VIA SAN SABINO", "VIA SACCO", "CORTE DEI SAETTA",
        "VIA ANTONIO SALANDRA", "PIAZZA SALERNO", "VIA SALICE", "CORTE DEI SALOMI", "VIA SALSO",
        "STRADA ESTERNA SAN CATALDO",
        "VIA SANDALO", "VIA SANGRO", "VIA GIUSEPPE SAPETO", "VICO DELLA SAPONEA", "CORTE DEI SARACENI", "VIA SARDEGNA",
        "VIA SASSARI", "VIA NAZARIO SAURO", "VIA PRINCIPI DI SAVOIA", "VIA LUIGI SCARAMBONE", "VIA GIUSEPPE SCARDIA",
        "VIA PEREGRINO SCARDINO", "VIA NICOLA SCHIAVONI", "P.ZZA TITO SCHIPA", "VIA MICHELANGELO SCHIPA",
        "VIA DELLE SCIENZE",
        "VIA SCIPIONE AMMIRATO", "VIA LUIGI SCORRANO", "VIA ROCCO SCOTELLARO", "VIA SCRIVIA", "VIA SCUOLA ELEMENTARE",
        "VIA SECCHIA", "VIA QUINTINO SELLA", "VIA TRAVERSA SERRA BIANCA", "VIA SESIA", "VIA XX SETTEMBRE",
        "VIA LUIGI SETTEMBRINI", "VICO SFERRACAVALLI", "VIA CONTESSA SIBILLA", "VIA SICILIA", "VIA STANISLAO SIDOTI",
        "PIAZZALE SIENA", "VIA ERNESTO SIMINI", "VIA DELLA SINAGOGA", "VIA SINNI", "VIA SIRACUSA", "VIA FERECIDE SIRO",
        "VIA FILIPPO SMALDONE", "VIA SONDRIO", "VIA GAETANO STABILI", "PIAZZETTA DELLA STAMPA", "VIA DEGLI STAMPACCHIA",
        "VIA ERCOLE STASI", "VIA EMILIO STASI PAOLO", "CORTE GAETANO STELLA", "VICO DEGLI STORELLA",
        "VICO STORTO VECCHIA CARITA'", "VIA GIANSERIO STRAFELLA", "VIA GUSTAVO STRAFFORELLO", "VIA STURA",
        "VIA ESTERNA SURBO", "VIA VECCHIA SURBO", "CORTE DEI SYBARIS", "VIA MANIFATTURA TABACCHI", "VIA DI TAFAGNANO",
        "VIA TAGLIAMENTO", "VIA TANAGRO", "VIA TANARO", "VIA GIANMARIA TARANTINO", "VIA TARANTO", "VIA TARO",
        "VIA GIUSEPPE TARTINI", "LARGO LUIGI TASSELLI", "VIA TECNICA", "VIA LIVIO TEMPESTA", "VIA TEOCRITO",
        "VIA TERAMO", "VIA TERNI", "VIA TEVERE", "VIA TICINO", "VIA LUIGI TINELLI", "VIA TIRSO", "VIA CLAUDIO TOLOMEO",
        "VIA GIOACCHINO TOMA", "VIA NICCOLO' TOMMASEO", "VIA TORINO", "VIA TORRE MOZZA", "VIA COOPERATIVA TORRICELLI",
        "VIA BENEDETTO TORSELLO", "VIA TOSCANA", "PIAZZALE ARTURO TOSCANINI", "VIA MAGGIORE TOSELLI", "VIA ENRICO TOTI",
        "VIA TREBBIA", "VIA GIUSEPPE TRICARICO", "VIA DELLA TRIGLIA", "VIA TRILUSSA", "VIA TURATI",
        "VIA DELL' ULIVO SAN LIGORIO", "VIA PRIMO UMBERTO", "VIA GIUSEPPE UNGARETTI", "VIA GIOACCHINO UNGARO",
        "VIA URBINO", "VIA ANTONIOTTO USODIMARE", "VIA NICOLA VACCA", "VIA EPANIMONDA VALENTINI", "VIA DIEGO VALERI",
        "VIA NICOLA VALLETTA", "VIA VALONA", "VIA PIETRO VALZANI", "VIA LUIGI VANVITELLI", "VIA BERNARDO VARENIO",
        "VIA VARESE", "VIA GIORGIO VASARI", "VIA DI VASTE", "VIA VELINO", "VIA SANTA VENERA", "VIA VITTORIO VENETO",
        "VIA VENEZIA", "VIA SEBASTIANO VENIERO", "VIA VENOSA", "VIA DEI VERARDI", "VIA VERCELLI", "VIA GIUSEPPE VERDI",
        "PIAZZA GIUSEPPE VERDI", "VIA DI VERETO", "VIA GIOVANNI VERGA", "VICO VERNAZZA", "VIA VERNOLE", "VIA VERONA",
        "VIA PAOLO VERONESE", "VIA GIOVANNI DA VERRAZZANO", "CORTE DEL VERRIO", "VIA AMERIGO VESPUCCI",
        "VIA SANTA MARIA VETERANI", "VIA VICENZA", "VIA ANDREA VIGNES", "VIA PIPPO VIGONI", "VIA VIRGILIO",
        "VIA MICHELE VITERBO", "VIA ANTONIO VIVALDI", "VIA UGOLINO VIVALDI", "VIA ALESSANDRO VOLTA", "VIA ZANTE"
    ]
}

sub_pregio_lecce = {
    1: [
        "VIA IMPERATORE AUGUSTO", "VIA FILIPPO BACILE", "VIA ROBERTO DI BICCARI",
        "PIAZZETTA SIGISMONDO CASTROMEDIANO", "VIA FELICE CAVALLOTTI", "VIA REGIO SACRO CONSIGLIO",
        "VIA ACHILLE COSTA", "PIAZZETTA COLONNELLO DE CRISTOFORIS", "PIAZZETTA NICOLA DE PACE",
        "PIAZZETTA BRIZIO DE SANTIS", "VIA 140 REGGIMENTO FANTERIA", "VIA 47 REGGIMENTO FANTERIA",
        "VIA 95 REGGIMENTO FANTERIA", "VIA VITO FAZZI", "VICO DEI FEDELE", "VIA FABIO FILZI",
        "VIA GIUSEPPE GARIBALDI", "VIA ALFONSO LAMARMORA", "PIAZZA LIBERTINI", "VIA XXV LUGLIO",
        "VIA GUGLIELMO MARCONI", "VIALE DEL MARE", "VIA LUDOVICO MAREMONTI", "VIA BRACCIO MARTELLO",
        "VIA MATTEO DA LECCE", "VIA GIACOMO MATTEOTTI", "PIAZZA GIUSEPPE MAZZINI",
        "VIA SAN MICHELE MONTE", "VICO ARCO DEI MILANESI", "VIA DEI MOCENIGO", "VIA GUGLIELMO OBERDAN",
        "PIAZZA SANTO ORONZO", "PIAZZETTA GABRIELE RICCARDI", "VIA LIBORIO ROMANO",
        "VIA FRANCESCO RUBICHI", "VIA RICHEL RUBICHI", "VICO DELLA SAPONEA", "VIA FRANCESCO STORELLA",
        "VIA TEMPLARI", "VIA SALVATORE TRINCHESE", "VIA PRIMO UMBERTO", "VIA GIUSEPPE VERDI",
        "PIAZZA VITTORIO EMANUELE II", "VIA GIUSEPPE ZANARDELLI"
    ],
    2: [
        "VIA CESARE ABBA", "VIA DOM. TOMMASO ALBANESE", "VIA LIVIO ANDRONICO", "VIA ASTI",
        "VIA FRANCESCO ANTONIO ASTORE", "VIA VITTORIO BODINI", "VIA BONAVENTURA DA LAMA",
        "VIA BENEDETTO CROCE", "VIA ORONZO DE DONNO", "VIA ALCIDE DE GASPERI", "VIA COSIMO DE GIORGI",
        "VIA FRANCESCO DE MURA", "VIA FRANCESCO D'ELIA", "VIA ALBERICO LONGO", "VIA BARTOLO LONGO",
        "VIA LUPIAE", "VIA ANTONIO MANNARINO", "VIA FRANCESCO MARANGI", "VIA MARTINO MARINOSCI",
        "VIA PIETRO MARTI", "VIA GIOV. LEON. MARUGI", "VIA CARLO MASSA", "VIA MERINE",
        "VIA MARCO PACUVIO", "VIA BALDASSARRE PAPADIA", "VIA GASPARE PAPATODERO",
        "PIAZZA DEI PARTIGIANI", "VIA LUDOVICO PEPE", "VIA PITAGORA", "VIA FRANCESCO POLI",
        "VIA ANTONIO PROFILO", "PIAZZA QUASIMODO", "VIA BARTOLOMEO RAVENNA", "VIA VINCENZO SABATO",
        "VIA DEI SALESIANI", "VIA MICHELE SAPONARO", "VIA SAN DOMENICO SAVIO", "VIA FRANCESCO SCARPA",
        "VIA SETTELACQUARE", "VIA GIOVANNI STANO", "LARGO LUIGI TASSELLI", "VIA NICCOLO' TOMMASEO",
        "VIA SAN GIOV. MARIA VIANNEY", "VIA PIETRO VINCENTI"
    ]
}

sub_pregio_tratto = {
    1: ["VIA NAZARIO SAURO"],
    2: ["VIALE DELLA LIBERTA'", "VIALE DELLO STADIO", "VIA VECCHIA FRIGOLE"]
}

st.subheader("Generalità")
via = st.text_input("Inserisci la via senza numero civico, nome completo").upper()
mq_tot = st.number_input("Inserire i mq (superficie calpestabile al netto delle pareti)")

for k in stradario_lecce.keys():
    stradario_lecce[k] = [i.strip().replace(" ", "") for i in stradario_lecce[k]]

for k in sub_pregio_lecce.keys():
    sub_pregio_lecce[k] = [i.strip().replace(" ", "") for i in sub_pregio_lecce[k]]

for k in sub_pregio_tratto.keys():
    sub_pregio_tratto[k] = [i.strip().replace(" ", "") for i in sub_pregio_tratto[k]]

pulizia = lambda x: x.replace(" ", "").strip().upper()

can_min = 0.0
can_max = 0.0

if via and via.strip() != "":
    if all(pulizia(via) not in stradario_lecce[k] for k in stradario_lecce.keys()):
        st.warning("La via non è stata trovata")

    fascia = ""
    fasce_zona = {}
    elementi_pregio_zona = []
    chiedi_cond_sat = False
    nota_posto_auto = False


    if pulizia(via) in stradario_lecce[1]:

        fasce_zona = {"A": (4.70, 5.40), "B": (3.60, 4.60), "C": (1.80, 3.50)}

        car1 = st.checkbox("Appartamenti dal 1° piano fuori terra")
        car2 = st.checkbox("Allacciamento gas metano")
        car3 = st.checkbox("Ascensore a partire dal 2° piano")
        car4 = st.checkbox("Autoclave")
        car5 = st.checkbox("Impianto elettrico interno adeguato alla legge n.37/08")
        car6 = st.checkbox("Riscaldamento autonomo o centralizzato")
        car7 = st.checkbox("Infissi interni ed esterni in buono stato")
        servizi_interni = st.checkbox(
            "Servizi igienici (tazza, lavabo, doccia ovvero vasca da bagno) posti all'interno dell'alloggio",
            help="I servizi igienici posti all'esterno dell'alloggio determinano l'inserimento automatico del canone nella terza sub-fascia.")
        car8 = False
        if servizi_interni == True:
            car8 = st.checkbox(
                "I servizi igienici interni sono completi, dotati anche di bidet (requisito per la sub-fascia A)")
        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8]
        counter = sum(con for con in condizioni if con == True)

        st.markdown("**Condizioni Speciali**")


        zona_pregio = False
        if pulizia(via) in sub_pregio_tratto[1]:
            zona_pregio = st.checkbox(
                "La via è in sub-zona di pregio solo per un tratto: il civico ricade nel tratto di pregio?",
                help="Tratto di pregio per Via Nazario Sauro: da via Battisti a via 95° Rgt Fanteria."
                     "e le altre vie? ")
        elif pulizia(via) in sub_pregio_lecce[1]:
            zona_pregio = True
            st.info("Via classificata in sub-zona di pregio (P) dall'allegato 1: concorre all'accesso diretto alla sub-fascia A")
        buone_condizioni = st.checkbox(
            "Stabile e appartamento in buone condizioni",
            help="Condizione essenziale per la collocazione nella sub-fascia A (allegato 3: portone e citofono funzionanti, pavimentazioni e rivestimenti senza distacchi, infissi con chiusure e oscuramenti funzionanti, impianto di adduzione e scarico acqua funzionanti, ecc.).")

        if servizi_interni == False:
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C (servizi igienici esterni all'alloggio)")
        elif (counter >= 6 or zona_pregio == True) and car8 == True and buone_condizioni == True:
            fascia = "A"
            st.success(f"Assegnata: SUB-FASCIA A")
        elif counter >= 4:
            fascia = "B"
            st.info(f"Assegnata: SUB-FASCIA B")
        else:
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C")


        chiedi_cond_sat = True

    elif pulizia(via) in stradario_lecce[2]:

        fasce_zona = {"A": (4.70, 5.40), "B": (3.90, 4.60), "C": (3.00, 3.80)}

        car1 = st.checkbox("Allacciamento al gas metano")
        car2 = st.checkbox("Ascensore a partire dal 3° piano")
        car3 = st.checkbox("Autoclave")
        car4 = st.checkbox("Verde condominiale")
        car5 = st.checkbox("Cortile in comune")
        car6 = st.checkbox(
            "Impianto elettrico interno adeguato alla legge n.37/08 (già n.46/90)")
        car7 = st.checkbox("Impianto di ricezione satellitare")
        car8 = st.checkbox("Riscaldamento centralizzato oppure autonomo")
        car9 = st.checkbox("Porta blindata")
        car10 = st.checkbox("Ripostiglio e/o Cantina")
        car11 = st.checkbox("Doppi servizi")
        car12 = st.checkbox("Impianto di condizionamento")
        car13 = st.checkbox("Infissi interni ed esterni in buono stato")
        car14 = st.checkbox("Posto auto")
        car15 = st.checkbox("2° Posto auto")
        car16 = st.checkbox("Attico")

        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14, car15,
                      car16]
        counter = sum(con for con in condizioni if con == True)

        st.markdown("**Condizioni Speciali**")


        zona_pregio = False
        if pulizia(via) in sub_pregio_tratto[2]:
            zona_pregio = st.checkbox(
                "La via è in sub-zona di pregio solo per un tratto: il civico ricade nel tratto di pregio?",
                help="Tratti di pregio: Viale della Libertà sino a via Lupiae; Viale dello Stadio sino a via Marinosci; Via Vecchia Frigole nel tratto ricadente in zona 2.")
        elif pulizia(via) in sub_pregio_lecce[2]:
            zona_pregio = True
            st.info("Via classificata in sub-zona di pregio (P) dall'allegato 1: concorre all'accesso diretto alla sub-fascia A")
        immobile_A7 = st.checkbox("Immobili accatastati A/7")
        buone_condizioni = st.checkbox(
            "Stabile e appartamento in buone condizioni",
            help="Condizione essenziale per la collocazione nella sub-fascia A (allegato 3: portone e citofono funzionanti, pavimentazioni e rivestimenti senza distacchi, infissi con chiusure e oscuramenti funzionanti, impianto di adduzione e scarico acqua funzionanti, ecc.).")
        servizi_esterni = st.checkbox("Servizi igienici posti all'esterno dell'alloggio")

        if servizi_esterni == True or (car8 == False and car3 == False):
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C (servizi igienici esterni oppure immobile privo di riscaldamento e di autoclave)")
        elif (counter >= 9 or zona_pregio == True or immobile_A7 == True) and car6 == True and buone_condizioni == True:
            fascia = "A"
            st.success(f"Assegnata: SUB-FASCIA A")
        elif counter >= 6:
            fascia = "B"
            st.info(f"Assegnata: SUB-FASCIA B")
        else:
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C")


        elementi_pregio_zona = [car12, car7]
        nota_posto_auto = True

    elif pulizia(via) in stradario_lecce[3]:

        fasce_zona = {"A": (3.90, 4.30), "B": (3.20, 3.80), "C": (2.40, 3.20)}

        car1 = st.checkbox("Allacciamento al gas metano")
        car2 = st.checkbox("Ascensore a partire dal 3° piano")
        car3 = st.checkbox("Autoclave")
        car4 = st.checkbox("Verde esclusivo")
        car5 = st.checkbox("Verde condominiale e/o verde attrezzato")
        car6 = st.checkbox("Cortile in comune")
        car7 = st.checkbox("Impianto elettrico interno adeguato alla legge n.37/08 (già n. 46/90)")
        car8 = st.checkbox("Impianto di ricezione satellitare")
        car9 = st.checkbox("Impianti sportivi")
        car10 = st.checkbox("Riscaldamento centralizzato oppure autonomo")
        car11 = st.checkbox("Porta blindata")
        car12 = st.checkbox("Ripostiglio e/o cantina")
        car13 = st.checkbox("Doppi servizi")
        car14 = st.checkbox("Impianto di condizionamento")
        car15 = st.checkbox("Infissi interni ed esterni in buono stato")
        car16 = st.checkbox("1° Posto auto")
        car17 = st.checkbox("2° Posto auto")
        car18 = st.checkbox("Box auto")
        car19 = st.checkbox("Cassaforte")
        car20 = st.checkbox("Parquet")
        car21 = st.checkbox("Attico")

        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10,
                      car11, car12, car13, car14, car15, car16, car17, car18, car19, car20, car21]

        counter = sum(con for con in condizioni if con == True)

        st.markdown("**Condizioni Speciali**")

        rifiniture = st.checkbox(
            "Particolari rifiniture: piastrellatura di almeno due metri in entrambi i servizi e nella cucina, pavimentazione in marmo od altro di particolare pregio")
        buone_condizioni = st.checkbox(
            "Stabile e appartamento in buone condizioni",
            help="Condizione essenziale per la collocazione nella sub-fascia A (allegato 3: portone e citofono funzionanti, pavimentazioni e rivestimenti senza distacchi, infissi con chiusure e oscuramenti funzionanti, impianto di adduzione e scarico acqua funzionanti, ecc.).")
        servizi_esterni = st.checkbox("Servizi igienici posti all'esterno dell'alloggio")

        if servizi_esterni == True or (car10 == False and car3 == False):
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C (servizi igienici esterni oppure immobile privo di riscaldamento e di autoclave)")
        elif (counter >= 13 or rifiniture == True) and car7 == True and buone_condizioni == True:

            fascia = "A"
            st.success(f"Assegnata: SUB-FASCIA A")
        elif counter >= 8:
            fascia = "B"
            st.info(f"Assegnata: SUB-FASCIA B")
        else:
            fascia = "C"
            st.warning(f"Assegnata: SUB-FASCIA C")


        elementi_pregio_zona = [car14, car8]
        nota_posto_auto = True

    if pulizia(via) in stradario_lecce[1] or pulizia(via) in stradario_lecce[2] or pulizia(via) in stradario_lecce[3]:

        st.subheader("Incrementi di fascia")

        if chiedi_cond_sat == True:
            p_cond = st.checkbox("Impianto di condizionamento")
            p_sat = st.checkbox("Impianto satellitare")
            elementi_pregio_zona = [p_cond, p_sat]

        allarme = st.checkbox("Impianto di allarme")
        videosorveglianza = st.checkbox("Videosorveglianza")
        domotica = st.checkbox("Domotica")

        lista_pregio = elementi_pregio_zona + [allarme, videosorveglianza, domotica]
        elementi_pregio = sum(el for el in lista_pregio if el == True)

        ammobiliato = st.checkbox("Immobile totalmente ammobiliato?", help="""Per immobile totalmente ammobiliato si intende quello dotato dei seguenti arredi:
            -Cucina
            -Pensili a muro oppure credenza
            -Frigorifero
            -Fornello
            -Tavolo con sedie
            -Scolapiatti e stoviglie
            -Camera da letto
            -Letto con materasso
            -Comodino
            -Armadio e/o guardaroba
            -Sedia
            -Camera — studio
            -Scrivania con sedia
            -Libreria
            -Soggiorno — tinello
            -Tavolo con sedie
            -Vetrinetta
            -Bagno arredato (mensole, specchio, e sedile)

            Tutte le camere devono essere provviste di idonea illuminazione elettrica.
            Per immobile parzialmente arredato si intende quello dotato di parte degli arredi innanzi indicati. Gli arredi del vano cucina, della camera da letto e del bagno devono essere sempre presenti.""")

        parz_ammobiliato = st.checkbox("Immobile parzialmente arredato?")


        ordine_fasce = ["C", "B", "A"]
        indice_fascia = ordine_fasce.index(fascia)
        perc_arredo = 0.0

        if elementi_pregio >= 2 and indice_fascia < 2:
            indice_fascia = indice_fascia + 1
            st.info("Incremento di una fascia: almeno due elementi di pregio fra condizionamento, allarme, videosorveglianza, domotica e impianto satellitare")

        if ammobiliato == True and parz_ammobiliato == True:
            st.warning("Entrambe le opzioni di arredamento sono spuntate: selezionarne una sola")
        elif ammobiliato == True or parz_ammobiliato == True:
            if indice_fascia < 2:
                indice_fascia = indice_fascia + 1
                st.info("Incremento di una fascia: immobile ammobiliato")
            else:
                if ammobiliato == True:
                    perc_arredo = 0.20
                else:
                    perc_arredo = 0.08
                st.info(f"Immobile già in fascia A: aumento del canone del {int(perc_arredo * 100)}% per l'arredo")

        fascia_finale = ordine_fasce[indice_fascia]
        can_min, can_max = fasce_zona[fascia_finale]
        st.write(f"Sub-fascia finale: {fascia_finale} ({can_min:.2f} - {can_max:.2f} €/mq)")

        st.subheader("Maggiorazioni del canone")

        pregio_catastale = st.checkbox(
            "Immobile di particolare pregio: categoria catastale A/1, A/8, A/9 oppure vincolato ai sensi del D.Lgs. 42/04 (+15%)",
            help="""Spuntare solo se ricorre almeno una delle seguenti condizioni:

            -Categoria catastale A/1 (abitazione di tipo signorile): unità in fabbricati ubicati in zone di pregio, con caratteristiche costruttive, tecnologiche e di rifinitura di livello superiore a quello dei fabbricati residenziali ordinari.
            -Categoria catastale A/8 (abitazione in villa): immobile caratterizzato dalla presenza di parco e/o giardino, con caratteristiche costruttive e rifiniture di livello superiore all'ordinario.
            -Categoria catastale A/9: castelli e palazzi di eminenti pregi artistici o storici.
            -Immobile vincolato ai sensi del D.Lgs. 42/2004 (Codice dei beni culturali, già L. 1089/39): esiste una dichiarazione di interesse culturale della Soprintendenza (vincolo diretto), di norma trascritta nei registri immobiliari e richiamata nell'atto di provenienza.

            La categoria catastale si legge nella visura catastale dell'immobile; il vincolo risulta dal decreto di vincolo, dall'atto di acquisto o può essere verificato presso la Soprintendenza.
            NON basta che l'immobile sia ristrutturato, ben rifinito o in zona centrale: contano esclusivamente la categoria catastale o il vincolo formale. Se ricorre una di queste condizioni, il canone unitario è aumentato del 15%.""")
        classe_energetica = st.checkbox("Classe energetica C o superiore (+10%)")
        nuova_costruzione = st.radio(
            "Immobile costruito, integralmente ristrutturato o completamente restaurato (fine lavori) prima dell'inizio della locazione:",
            ["No, oppure oltre il quinto anno prima",
             "Dal quinto al quarto anno prima (+8%)",
             "Dal terzo al secondo anno prima (+10%)",
             "Entro l'anno prima (+15%)"])
        durata = st.radio(
            "Durata del contratto:",
            ["3 anni + 2 (ordinaria)",
             "4 anni (+3%)",
             "5 o 6 anni (+6%)",
             "Oltre 6 anni (+10%)"])




        perc_totale = 0.0
        if pregio_catastale == True:
            perc_totale = perc_totale + 0.15
        if classe_energetica == True:
            perc_totale = perc_totale + 0.10
        if nuova_costruzione == "Dal quinto al quarto anno prima (+8%)":
            perc_totale = perc_totale + 0.08
        elif nuova_costruzione == "Dal terzo al secondo anno prima (+10%)":
            perc_totale = perc_totale + 0.10
        elif nuova_costruzione == "Entro l'anno prima (+15%)":
            perc_totale = perc_totale + 0.15
        if durata == "4 anni (+3%)":
            perc_totale = perc_totale + 0.03
        elif durata == "5 o 6 anni (+6%)":
            perc_totale = perc_totale + 0.06
        elif durata == "Oltre 6 anni (+10%)":
            perc_totale = perc_totale + 0.10
        if perc_arredo > 0:
            perc_totale = perc_totale + perc_arredo

        can_min = can_min + can_min * perc_totale
        can_max = can_max + can_max * perc_totale


        mq_netta = mq_tot

        st.subheader("1. Accessori e pertinenze")

        if nota_posto_auto == True:
            st.caption(
                "Nota: per gli immobili costruiti dopo il 1973 il primo posto auto ovvero box auto di pertinenza dell'immobile non può essere affittato separatamente dall'appartamento.")

        if st.checkbox("Presenti balconi, terrazze ad uso esclusivo o cantine?"):
            mq_balconi = st.number_input("Inserire i mq (balconi, terrazze, cantine):")
            mq_tot += mq_balconi * 0.25

        if st.checkbox("Presente autorimessa singola?"):
            mq_autorimessa = st.number_input("Inserire i mq dell'autorimessa singola:")
            mq_tot += mq_autorimessa * 0.50

        if st.checkbox("Presente posto macchina in autorimesse di uso comune?"):
            mq_posto_comune = st.number_input("Inserire i mq del posto macchina (autorimessa comune):")
            mq_tot += mq_posto_comune * 0.20

        if st.checkbox("Presente posto macchina in spazi comuni?"):
            mq_posto_spazi = st.number_input("Inserire i mq del posto macchina (spazi comuni):")
            mq_tot += mq_posto_spazi * 0.15

        if st.checkbox("Presente superficie scoperta ad uso esclusivo (area verde o pavimentata non a livello)?"):
            mq_scoperta = st.number_input("Inserire i mq della superficie scoperta:")

            if mq_scoperta > 0:

                mq_scoperta_utile = min(mq_scoperta, 300.0)


                if mq_scoperta_utile <= mq_netta:
                    mq_tot += mq_scoperta_utile * 0.20
                else:
                    mq_tot += (mq_netta * 0.20) + ((mq_scoperta_utile - mq_netta) * 0.10)

        st.subheader("Altre superfici")

        if st.checkbox("Presenti vani con altezza utile compresa fra 1,00 e 1,70 metri?"):
            mq_vani_bassi = st.number_input("Inserire i mq dei vani (h 1,00 - 1,70 m):")
            mq_tot += mq_vani_bassi * 0.70

        if st.checkbox("Presenti soppalchi ed ammezzati con altezza utile superiore a 1,70 metri (con scala fissa)?"):
            mq_soppalchi = st.number_input("Inserire i mq dei soppalchi/ammezzati:")
            mq_tot += mq_soppalchi * 1.00


        maggiorazione_superficie = 0.0
        riduzione_superficie = 0.0

        if mq_netta > 0 and mq_netta < 45.0:
            maggiorazione_superficie = 0.25
        elif mq_netta >= 45.0 and mq_netta < 60.0:
            maggiorazione_superficie = 0.20

        if mq_tot > 115.0:
            riduzione_superficie = 0.10

        moltiplicatore = 1.0 + maggiorazione_superficie - riduzione_superficie
        mq_tot = mq_tot * moltiplicatore

        can_finale_min = mq_tot * can_min
        can_finale_max = mq_tot * can_max

        lala = st.button("Stima il range")

        if lala:
            if ammobiliato == True and parz_ammobiliato == True:
                st.warning("Correggere le opzioni di arredamento per ottenere la stima")
            else:
                st.success(f"Range di canone stimato: da {can_finale_min:.2f} € a {can_finale_max:.2f} €")

