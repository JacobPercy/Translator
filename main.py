import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

app.title("Translator")



def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="Launch", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()