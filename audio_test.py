from text_to_speech import save
from langdetect import detect
import pyglet
from mutagen.mp3 import MP3



text = "Hallo, wie geht es dir an diesem schönen Abend?"
language = detect(text)
print(language)


output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)

audio = MP3("output.mp3")
value = audio.info.length
print(value)



pyglet.app.event_loop.sleep(value)
