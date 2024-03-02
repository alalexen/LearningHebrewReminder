from get_word import get_one_random_verb
import random
import time


def conjugation(options_amount: int = 4):
    verb = get_one_random_verb()

    correct_answer = verb["random_conjugation"]
    random_answers = random.sample(verb["all_conjugations"], options_amount)
    if correct_answer not in random_answers:
        random_index = random.randint(0, options_amount - 1)
        random_answers[random_index] = correct_answer

    options = {i: v for i, v in enumerate(random_answers, 1)}

    input_result = input(
        f"""({verb['form']}) Choose correct form: {verb['translation']} -
        \n{options[1]} - 1\n{options[2]} - 2\n{options[3]} - 3\n{options[4]} - 4\nyour answer: """
    )

    res = verify_answer(
        input_result=int(input_result),
        options=options,
        correct_answer=correct_answer
    )
    return res


def word_translation(options_amount: int = 4):
    verbs = []
    start_time = time.time()
    timeout = 10
    while len(verbs) < options_amount and time.time() - start_time < timeout:
        verb = get_one_random_verb()
        if verb not in verbs:
            verbs.append(verb)

    correct_answer = random.choice(verbs)

    options = {i: w["infinitive"] for i, w in enumerate(verbs, 1)}

    input_result = input(
        f"""Select the correct translation of '{correct_answer['translation']}':
        \n{options[1]} - 1\n{options[2]} - 2\n{options[3]} - 3\n{options[4]} - 4\nyour answer: """
    )

    res = verify_answer(
        input_result=int(input_result),
        options=options,
        correct_answer=correct_answer["infinitive"],
    )
    return res


def verify_answer(input_result: int, options: dict, correct_answer: str, num_of_options: int = 4):
    """Verify provided input"""
    if not (1 <= input_result <= num_of_options):
        print("Provide correct number")
        return "Provide correct number"
    else:
        answer = options[input_result]

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"{correct_answer} <-- The correct answer is ")
        return 0

