import translators as ts

input = "this thing"
lang = "el"
print(ts.translate_text(input,translator="google",from_language = "auto",to_language = lang))

translated_result = ts.translate_text("hello", translator="google", from_lang="auto", to_lang="el")