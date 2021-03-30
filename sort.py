import os
import glob
import shutil
import datetime
from os import path

nomeDoApp = os.path.basename(os.path.realpath(__file__))
nomeDoApp = os.path.splitext(nomeDoApp)[0]

# DATA DE HOJE:
data = datetime.datetime.now() 
meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho',
       'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
# INDICE DO MES ATUAL:
mes = data.month-1 

# NOME DA PASTA DE TRABALHO A SER CRIADA: 
pastaOrganizada = './'+meses[mes]+" "+str(data.year) 
# [ex: "Abril 2021"]

nomeDoLog = "Movidos em "+data.strftime('%d_%m_%Y às %H-%M')+'.txt'
logArquivo = open(nomeDoLog,'a')
logArquivo.close()

# SELECIONA TODOS OS ARQUIVOS DO DIRETÓRIO ATUAL
arquivosBaguncados=glob.glob("./*")

# TIPOS DE ARQUIVOS A SEREM DETECTADOS:
documentos=['.doc','.docx','.htm','.odt','.pdf','.xls','xlsx','.ods','.ppt','.pptx','.txt'] # OK
imagens=['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'] # OK
videos=['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'] # OK
audios=['.aif','.cda','.mid','.mp3','.mpa','.ogg','.wav','.wma','.wpl'] # OK
programas=['.apk','.bat','.bin','.cgi','.pl','.com','.exe','.gadget','.jar','.msi','.py','.wsf'] # OK
compactados=['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip','.iso'] # OK
arquivos=['.apk', '.torrent', '.bnp', '.h2w', '.php', '.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ini','.sys','.tmp','.download','.css','.webp','.html']

# PASTAS CUJOS ARQUIVOS SERÃO MOVIDOS:

pastaDocumentos = pastaOrganizada + '/Documentos'
pastaImagens = pastaOrganizada + '/Imagens'
pastaVideos = pastaOrganizada + '/Vídeos'
pastaAudios = pastaOrganizada + '/Áudios'
pastaProgramas = pastaOrganizada + '/Programas'
pastaCompactados = pastaOrganizada + '/Compactados'
pastaArquivos = pastaOrganizada + '/Outros'

# FAVOR OBEDECER A ORDEM DOS TIPOS DE ARQUIVOS / PASTAS, RESPECTIVAMENTE !!!
listaTipos = [documentos, imagens, videos, audios, programas, compactados, arquivos]
listaPastas = [pastaDocumentos, pastaImagens, pastaVideos, pastaAudios, pastaProgramas, pastaCompactados, pastaArquivos]

try:
    input ("\n\nOs arquivos da pasta: '" + os.getcwd() + "'\nSerão magicamente organizados de acordo com os seus tipos.\n\nPressione Enter para continuar ou CTRL-C para abortar.\n")
except KeyboardInterrupt:
    print("\nArregou.")
    exit (0)

# TENTE CRIAR A PASTA DE TRABALHO:
try:
    os.mkdir(pastaOrganizada)
    print("\n"+pastaOrganizada+" foi criada! Movendo arquivos para la...")
except FileExistsError:    
    print("\n"+pastaOrganizada+" ja existe. Movendo arquivos para la...")

for arquivo in arquivosBaguncados:
    
    nomeArquivo = os.path.basename(arquivo)
    extensaoArquivo = os.path.splitext(arquivo)[1]
    
    posicaoAtual = 0
    posicaoFinal = len(listaTipos)
    while (posicaoAtual < posicaoFinal):
        
        if extensaoArquivo in listaTipos[posicaoAtual]: # COMPARA A EXTENSÃO DO ARQUIVO COM OS TIPOS NA LISTA
            pastaSelecionada = listaPastas[posicaoAtual]

            # TENTAR CRIAR A PASTA ATUALMENTE SELECIONADA:
            try:
                os.mkdir(pastaSelecionada) 
            except FileExistsError:
                pass

            if (os.path.splitext(nomeArquivo)[0] != nomeDoApp) and (nomeArquivo != nomeDoLog): 
                try:
                    shutil.move(arquivo,pastaSelecionada) # MOVE O ARQUIVO PRA ELA
                except:
                    print("\nO arquivo ["+arquivo+"] já existe no destino e foi ignorado.")
                    
                nomeDaPastaSelecionada = os.path.basename(pastaSelecionada)
                mensagem = "\n"+nomeDaPastaSelecionada+" <=== "+arquivo # DIZ QUAL ARQUIVO FOI MOVIDO PRA ONDE
                print(mensagem)
                
                logArquivo = open(nomeDoLog,'a')
                logArquivo.write(mensagem)
                logArquivo.close()
        posicaoAtual+=1
        
logArquivo = open(nomeDoLog,'a')
logArquivo.write('\n\n\t— "Todo sofrimento possui um pouco de prazer."')
logArquivo.close()
        
try:
    input ("\n\n============== PRONTO! TUDO ARRUMADINHO! ==============\n\nPressione qualquer tecla para finalizar o programa.\n")
except KeyboardInterrupt:
    pass