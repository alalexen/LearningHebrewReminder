import random
from get_word import get_one_random_verb


# terminal only
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


def generate_options_for_conjugation():
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

    text = f"""Select the correct form of >> {verb['translation']}  - {verb['form']}
        \n{options[1]} - 1  {options[2]} - 2  {options[3]} - 3  {options[4]} - 4"""

    return {"text": text, "options": options, "correct_answer": correct_answer}


def verify_answer(
    input_result: int, options: dict, correct_answer: str, num_of_options: int = 4
):
    """Verify provided input"""
    if not (1 <= input_result <= num_of_options):
        print("Provide correct number")
        return "Provide correct number"
    else:
        answer = options[input_result]

    if answer == correct_answer:
        print("Correct!")
        result = "Correct!"
    else:
        print(f"{correct_answer} <-- The correct answer is ")
        result = f"{correct_answer} <-- The correct answer is "

    text_color = "green" if result == "Correct!" else "red"
    label = customtkinter.CTkLabel(
        window,
        text=result,
        font=("Aria Bolt", 15),
        wraplength=500,
        text_color=text_color,
        height=30,
    )
    label.pack()
    window.after(2000, window.destroy)


# which_infinitive_translation_is_correct()


# # ------------------- GUI -------------------

import customtkinter

window = customtkinter.CTk()
window.title("Hebrew reminder")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
window.geometry("500x200+1500+10")
window.attributes("-topmost", True)

correct_data = generate_options_for_conjugation()

# text
label = customtkinter.CTkLabel(
    window, text=correct_data["text"], font=("Aria Bolt", 15), wraplength=500
)
label.pack()


def which_button_pressed(button: int):
    verify_answer(button, correct_data["options"], correct_data["correct_answer"])


# buttons
button1 = customtkinter.CTkButton(
    window, text="1", width=35, height=20, command=lambda l=1: which_button_pressed(l)
)
button1.pack()
button1.place(x=150, y=125)

button2 = customtkinter.CTkButton(
    window, text="2", width=35, height=20, command=lambda l=2: which_button_pressed(l)
)
button2.place(x=205, y=125)

button3 = customtkinter.CTkButton(
    window, text="3", width=35, height=20, command=lambda l=3: which_button_pressed(l)
)
button3.place(x=260, y=125)

button4 = customtkinter.CTkButton(
    window, text="4", width=35, height=20, command=lambda l=4: which_button_pressed(l)
)
button4.place(x=315, y=125)


window.mainloop()
