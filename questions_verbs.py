from get_word import get_one_random_verb
import customtkinter
import random


class ChooseCorrectConjugation:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.title("Hebrew reminder")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.window.geometry("500x200+1500+10")
        self.window.attributes("-topmost", True)

        self.correct_data = self.generate_options_for_conjugation()

        # text
        self.label = customtkinter.CTkLabel(
            self.window, text=self.correct_data["text"], font=("Arial Bold", 15), wraplength=500
        )
        self.label.pack()

        # buttons
        self.create_button("1", 150, 125, lambda: self.which_button_pressed(1))
        self.create_button("2", 205, 125, lambda: self.which_button_pressed(2))
        self.create_button("3", 260, 125, lambda: self.which_button_pressed(3))
        self.create_button("4", 315, 125, lambda: self.which_button_pressed(4))

    def create_button(self, text, x, y, command):
        button = customtkinter.CTkButton(
            self.window, text=text, width=35, height=20, command=command
        )
        button.place(x=x, y=y)

    def which_button_pressed(self, button):
        self.verify_answer(button, self.correct_data["options"], self.correct_data["correct_answer"])

    @staticmethod
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

    def verify_answer(self, input_result: int, options: dict, correct_answer: str, num_of_options: int = 4):
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
            self.window,
            text=result,
            font=("Aria Bolt", 15),
            wraplength=500,
            text_color=text_color,
            height=30,
        )
        label.pack()
        self.window.after(2000, self.window.destroy)

    def run(self):
        self.window.mainloop()


class ChooseCorrectTranslation(ChooseCorrectConjugation):
    # terminal only

    def which_infinitive_translation_is_correct(self):
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

        self.verify_answer(
            input_result=int(input_result),
            options=options,
            correct_answer=correct_answer["infinitive"],
        )
