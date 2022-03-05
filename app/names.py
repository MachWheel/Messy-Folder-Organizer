from os import path
from datetime import datetime


def mes_ano():
    data = datetime.now()
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    mes = data.month - 1  # INDICE DO MES
    return meses[mes] + " " + str(data.year)


def is_application(file_name) -> bool:
    app_path = path.basename(path.realpath(__file__))
    app_name = path.splitext(app_path)[0]
    print(f"APP_NAME: {app_name}")  # ################
    return path.splitext(file_name)[0] == app_name


def is_log(file_name) -> bool:
    return path.splitext(file_name)[0] == log_name


log_name = (f"Movidos em "
            f"{datetime.now().strftime('%d_%m_%Y às %H-%M')}")
