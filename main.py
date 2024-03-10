import customtkinter as ctk
import translators as ts
import pyperclip as pc
from text_to_speech import save
from langdetect import detect
import pyglet
from mutagen.mp3 import MP3
import os


class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.attributes("-fullscreen", True)

        self.width_1 = self.winfo_screenwidth()
        self.height_1 = self.winfo_screenheight()

        self.window_title = ctk.CTkLabel(self,text="Translator",font = ("Calibri", int(0.25 * self.height_1)))
        self.window_title.pack(pady=20)
        button = ctk.CTkButton(master=self, 
                               text="LAUNCH", 
                               height=int(.25 * self.height_1), 
                               width=int(.25 * self.width_1), 
                               corner_radius=25,
                               command=self.launch_function, 
                               font = ("Calibri", int(0.25 * self.height_1),'bold'))
        button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
        self.close_button()
    
    def close_button(self):
        self.close = ctk.CTkButton(master=self, 
                               text="X", 
                               height=15, 
                               width=20, 
                               command=self.destroy, 
                               font = ("Calibri", 15,'bold'))
        self.close.place(relx=0.985, rely=0.03, anchor=ctk.CENTER)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def translate(self, entry, output_text, to_language_str):
        input_text = entry.get()

        translated_result = ts.translate_text(input_text, 
                                              translator="google", 
                                              from_language="auto", 
                                              to_language=to_language_str)
        output_text.set(translated_result)

    def swap_boxes(self):
        temp = self.input_text.get()
        self.input_text.set(self.output_text.get())
        self.output_text.set(temp)

    def play_audio(self,str):
        save(text=str, lang=detect(str), file="output.mp3")

        audio = MP3("output.mp3")
        dur = audio.info.length
        sound = pyglet.media.load("output.mp3")
        sound.play()
        pyglet.app.event_loop.sleep(dur)
        os.remove("output.mp3")

    def launch_function(self):
        self.clear_screen()
        self.close_button()

        self.width_1 = self.winfo_screenwidth()
        self.height_1 = self.winfo_screenheight()

        #Top box (input)
        self.input_text = ctk.StringVar()
        self.entry = ctk.CTkEntry(master=self,
                               placeholder_text="Type text to be translated",
                               textvariable=self.input_text,
                               width=int(0.75 * self.width_1),
                               height=int(0.25 * self.height_1),
                               border_width=10,
                               corner_radius=10,
                               font=("Calibri",30))
        self.entry.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.entry.bind("<Return>", lambda event: self.translate(self.entry,
                                                                 self.output_text,
                                                                 self.to_lang.get()))

        #Box with language input
        self.to_lang = ctk.CTkEntry(master=self,
                                    placeholder_text='Enter a language to translate to (example: "es")',
                                    width=500,
                                    height=40,
                                    border_width = 2,
                                    corner_radius=5,
                                    font=("Calibri",20))
        self.to_lang.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        self.to_lang.bind("<Return>",lambda event: self.translate(self.entry,
                                                                  self.output_text,
                                                                  self.to_lang.get()))

        #Bottom box (output)
        self.output_text = ctk.StringVar()
        self.output_text.set("Output")
        self.output_box = ctk.CTkEntry(master=self,
                                       textvariable=self.output_text, 
                                       width=int(0.75 * self.width_1), 
                                       height=int(0.25 * self.height_1),
                                       border_width=10,
                                       corner_radius=10,
                                       font=("Calibri",30))
        self.output_box.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        #Swap fields button
        self.swapper = ctk.CTkButton(master=self, 
                               text="Swap text", 
                               height=10, 
                               width=10, 
                               command=self.swap_boxes, 
                               font = ("Calibri", int(0.05 * self.height_1),'bold'))
        self.swapper.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)

        #Translate button
        self.translate_button = ctk.CTkButton(master=self, 
                               text="Translate", 
                               height=10, 
                               width=10, 
                               command=lambda: self.translate(self.entry,
                                                              self.output_text,
                                                              self.to_lang.get()), 
                               font = ("Calibri", int(0.05 * self.height_1),'bold'))
        self.translate_button.place(relx=0.2, rely=0.5, anchor=ctk.CENTER)

        #Copy buttons
        self.copy_1 = ctk.CTkButton(master=self, 
                               text="Copy", 
                               height=10, 
                               width=10, 
                               command=lambda: pc.copy(self.input_text.get()))
        self.copy_1.place(relx=0.1, rely=0.2, anchor=ctk.CENTER)

        self.copy_2 = ctk.CTkButton(master=self, 
                               text="Copy", 
                               height=10, 
                               width=10, 
                               command=lambda: pc.copy(self.output_text.get()))
        self.copy_2.place(relx=0.1, rely=0.8, anchor=ctk.CENTER)

        #Audio player buttons
        self.audio_1 = ctk.CTkButton(master=self, 
                               text="Play", 
                               height=10, 
                               width=10, 
                               command=lambda: self.play_audio(self.input_text.get()))
        self.audio_1.place(relx=0.9, rely=0.2, anchor=ctk.CENTER)

        self.audio_2 = ctk.CTkButton(master=self, 
                               text="Play", 
                               height=10, 
                               width=10, 
                               command=lambda: self.play_audio(self.output_text.get()))
        self.audio_2.place(relx=0.9, rely=0.8, anchor=ctk.CENTER)
                                      

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()