#Organizador de Arquivos com Base numa extensão
import os
import shutil

origem = '/home/ackio/Downloads/'
destino = '/home/ackio/Documentos/Projects ACK/Python/Arquivos/'
extensao = '.csv'

lista_arquivos = os.listdir(origem)

for Arquivo in lista_arquivos:
    if extensao in Arquivo:
        origem_comp = origem + Arquivo
        destino_comp = destino + Arquivo
        shutil.move(origem_comp, destino_comp)


