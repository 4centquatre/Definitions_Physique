import streamlit as st
from random import randint

dico = {
    0: ["Acide selon Brönsted", "Espèce susceptible de céder un proton H+ (ex : AH, RCOOH)."],
    1: ["Base selon Brönsted", "Espèce susceptible de capter un proton H+ (ex : A-, RCOO-)."],
    2: ["Oxydant", "Espèce capable de capter un ou plusieurs électrons. Il peut être réduit."],
    3: ["Réducteur", "Espèce capable de céder un ou plusieurs électrons. Il peut être oxydé."],
    4: ["Oxydation", "Perte d'électrons. Un réducteur perd des électrons et subit une oxydation."],
    5: ["Couple ox/red", "Oxydant et réducteur d'un même couple, espèces conjuguées."],
    6: ["Volume molaire Vm", "Volume occupé par une mole de gaz à une température donnée."],
    7: ["Alcoolémie", "Taux d'alcool (éthanol) dans le sang."],
    8: ["Éthylotest chimique", "Test colorimétrique révélant l'éthanol par une réaction chimique avec changement de couleur."],
    9: ["Indicateur colorimétrique", "Espèce dont la couleur varie en fonction du pH (utilisé en dosage pH-métrique)."],
    10: ["DJA (Dose Journalière Admissible)", "Quantité de substance qu'un individu peut ingérer sans risque par jour et par kg de masse corporelle."],
    11: ["DJT (Dose Journalière Tolérable)", "Quantité de contaminants qu'un individu peut ingérer sans risque par jour et par kg de masse corporelle."],
    12: ["Conductivité électrique", "Grandeur évaluant la capacité d'une solution à conduire l'électricité, mesurée avec un conductimètre."],
    13: ["Équivalence (dosage)", "Moment où les réactifs sont introduits dans les proportions stœchiométriques."],
    14: ["Micropolluant", "Espèce présente à très faible concentration dans l'eau (ng/L), pouvant persister dans les eaux traitées."],
    15: ["Hypoxie", "Diminution de la quantité d'oxygène apportée aux tissus par le sang."],
    16: ["Ozone (O₃)", "Gaz absorbant les UV dangereux du soleil (couche située à 20-30 km d'altitude)."],
    17: ["Monoxyde de carbone (CO)", "Gaz indolore, incolore et toxique."],
    18: ["Effet de serre naturel", "Permet de maintenir une température moyenne d'environ 15°C sur Terre."],
    19: ["Gaz à effet de serre", "Gaz responsables du réchauffement climatique (CO₂, méthane…)."],
    20: ["Ultrasons", "Ondes sonores de fréquence > 20 000 Hz, inaudibles pour l'humain."],
    21: ["Principe de l'échographie", "Imagerie utilisant les ultrasons émis/réfléchis par une sonde selon le principe de l'écho."],
    22: ["Échographie Doppler", "Technique utilisant l'effet Doppler pour mesurer la vitesse et le sens du flux sanguin."],
    23: ["Radiographie", "Technique basée sur l'absorption différentielle des rayons X selon la densité des tissus."],
    24: ["Opacités (radiographie)", "Zones claires correspondant aux tissus denses absorbant fortement les rayons X."],
    25: ["Clartés (radiographie)", "Zones sombres correspondant aux tissus peu absorbants."],
    26: ["Radiothérapie", "Traitement anticancéreux utilisant des rayons X pour détruire les cellules cancéreuses."],
    27: ["Produit de contraste", "Molécules sensibles au champ magnétique améliorant la qualité des images médicales."],
    28: ["Isotope", "Noyau d'un même élément ayant le même nombre de protons mais un nombre différent de neutrons."],
    29: ["Période radioactive (demi-vie)", "Temps au bout duquel la moitié des noyaux radioactifs se sont désintégrés."],
    30: ["Activité radioactive A", "Nombre de désintégrations par seconde (en becquerels, Bq)."],
    31: ["Dose absorbée D", "Énergie absorbée par unité de masse corporelle irradiée (en Gray, Gy)."],
    32: ["Absorbance A", "Grandeur mesurant la capacité d'une espèce colorée à absorber la lumière visible."],
    33: ["Acide aminé", "Composé possédant une fonction acide carboxylique (-COOH) et une fonction amine (-NH₂) sur le même carbone."],
    34: ["Carbone asymétrique C*", "Carbone tétragonal lié à quatre atomes ou groupes différents."],
    35: ["Molécule chirale", "Molécule non superposable à son image dans un miroir, possédant au moins un carbone asymétrique."],
    36: ["Énantiomères", "Molécules images l'une de l'autre dans un miroir, non superposables."],
    37: ["Dipeptide", "Molécule obtenue par condensation de deux acides aminés (liaison peptidique)."],
    38: ["Triglycéride", "Triester du glycérol et de trois acides gras (lipides)."],
    39: ["Acide gras", "Acide carboxylique RCOOH à longue chaîne carbonée, saturée ou insaturée."],
    40: ["Acide gras saturé", "Acide gras de formule brute CnH2nO2."],
    41: ["Hydrolyse des triglycérides", "Destruction d'une liaison chimique par fixation d'eau, produisant acides gras et glycérol."],
    42: ["Liposoluble", "Soluble dans les graisses (molécules à longues chaînes carbonées)."],
    43: ["Hydrosoluble", "Soluble dans l'eau grâce aux liaisons O-H formant des liaisons hydrogène."],
    44: ["Béomédicament", "Association d'un principe actif et d'un vecteur guidant celui-ci vers les cellules à traiter."]
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

st.title("Quiz Définitions")

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
    st.session_state.indice = 0
    st.session_state.step = "reponse"
    st.rerun()

if st.session_state.step == "reponse":
    indice2 = randint(0,len(st.session_state.dico[st.session_state.indice])-1)
    st.session_state.indice2 = indice2
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