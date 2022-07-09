import translators as ts

text = 'Subscribe for more!'

languages = ['hr', 'it', 'fr', 'es', 'ja', 'ru', 'el']

for language in languages:
    translation = ts.google(text, 'en', language)
    print(translation)