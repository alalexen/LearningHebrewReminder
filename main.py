from add_words_from_pealim import AddWord
from get_sentence_example import Reverso
from questions_verbs import *


def ask_action():
    ask_action = input(
        f"""What do you want to do?:
         \n1 - Practice vocabulary\n2 - Add new verbs to your vocabulary\n3 - Add examples for word(s) with translation 
         \nyour answer: """
    )
    return int(ask_action)


def ask_words(input_text: str):
    words = input(input_text)
    return [words]


if __name__ == '__main__':
    action = ask_action()
    input_text = "Provide the words in Hebrew separated by comma."

    if action == 2:
        # Adding new words to the verbs.csv:
        input_text += " Please provide infinitives only"
        words = ask_words(input_text)
        add_words = AddWord()
        add_words.add_verbs_to_file_batch(words)
    elif action == 3:
        words = ask_words(input_text)
        # Adding examples to examples.csv:
        for w in words:
            r = Reverso(w)
            res = r.get_example()
            r.add_example_to_file(res['he'], res['en'])
    else:
        # Practice:
        app = ChooseCorrectTranslation()

        print("*** Note! If you want practice vocabulary, check you have words added ***")
        type = int((input("\nHow do you want to practice?\n1: Select the correct translation\n2: Select the correct form\nyour answer:")))
        if type == 1:
            # terminal:
            for _ in range(10):
                app.which_infinitive_translation_is_correct()
        else:
                app.run()