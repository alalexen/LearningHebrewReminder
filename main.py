from add_words_from_pealim import AddWord
from questions_verbs import *
from datetime import datetime


def ask_action():
    ask_action = input(
        f"""What do you want to do?:
         \n1 - Practice vocabulary\n2 - Add new verbs to your vocabulary
         \nyour answer: """
    )
    return int(ask_action)


def ask_words(input_text: str):
    """Input words for searching"""
    w = input(input_text)
    return w.split(",")


def save_score(score: str):
    with open("score.txt", "a") as f:
        today = datetime.now()
        text = str(today.day) + "." + str(today.month) + "." + str(today.year) + " - " + score
        f.write(f"\n{text}")
    print("Your result has been added.")


if __name__ == '__main__':
    action = ask_action()
    input_text = "Provide the words in Hebrew separated by comma."

    if action == 2:
        # Adding new words to the verbs.csv:
        input_text += " Please provide infinitives only.\n"
        words = ask_words(input_text)
        add_words = AddWord()
        add_words.add_verbs_to_file_batch(words)
    else:
        # Practice:
        score = 0
        questions = 1
        for _ in range(questions):
            res = word_translation()
            score += res
            res1 = conjugation()
            score += res1
        final_score = f"{score}/{questions*2}"
        print("Your result is " + final_score)
        save = input("Do you want to save the result? y/n: ")
        if save in ["yes", "y"]:
            save_score(final_score)