def CONFIRM(working_folder):
    return (f"Os arquivos da pasta:"
            f"\n'{working_folder}'\n"
            f"Serão organizados de acordo "
            f"com os seus tipos.\n\n"
            f"DESEJA CONTINUAR?")


def MOVED(file, destination):
    return f"\n[#] {file}\nMOVIDO PARA: {destination}\n"


def IGNORED(file):
    return f"\n[!] {file}\nFOI IGNORADO, IMPOSSIVEL MOVER."


def DEST_FOLDER(folder, created):
    if created:
        return (f"\nPasta '{folder}' criada.\n"
                f"Movendo arquivos para ela...\n\n")
    else:
        return f"Movendo arquivos para '{folder}'..."


APP_TITLE = 'Organizador'

SELECT_FOLDER = 'Selecione uma pasta para organizar: '

DONE = (f"ARQUIVOS ORGANIZADOS!\n"
        f"PRESSIONE OK PARA ABRIR"
        f"A PASTA CRIADA")

CANCELLED = "CANCELANDO: Operação abortada."
