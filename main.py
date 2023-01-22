import speech_recognition as sr
import pyttsx3 as psx


def reconhecedor_voz():
    # Criar um reconhecedor
    r = sr.Recognizer()
    mf = sr.Microphone()

    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` deve ser uma instancia `Recognizer`")

    if not isinstance(mf, sr.Microphone):
        raise TypeError("`microfone` deve ser uma instancia `Microfone`")

    # Abrir o microfone para captura
    with mf as fonte:
        r.adjust_for_ambient_noise(fonte, duration=0.5)
        audio = r.listen(fonte)  # Define o microfone como fonte de audio

    try:
        fala = r.recognize_google(audio, language="pt-br")
    except sr.RequestError:
        print("API falhou")
    except sr.UnknownValueError:
        print("Não foi reconhecida nenhuma palavra")

    return fala


def reconhecedor_texto(texto):
    engine = psx.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(texto)
    engine.runAndWait()


if __name__ == "__main__":
    texto = reconhecedor_voz()
    reconhecedor_texto(texto)
