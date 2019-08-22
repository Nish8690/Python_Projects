#Speech to Text
import speech_recognition as sr
 
r = sr.Recognizer()

with sr.Microphone() as source:
     print("speek anything : ")
     audio = r.listen(source)

try:
        text = r.recognize_google(audio)

        fptr = open('C:/Users/11010853.SRHK/PycharmProjects/temp/test.txt', 'w+')

        fptr.write(str(text) + '\n')

        fptr.close()

        print(f'you said : {text}')
except:
        print("Try Again")