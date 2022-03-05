import glob
from .names import mes_ano


# SELECIONAR TODOS OS ARQUIVOS DO DIRETÓRIO ATUAL
arquivosBaguncados = glob.glob("./*")

pastaOrganizada = './' + mes_ano()  # [ex: "Abril 2021"]

# PASTAS CUJOS ARQUIVOS SERÃO MOVIDOS:
pastaDocumentos = pastaOrganizada + '/Documentos'
pastaImagens = pastaOrganizada + '/Imagens'
pastaVideos = pastaOrganizada + '/Vídeos'
pastaAudios = pastaOrganizada + '/Áudios'
pastaProgramas = pastaOrganizada + '/Programas'
pastaCompactados = pastaOrganizada + '/Compactados'
pastaArquivos = pastaOrganizada + '/Outros'

listaPastas = [pastaDocumentos, pastaImagens, pastaVideos,
               pastaAudios, pastaProgramas, pastaCompactados,
               pastaArquivos]
