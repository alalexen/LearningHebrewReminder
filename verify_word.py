import csv
import unicodedata
import random

header = ["Base Form", "Masculine", "Feminine", "Masculine Plural", "Feminine Plural", "Past Tense I",
          "Past Tense You Male", "Past Tense You Female", "Past Tense He", "Past Tense She", "Past Tense We",
          "Past Tense You Plural Male", "Past Tense You Plural Female", "Past Tense They Plural Male",
          "Past Tense They Plural Female", "Future Tense I", "Future Tense You Male", "Future Tense You Female",
          "Future Tense He", "Future Tense She", "Future Tense We", "Future Tense You Plural Male",
          "Future Tense You Plural Female", "Future Tense They Plural Male", "Future Tense They Plural Female"]


def get_one_random_verb():
    with open("verbs.csv", "r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        verb_line = random.choice(reader)
        word = random.choice([w for w in verb_line if verb_line.index(w) != 0])
        translation = get_translation(reader.index(verb_line))
    return {"infinitive": verb_line[0][::-1], "translation": translation, "word": word[::-1],
            "form": get_form(verb_line.index(word))}


def get_form(index):
    return header[index]


def get_translation(index):
    with open("translations.csv", "r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        return reader[index][0]


def remove_diacritics(text):
    return ''.join([c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)])


def ask_for_infinitive_translation_and_verify():
    verb = get_one_random_verb()
    for a in range(3):
        ask_hebrew_translation = input(f"Please translate: {verb['translation']}\nyour answer: ")
        print(ask_hebrew_translation[::-1])
        if remove_diacritics(verb['infinitive'])[::-1] == ask_hebrew_translation:
            print("You're right!")
            break
        else:
            print("Incorrect answer, please try again")
        if a == 2:
            print(f"The correct answer is {verb['infinitive']}")


def ask_for_verb_form_translation_and_verify():
    verb = get_one_random_verb()
    for a in range(3):
        ask_hebrew_translation = input(
            f"Please put the verb {verb['infinitive']} to the form '{verb['form']}' \nyour answer: ")
        print(ask_hebrew_translation[::-1])
        if remove_diacritics(verb['word'])[::-1] == ask_hebrew_translation:
            print("You're right!")
            break
        else:
            print("Incorrect answer, please try again")
        if a == 2:
            print(f"The correct answer is {verb['word']}")


ask_for_infinitive_translation_and_verify()
ask_for_verb_form_translation_and_verify()
