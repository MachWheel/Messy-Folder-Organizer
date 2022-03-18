# coding=utf-8
from resources.names import MES_ANO


def CONFIRM(working_folder):
    return (f"Os arquivos da pasta:"
            f"\n'{working_folder}'\n"
            f"Serão organizados de acordo "
            f"com os seus tipos.\n\n"
            f"DESEJA CONTINUAR?")


def MOVED(f):
    return f"\n[#] ARQUIVO '{f.file_name}{f.file_extension}' MOVIDO PARA: '{f.category_name}'\n"


def IGNORED(f):
    return f"\n[!] ARQUIVO '{f.file_name}{f.file_extension}' IGNORADO."


def DESTINATION(folder):
    return f"\n[!] OS ARQUIVOS SERÃO MOVIDOS PARA:\n'{folder}'\n"


def EXISTING(folder):
    return f"\n[!] UTILIZANDO PASTA EXISTENTE:\n'{folder}'\n"


def CREATED(folder):
    return f"\n[#] PASTA '{folder}' CRIADA.\n"


def WORKING(folder):
    return f"\n[#] TRABALHANDO NA PASTA:\n'{folder}'\n"


def DRAWN(view):
    return f"\nJANELA DESENHADA: {view}\n"


APP_TITLE = 'Organizador'

FACTORY = '\nCRIANDO APLICAÇÃO...\n'

STARTED = '\nAPLICAÇÃO INICIALIZADA.\n'

SELECT_FOLDER = 'Escolha uma pasta bagunçada para organizar:'

DONE = (f"ARQUIVOS ORGANIZADOS!\n"
        f"PRESSIONE OK PARA ABRIR"
        f"A PASTA CRIADA")

EXTS_LOADED = "\nEXTENSÕES CARREGADAS.\n"

CANCELLED = "\nOPERAÇÃO ABORTADA.\n"

CONFIRMED = "\nOPERAÇÃO CONFIRMADA.\n"

FINISHED = '\nOPERAÇÃO FINALIZADA.\n'

SUBDIR_CHECK = f'Organizar arquivos na subpasta "{MES_ANO()}"'

SUBDIR_CHECK_TOOLTIP = "Se desmarcado, os arquivos serão organizados dentro da própria pasta escolhida."
