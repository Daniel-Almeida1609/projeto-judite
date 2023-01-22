import datetime


class SystemInfo:
    def __init__(self) -> None:
        pass

    def pega_hora():
        agora = datetime.datetime.now()
        resposta = "São {} horas e {} minutos.".format(agora.hour, agora.minute)
        return resposta
    def meu_nome():
        nome = 'Judite'
        resposta = "Meu nome é {}.".format(nome)
        return resposta