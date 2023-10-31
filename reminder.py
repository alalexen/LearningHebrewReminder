from get_word import get_one_random_verb
import customtkinter

# # ------------------- Reminder -------------------

window = customtkinter.CTk()
customtkinter.set_default_color_theme("green")
window.title("Hebrew reminder")
customtkinter.set_appearance_mode("dark")

window.geometry("800x100+1500+10")

window.attributes("-topmost", True)
random_verb = get_one_random_verb()

text = (
    f"{random_verb['infinitive']}" + " \n * * * \n " + f"{random_verb['translation']}"
)
print(text)
label = customtkinter.CTkLabel(window, text=text, font=("Aria Bolt", 20))
label.place(relx=1, rely=0, anchor="ne")

label.pack()


window.after(5000, window.destroy)
window.mainloop()
