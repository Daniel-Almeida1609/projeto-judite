import speech_recognition as sr
import pyttsx3 as psx
import json
import classe


def reconhecedor_voz():
    # Criar um reconhecedor
    r = sr.Recognizer()
    mf = sr.Microphone()

    # Verificando as instancias
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` deve ser uma instancia `Recognizer`")

    if not isinstance(mf, sr.Microphone):
        raise TypeError("`microfone` deve ser uma instancia `Microfone`")

    # Abrir o microfone para captura
    with mf as fonte:
        r.adjust_for_ambient_noise(fonte, duration=0.5)
        audio = r.listen(fonte)  # Define o microfone como fonte de audio

    resposta = {"sucesso": True, "erro": None, "transcricao": None}

    try:
        # tratando a lista de dicionarios
        fala = r.recognize_google(audio, language="pt-br", show_all=True)
        print(fala)
        dic_fala = fala["alternative"][0]
        resposta["transcricao"] = dic_fala["transcript"].lower()
    except sr.RequestError:
        resposta["sucesso"] = False
        resposta["erro"] = "API falhou"
    except sr.UnknownValueError:
        resposta["erro"] = "Não foi reconhecida nenhuma palavra"

    return resposta


def reconhecedor_texto(texto):
    engine = psx.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices)
    engine.say(texto)
    engine.runAndWait()


if __name__ == "__main__":
    texto = reconhecedor_voz()
    print(texto)
    if (texto["transcricao"] == "que horas são" or texto["transcricao"] == "me diga as horas"):
        frase_falada = classe.SystemInfo.pega_hora()
    if (texto["transcricao"] == 'qual o seu nome' or texto["transcricao"] == 'me diga o seu nome'):
        frase_falada = classe.SystemInfo.meu_nome()
    
    reconhecedor_texto(frase_falada)
