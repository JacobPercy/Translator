import customtkinter as ctk
import tkinter

class App(ctk.CTk):
    
    def __init__(self):
        def clear_screen(self):
            for widget in self.winfo_children():
                widget.destroy()
        def button_function():
            clear_screen(self.window_title)
        super().__init__()
        self.title("Translator")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        self.window_title = ctk.CTkLabel(
            self,
            text="Automatic Translation Tool".replace(
                    "               ",
                    ""
                ),
            font = ("JetBrains Mono", 75)
        )
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, text="Launch", command=button_function)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.mainloop()

def main():
    ctk.set_appearance_mode("dark")
    App()

if __name__ == "__main__":
    main()