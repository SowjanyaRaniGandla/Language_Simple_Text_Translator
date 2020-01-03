from googletrans import Translator

text=input("enter name here...")
trans_lang=input("enter translation language")
dest=trans_lang.capitalize()
#print(dest)


languages={
    'Telugu' : 'te',
    'Japanese' : 'ja',
    'Russian' : 'ru',
    'Italian' : 'it',
    'Latin' : 'la',
    'Hindi' : 'hi',
    'Arabic' : 'ar',
    'Greek' : 'el',
    'KOrean' : 'ko',
    'Urdu' : 'ur'

}
output_lang=languages[dest]
translator=Translator()

#for key,value in languages.items() :
print(translator.translate(text,dest=output_lang).text)
print(translator.detect(text))

