import random
from get_word import get_one_random_verb


def which_infinitive_translation_is_correct():
    verbs = []
    for _ in range(4):
        verb = get_one_random_verb()
        verbs.append(verb)

    correct_answer = random.choice(verbs)

    options = {}
    i = 1
    for w in verbs:
        options[i] = w["infinitive"]
        i += 1

    input_result = input(
        f"""Select the correct translation of '{correct_answer['translation']}':
        \n{options[1]} - 1\n{options[2]} - 2\n{options[3]} - 3\n{options[4]} - 4\nyour answer: """
    )

    verify_answer(
        input_result=int(input_result),
        options=options,
        correct_answer=correct_answer["infinitive"],
    )


def which_conjugation_is_correct():
    """Choose random words and ask which one corresponds to the translation in a specific conjugation type."""
    verb = get_one_random_verb()

    correct_answer = verb["random_conjugation"]
    random_answers = random.sample(verb["all_conjugations"], 4)
    if correct_answer not in random_answers:
        random_index = random.randint(0, len(random_answers) - 1)
        random_answers[random_index] = correct_answer

    options = {}
    i = 1
    for w in random_answers:
        options[i] = w
        i += 1

    input_result = input(
        f"""Select the correct form of >> {verb['translation']}  - {verb['form']}
        \n{options[1]} - 1\n{options[2]} - 2\n{options[3]} - 3\n{options[4]} - 4\nyour answer: """
    )

    verify_answer(
        input_result=int(input_result), options=options, correct_answer=correct_answer
    )


def verify_answer(input_result: int, options: dict, correct_answer: str, num_of_options: int = 4):
    """Verify provided input"""
    if not (1 <= input_result <= num_of_options):
        print("Provide correct number")
        return
    else:
        answer = options[input_result]

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"{correct_answer} <-- The correct answer is ")


which_conjugation_is_correct()
which_infinitive_translation_is_correct()
