import csv
import random

from locators import conjugations as conj


def get_one_random_verb() -> dict:
    """
    Get one random line from verbs.csv file
    :return:
    all_conjugations: the line form file
    infinitive: infinitive
    translation: translation,
    random_conjugation: random word from the line except infinitive,
    form: type of the conjugation in English
    """
    with open("verbs.csv", "r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        verb_line = random.choice(reader)
        word = random.choice([w for w in verb_line if verb_line.index(w) != 0])
        translation = get_translation(reader.index(verb_line))

    return {
        "all_conjugations": verb_line,
        "infinitive": verb_line[0],
        "translation": translation,
        "random_conjugation": word,  # infinitive is excluded
        "form": get_form(verb_line.index(word)),
    }


def get_translation(index):
    with open("verbs_translations.csv", "r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        return reader[index][0]


def get_form(index):
    conjugations = list(conj.keys())
    return conjugations[index]
