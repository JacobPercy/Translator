import customtkinter as ctk

class App(ctk.CTk):
    
    def __init__(self):

        super().__init__()
        self.title("Translator")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        self.window_title = ctk.CTkLabel(self,text="Translator",font = ("Calibri", 500))
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, text="LAUNCH", height=200,width=800,command=self.button_function, font = ("Calibri", 200,'bold'))
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.mainloop()
    
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        

    def button_function(self):
        self.clear_screen()

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    App()

if __name__ == "__main__":
    main()