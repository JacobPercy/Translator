import customtkinter as ctk
import translators as ts

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        width_1 = self.winfo_screenwidth()
        height_1 = self.winfo_screenheight()

        print(width_1)
        print(height_1)

        self.window_title = ctk.CTkLabel(self,text="Translator",font = ("Calibri", int(0.25 * height_1)))
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, 
                               text="LAUNCH", 
                               height=int(.25 * height_1), 
                               width=int(.25 * width_1), 
                               command=self.launch_function, 
                               font = ("Calibri", int(0.25 * height_1),'bold'))
        button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def translate(self, entry, output_text, to_language_str):
        input_text = entry.get()
        print(to_language_str)

        translated_result = ts.translate_text(input_text, 
                                              translator="google", 
                                              from_language="auto", 
                                              to_language=to_language_str)
        output_text.set(translated_result)
        
        print(translated_result)

    def swap_boxes(self):
        print("button pressed")
        temp = self.input_text.get()
        self.input_text.set(self.output_text.get())
        self.output_text.set(temp)

    def launch_function(self):
        self.clear_screen()

        width_1 = self.winfo_screenwidth()
        height_1 = self.winfo_screenheight()

        #Top box (input)
        self.input_text = ctk.StringVar()
        self.entry = ctk.CTkEntry(master=self,
                               placeholder_text="Type text to be translated",
                               textvariable=self.input_text,

                               width=int(0.75 * width_1),
                               height=int(0.25 * height_1),
                               border_width=10,
                               corner_radius=10,
                               font=("Calibri",100,"bold"))
        self.entry.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.entry.bind("<Return>", lambda event: self.translate(self.entry,self.output_text,self.to_lang.get()))

        #Bottom box (output)
        self.output_text = ctk.StringVar()
        self.output_text.set("Type text to be translated")
        self.output_box = ctk.CTkEntry(master=self,
                                       textvariable=self.output_text, 
                                       width=int(0.75 * width_1), 
                                       height=int(0.25 * height_1),
                                       border_width=10,
                                       corner_radius=10,
                                       font=("Calibri",30))
        self.output_box.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
        #self.output_box.configure(state="disabled")


        self.to_lang = ctk.CTkEntry(master=self,
                                    placeholder_text="type language to translate to",
                                    width=500,
                                    height=40,
                                    border_width = 2,
                                    corner_radius=2,
                                    font=("Calibri",20))
        self.to_lang.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        self.to_lang.bind("<Return>",lambda event: self.translate(self.entry,
                                                                  self.output_text,
                                                                  self.to_lang.get()))


        self.swapper = ctk.CTkButton(master=self, 
                               text="Swap text", 
                               height=1, 
                               width=1, 
                               command=self.swap_boxes, 
                               font = ("Calibri", int(0.05 * height_1),'bold'))
        self.swapper.place(relx=0.2, rely=0.5, anchor=ctk.CENTER)
                                      

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
