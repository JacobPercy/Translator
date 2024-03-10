from text_to_speech import save
from langdetect import detect
import pyglet

text = "Hallo, wie geht es dir an diesem schönen Abend?"
language = detect(text)
print(language)


output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)

sound = pyglet.media.load("output.mp3")
sound.play()
pyglet.app.run()
