import streamlit as st
from random import randint

dico = {
    0: ["Acide selon Brönsted (1ère)", "espèce susceptible de céder un proton H+ (ex: AH, RCOOH)."],
    1: ["Base selon Bronsted (1er)", "espèce susceptible de capter un proton H+ (ex: A -; RCOO-)."],
    2: ["Oxydant", "espèce capable de capter un ou plusieurs électrons. Il peut être réduit"],
    3: ["Réducteur", "espèce capable de céder un ou plusieurs électrons. Il peut être oxydé."],
    4: ["Oxydation", "perte d'électrons. Un réducteur en perdant des électrons, subit une oxydation C'est une transformation chimique qui se produit au contact du d'oxygène 02 de l'air."],
    5: ["Couple ex/red", "Ox et red d'un même couple sont des espèces conjuguées"],
    6: ["Volume molaire vn", "volume occupé par une mole de gaz (à température donnée)."],
    7: ["Alcoolémie", "taux d'alcool l'éthanol) dans le sang."],
    8: ["Éthylotest chimique", "test colorimétrique qui met en évidence l'éthanol grâce à une réaction chimique avec un changement de couleur."],
    9: ["Indicateur colorimétrique", "espèce dont la couleur varie en fonction du PH (utilisé lors d'un dosage PH-métrique)"],
    10: ["DJA: Dose Journalière Admissible", "Quantité de substance autorisée, qu'un individu peut ingérer sans risque pour sa santé, par jour et par Kilogrammes de masse corporelle"],
    11: ["DJT: Dose Journalière Tolérable", "Quantité de contaminants autorisée, qu'un individu peut ingérer sans risque pour sa Santé xe par jour et par kilogrammes de masse corporelle"],
    12: ["Conductivité électrique o d'une solution", "Grandeur permettant d'évaluer la capacité de la solution à plus ou moins conduire l'électricité. Elle se mesure à l'aide d'un conductimètre."],
    13: ["Équivalence lors d'un dosage", "A l'équivalence, les réactifs sont introduits dans les proportions stacchiométriques"],
    14: ["Micropolluant", "espèce dont la concentration est très faible dans l'eau (quelques Ng/L) pouvant se retrouver dans les eaux traitées (pesticides, détergents) médicaments etc)."],
    15: ["Hypoxie", "Diminution de la quantité d'oxygène apportée aux tissus por le sang"],
    16: ["Ozone (03)", "Gaz qui absorbe les ultra violets les plus dangereux provenant du soleil (couche d'ozone située à 20Km /30km d'altitude)."],
    17: ["Monoxyde de carbone (CO)", "Gaz indolore, incolore et toxique."],
    18: ["Effet de serre naturel", "Permet de maintenir une température moyenne d'environ 15°℃ sur terre"],
    19: ["Gaz à effet de serre", "Les GES (méthane, CO2 ... ) sont à l'origine du réchauffement et du déréglém. ent climatique."],
    20: ["Ultrasons", "Ondes sonores de fréquence supérieure à 20000 Hz et donc inaudibles à l'oreille humaine."],
    21: ["Principe de l'échographie", "Technique d'imagerie médicale basée sur l'utilisation d'ultrasons. Les ultrasons sont émis par une sonde (servant à la fois d'émetteur et de récepteur) à une certaine fréquence vers les régions à explorer. Les ondes reviennent vers la sonde Selon le principe de l'écho. Selon la densité des tissus traversés, leur éloignement par rapport à la sonde, la fréquence est plus ou moins modifiée."],
    22: ["Echographie Doppler", "Le principe repose sur l'effet Doppler qui est un changement de fréquence de l'onde sonore perque l'orsqu' un observateur est en mouvement relatif. Cette technique utilise les ultrasons qui sont réfléchis par les globules rouges en mouvement. Elle permet de mesurer le décalage de fréquence entre l'onde émise et l'onde réfléchie Ceci afin de déterminer la vitesse et le sens d'écoute- ment du sang"],
    23: ["Radiographie", "Technique basée sur l'absorption différentielle des rayons X selon la densité des tissus. Les rayons X sont envoyés sur la zone à explorer où ils vont être plus ou moins absorbés selons les tissus Ils vont ensuite impressionner un film photosensible ou être analysés par un logiciel informatique"],
    24: ["Les zones claires d'une radiographie", "sont appelées opacités et correspondent aux tissus denses ayant fortement absorbé les rayons X"],
    25: ["Les zones sombres d'une radiographie", "sont appelées clartés et correspondent aux tissus nous ayant peu absorbé les rayons X."],
    26: ["Radiothérapie", "Traitement anticancéreux qui consiste à envoyer les rayons X localement sur un point précis Suffisamment longtemps afin de détruire les cellules cancéreuses."],
    27: ["Produit de contraste", "Molécules (très sensibles au champ magnétique) infectées, permettant d'améliorer la netteté et la qualité des images en IRM, radiographie, scintigra- phie et scanographie ."],
    28: ["Isotope", "Noyau d'un même élément possédant le même nombre de protons mais un nombre différent de neutrons."],
    29: ["Période radioactive Tou demi-vie tir2", "temps au bout duquel la moitié des noyaux radioactifs (radionucléides) se sont désintégrés (pour que l'activité soit divisée par deux)."],
    30: ["Activité A d'un échantillon radioactif", "Nombre de désintégrations par seconde (ou becquerel Bg)"],
    31: ["Dose absorbée D", "Energie absorbée par l'unité de masse corporelle irradiée (en Gray Gy )"],
    32: ["Absorbance A d'une solution colorée", "Grandeur permettant d'évaluer la capacité de l'espèce chimique colorée à absorber la lumière visible. A est sans unité et est mesurée avec un spectro photomètre."],
    33: ["Acide x- aniné", "composé comportant à la fois une fonction acide carboxylique (- COOH) et une fonction anine (-NH2). L'acide est dif X-aminés lorsque les fonctions amine et acide carboxylique sont portées par le même atome ("],
    34: ["Carbone asymétrique", "C'est un carbone tetragonal lié à quatre atomes, ou groupes d'atomes différents. Un le note C*"],
    35: ["Molécule chirale", "Une molécule est dite chirale si elle n'est pas superposable à son image dans, le miroir Une molécule possédant au moins un carbone asymétrique C\" est chirale"],
    36: ["Enantiomères", "Ce sont des molécules non superposables images l'un de l'autre dans un miroir, ce sont des isomères de configuration"],
    37: ["Dipeptide", "S'obtient par la réaction de condensation entre deux acides a-antinés par formation d'une liaison peptidique (fonction amide)"],
    38: ["Triglycéride", "fait partie de la famille des lipides (97%). C'est un triester du glycerol et de trois acides"],
    39: ["Acide gras", "Acide carboxylique RCOOH, à longue chaîne carbonnée saturée (uniquement des liaisons Simples (-c) ou insaturé (au moins une double liaison (=()."],
    40: ["Acide gras saturés", "de formule brute Cn Hzn Oz."],
    41: ["Hydrolyse des triglycérides", "destruction d'une liaison chimique par fixation d'eau. Ce qui produit des acides gras et du glycerol."],
    42: ["Lyposoluble", "Soluble dans les graisses (molécules possédant de longues chaînes carbonnées \" lipophiles\")"],
    43: ["Hydrosoluble", "soluble dans l'eau (molécules possédant des liaisons O- H \"hydrophile\" qui forment des liaisons hydrogène avec l'eau)"],
    44: ["Béomédicament", "association d'un principe actif et d'un vecteur permettant de le guider jusqu'aux cellules à traiter."]
}


if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = {}
if "dico_reponses" not in st.session_state:
    st.session_state.dico_reponses = {}
if "current" not in st.session_state:
    st.session_state.current = None
if "step" not in st.session_state:
    st.session_state.step = "question"
if "end" not in st.session_state:
    st.session_state.end = {}
if "dico" not in st.session_state:
    st.session_state.dico = dico.copy()
if "indice" not in st.session_state:
    st.session_state.current = None
if "indice2" not in st.session_state:
    st.session_state.current = None

st.title("Quiz Définitions Physique")

if st.session_state.step == "question":
    st.session_state.reponse = ""
    if len(st.session_state.questions.keys()) >= len(st.session_state.dico.keys()):
        st.session_state.step = "fin"
        st.rerun()
    tab_indices = []
    for cle in st.session_state.dico.keys():
        tab_indices.append(cle)
    i = randint(0, len(tab_indices) - 1)
    while tab_indices[i] in st.session_state.questions.keys():
        i = randint(0, len(tab_indices) - 1)
    indice = tab_indices[i]
    st.session_state.indice = indice
    st.session_state.step = "reponse"
    st.rerun()

if st.session_state.step == "reponse":
    indice2 = randint(0,len(st.session_state.dico[st.session_state.indice])-1)
    st.session_state.indice2 = 0
    question = st.session_state.dico[st.session_state.indice][st.session_state.indice2]
    st.session_state.questions[st.session_state.indice] = question
    st.write("Question : "+question)
    with st.form("form_reponse"):
        reponse = st.text_input("Écris ta réponse", key="reponse_input")
        validee = st.form_submit_button("Valider")

    if st.button("Stop"):
        st.session_state.step = "fin"
        st.rerun()

    elif validee:
        st.session_state.step = "feedback"
        st.session_state.reponse = reponse
        st.session_state.dico_reponses[st.session_state.indice] = reponse   
        st.rerun()

if st.session_state.step == "feedback":
    chaine = ""
    for car in st.session_state.dico[st.session_state.indice]:
        chaine += car + " "
    st.write("La réponse était : "+chaine)
    st.write("Ta réponse était : "+st.session_state.reponse)
    vrai_faux = st.radio("Tu as eu :", ["Vrai", "Faux"], horizontal=True)

    if st.button("Continuer"):
        if vrai_faux == "Vrai":
            st.session_state.score += 1
        elif vrai_faux == "Faux":
            st.session_state.end[st.session_state.indice] = st.session_state.dico[st.session_state.indice]
        st.session_state.step = "question"
        st.rerun()

if st.session_state.step == "fin":
    st.write("C'est fini ! Ton score est de : "+str(st.session_state.score)+"/"+str(len(st.session_state.dico_reponses.keys()))+ " Bravo mon coeur t'es trop forte !")
    if len(st.session_state.end.keys())>1:
        st.write("Tes reponses fausses etaient : ")
    elif len(st.session_state.end.keys()) == 1:
        st.write("Ta reponse fausse etait : ")
    else:
        st.write("Tu n'as eu aucune reponse fausse bravo !")
    for tab in st.session_state.end.values():
        chaine = ""
        for item in tab:
            chaine = chaine + str(item) + " "
        st.write(chaine)
    if st.button("Refaire"):
        st.session_state.score = 0
        st.session_state.questions = {}
        st.session_state.end = {}
        st.session_state.current = None
        st.session_state.step = "question"
        st.session_state.dico = dico.copy()
        st.session_state.indice = None
        st.session_state.indice2 = None
        st.session_state.reponse = ""
        st.session_state.dico_reponses = {}
        st.rerun()
    elif st.button("Refaire avec tes erreurs"):
        if len(st.session_state.end) > 0:
            st.session_state.questions = {}
            st.session_state.score = 0
            st.session_state.current = None
            st.session_state.step = "question"
            st.session_state.dico = st.session_state.end.copy()
            st.session_state.end = {}
            st.session_state.indice = None
            st.session_state.indice2 = None
            st.session_state.reponse = ""
            st.session_state.dico_reponses = {}
            st.rerun()
        else:
            st.warning("Tu n'as aucune erreur à refaire.")