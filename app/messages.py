def MSG_CONFIRM(working_folder):
    return (f"Os arquivos da pasta:"
            f"\n'{working_folder}'\n"
            f"Serão organizados de acordo "
            f"com os seus tipos.\n\n"
            f"DESEJA CONTINUAR?")


def MSG_MOVED(file, destination):
    return f"\n[#] {file}\nMOVIDO PARA: {destination}\n"


def MSG_IGNORED(file):
    return f"\n[!] {file}\nFOI IGNORADO, IMPOSSIVEL MOVER."


def MSG_CREATED(folder):
    return (f"\nPasta '{folder}' criada.\n"
            f"Movendo arquivos para ela...\n\n")

