import speech_recognition as sr

# Criar um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as fonte:
    while True:
        audio = r.listen(fonte)  # Define o microfone como fonte de audio
        print(r.recognize_google(audio, language="pt-br"))
