import customtkinter as ctk

class App(ctk.CTk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title("Translator")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        self.window_title = ctk.CTkLabel(
            self,
            text="Automatic Translation Tool".replace(
                    "               ",
                    ""
                ),
            font = ("JetBrains Mono", 36)
        )
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, text="Launch", command=button_function)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.mainloop()

def button_function():
    print("button pressed")

def main():
    ctk.set_appearance_mode("dark")
    App()


if __name__ == "__main__":
    main()