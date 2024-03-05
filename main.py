import customtkinter as ctk
import translators as ts

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        self.window_title = ctk.CTkLabel(self,text="Translator",font = ("Calibri", 500))
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, text="LAUNCH", height=200,width=800,command=self.launch_function, font = ("Calibri", 200,'bold'))
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def translate(self, entry, output_text):
        input_text = entry.get()
        translated = ts.translate_text(input_text, translator="google", from_lang="auto", to_lang="en")
        output_text.set(translated)
        
        print(translated)

    def handle_wait(self, output_text, event=None):
        # Cancel the previous waiting if any
        if hasattr(self, 'after_id'):
            self.entry.after_cancel(self.after_id)

        # Schedule the translation after 1000 milliseconds (1 second)
        self.after_id = self.entry.after(1000, self.translate, self.entry)

    def launch_function(self):
        self.clear_screen()
        self.entry = ctk.CTkEntry(master=self,
                               placeholder_text="Type text to be translated",
                               width=1000,
                               height=200,
                               border_width=10,
                               corner_radius=10,
                               font=("Calibri",100,"bold"))
        self.entry.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.entry.bind("<Return>", lambda event: self.translate(self.entry,output_text))
        self.entry.bind("<KeyRelease>", self.handle_wait)


        output_text = ctk.StringVar()
        output_text.set("Type text to be translated")
        self.output_box = ctk.CTkEntry(master=self,
                                       textvariable=output_text, 
                                       width=1000, 
                                       height=200,
                                       border_width=10,
                                       corner_radius=10,
                                       font=("Calibri",100,"bold"))
        self.output_box.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
        self.output_box.configure(state="disabled")

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
