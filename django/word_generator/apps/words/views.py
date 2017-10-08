from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if not request.session['count']:
        request.session['count'] = 0

    return render(request,'words/index.html')

def words(request):
    words = [
        "Discrimination",
        "Photosynthesis",
        "Constantinople",
        "Saponification",
        "Transformation",
        "Multiplication",
        "Capitalization",
        "Transportation",
        "Trichomoniasis",
        "Responsibility",
        "Disappointment",
        "Conjunctivitis",
        "Representative",
        "Expressionless",
        "Representation",
        "Capitalisation",
        "Disambiguation",
        "Chemosynthesis",
        "Gentrification",
        "Groundbreaking",
        "Defenestration",
        "Administration",
        "Interpretation",
        "Accountability",
        "Paleontologist",
        "Identification",
        "Understandable",
        "Schweinsteiger",
        "Specialization",
        "Benzodiazepine",
        "Classification",
        "Accomplishment",
        "Generalization",
        "Teleprocessing",
        "Hyperlipidemia",
        "Neutralization",
        "Ridiculousness",
        "Archaebacteria",
        "Abdominoplasty",
        "Infrastructure",
        "Autosuggestion",
        "Communications",
        "Antidepressant",
        "Counterculture",
        "Initialisation",
        "Procrastinator",
        "Chromatography",
        "Administrative",
        "Characteristic",
        "Abstemiousness",
        "Gerrymandering",
        "Reconstruction",
        "Abstractedness",
        "Acceptableness",
        "Cardiovascular",
        "Neutralisation",
        "Beautification",
        "Anthropometric",
        "Slaughterhouse",
        "Acanthocytosis",
        "Remarkableness",
        "Staphylococcus",
        "Acknowledgment",
        "Accommodations",
        "Accomplishable",
        "Presupposition",
        "Simplification",
        "Understatement",
        "Pasteurization",
        "Absentmindedly",
        "Rehabilitation",
        "Aggrandizement",
        "Reconciliation",
        "Electrophysics",
        "Thermodynamics",
        "Apprenticeship",
        "Anesthesiology",
        "Teleconference",
        "Foreordination",
        "Achondroplasia",
        "Forthrightness",
        "Extemporaneous",
        "Abdominousness",
        "Polymerization",
        "Salubriousness",
        "Westernization",
        "Nanotechnology",
        "Libidinousness",
        "Administrating",
        "Anathematizing",
        "Naturalization",
        "Hyperventilate",
        "Stratification",
        "Candlelighting",
        "Biodegradation",
        "Authentication",
        "Disorientation",
        "Associationism",
        "Diverticulitis",
        "Electioneering"
    ]

    request.session['word'] = (random.choice(words))
    request.session['count'] += 1
    return redirect('/')


def reset(request):

    del request.session['word']
    request.session['count'] = 0

    return redirect('/')
