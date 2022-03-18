# coding=utf-8
from datetime import datetime


def MES_ANO():
    data = datetime.now()
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    mes = data.month - 1  # INDICE DO MES
    return meses[mes] + " " + str(data.year)


LOG_NAME = (f"Registro "
            f"{datetime.now().strftime('%d_%m_%Y às %H-%M')}.log")

THEME = "DarkBlue"

IGNORED_CATEGORY = "Ignorados"
