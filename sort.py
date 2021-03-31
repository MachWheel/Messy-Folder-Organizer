import os
import glob
import shutil
import datetime
import sys
from os import path

# DATA DE HOJE:
data = datetime.datetime.now() 
meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho',
       'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
mes = data.month-1  # INDICE DO MES


# NOMES DAS COISAS:
nomeDoApp = os.path.basename(os.path.realpath(__file__))
nomeDoApp = os.path.splitext(nomeDoApp)[0]
nomeDoLog = "Movidos em "+data.strftime('%d_%m_%Y às %H-%M')+'.txt'
pastaOrganizada = './'+meses[mes]+" "+str(data.year) # [ex: "Abril 2021"]


# SELECIONAR TODOS OS ARQUIVOS DO DIRETÓRIO ATUAL
arquivosBaguncados = glob.glob("./*")


# TIPOS DE ARQUIVOS SUPORTADOS:
documentos=['.doc','.docx','.htm','.odt','.pdf','.xls','.xlsx','.xlsm','.ods','.ppt','.pptx','.txt','.mobi','.epub'] # OK
imagens=['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'] # OK
videos=['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.srt'] # OK
audios=['.aif','.cda','.mid','.mp3','.mpa','.ogg','.wav','.wma','.wpl'] # OK
programas=['.apk','.bat','.bin','.cgi','.pl','.com','.exe','.gadget','.jar','.msi','.py','.wsf'] # OK
compactados=['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip','.iso'] # OK
arquivos=['.apk', '.torrent', '.bnp', '.h2w', '.php', '.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ini','.sys','.tmp','.download','.css','.webp','.html','.xsl']


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

def logar(mensagem):
    logArquivo = open(nomeDoLog,'a')
    logArquivo.write(mensagem)
    print(mensagem)
    logArquivo.close()
    

try:
    input ("\n\nOs arquivos da pasta: '" + os.getcwd() + "'\nSerão magicamente organizados de acordo com os seus tipos.\n\nPressione Enter para continuar ou CTRL-C para abortar.\n")
except KeyboardInterrupt:
    print("\nArregou.")
    exit (0)

# TENTE CRIAR A PASTA DE TRABALHO:
try:
    os.mkdir(pastaOrganizada)
    logar("\n"+pastaOrganizada+" foi criada! Movendo arquivos para la...")
except FileExistsError:    
    logar("\n"+pastaOrganizada+" ja existe. Movendo arquivos para la...")

    
for arquivo in arquivosBaguncados:
    
    nomeArquivo = os.path.basename(arquivo)
    extensaoArquivo = str.lower(os.path.splitext(arquivo)[1])
    extensaoDetectada = False
    
    posicaoAtual = 0
    posicaoFinal = len(listaTipos)
    
    while (posicaoAtual < posicaoFinal):
        
        if extensaoArquivo in listaTipos[posicaoAtual]: # COMPARA A EXTENSÃO DO ARQUIVO COM OS TIPOS NA LISTA
            pastaSelecionada = listaPastas[posicaoAtual]
            extensaoDetectada = True


            if (os.path.splitext(nomeArquivo)[0] != nomeDoApp) and (nomeArquivo != nomeDoLog): 

                try: os.mkdir(pastaSelecionada) 
                except FileExistsError: pass
                
                try:
                    shutil.move(arquivo,pastaSelecionada) # MOVE O ARQUIVO PRA ELA
                    
                    nomeDaPastaSelecionada = os.path.basename(pastaSelecionada)
                    logar("\n"+nomeDaPastaSelecionada+" <=== ["+nomeArquivo+"]") # DIZ QUAL ARQUIVO FOI MOVIDO PRA ONDE
                    
                except shutil.Error as e:
                    logar("\n\n" + str(e))
                    logar("\nO ARQUIVO ["+nomeArquivo+"]\nFOI IGNORADO.")
                
        posicaoAtual+=1
        
    if not extensaoDetectada and extensaoArquivo and not (extensaoArquivo == '.lnk'): 
        logar("\n\nTipo não suportado: '"+extensaoArquivo+"' \nem ["+nomeArquivo+"]")     

logar('\n\n\t— "Todo sofrimento possui um pouco de prazer."')
        
try:
    input ("\n\n============== PRONTO! TUDO ARRUMADINHO! ==============\n\nPressione ENTER para finalizar o programa.\n")
except KeyboardInterrupt:
    pass