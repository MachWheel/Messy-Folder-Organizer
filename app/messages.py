# coding=utf-8
from .filter import Filter


def CONFIRM(working_folder):
    return (f"Os arquivos da pasta:"
            f"\n'{working_folder}'\n"
            f"Serão organizados de acordo "
            f"com os seus tipos.\n\n"
            f"DESEJA CONTINUAR?")


def MOVED(f: Filter):
    return f"\n[#] ARQUIVO '{f.file_name}{f.file_extension}' MOVIDO PARA: '{f.category_name}'\n"


def IGNORED(f: Filter):
    return f"\n[!] ARQUIVO '{f.file_name}{f.file_extension}' IGNORADO."


def DESTINATION(folder):
    return f"\n[!] OS ARQUIVOS SERÃO MOVIDOS PARA:\n'{folder}'\n"


def CREATED(folder):
    return f"\n[#] PASTA '{folder}' CRIADA.\n"


APP_TITLE = 'Organizador'

SELECT_FOLDER = 'Selecione uma pasta para organizar: '

DONE = (f"ARQUIVOS ORGANIZADOS!\n"
        f"PRESSIONE OK PARA ABRIR"
        f"A PASTA CRIADA")

CANCELLED = "CANCELANDO: Operação abortada."
