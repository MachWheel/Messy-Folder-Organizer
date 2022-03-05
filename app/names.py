# coding=utf-8
from datetime import datetime


def mes_ano():
    data = datetime.now()
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    mes = data.month - 1  # INDICE DO MES
    return meses[mes] + " " + str(data.year)


log_name = (f"Movidos em "
            f"{datetime.now().strftime('%d_%m_%Y às %H-%M')}")
