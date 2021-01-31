import os
import pygame


def printar_imagem(caminho, janela):
    local = os.path.join("imagens", caminho)
    try:
        imagem = pygame.image.load(local)
    except pygame.error:
        print("Imagem não foi encontrada ", local)
        raise SystemExit
    aparecer_img = janela.blit(imagem, (0, 0))
    return aparecer_img


def retira_decimais(num):
    num = float(num)
    lista_num = str(num).split('.')
    lista_decimais = str(lista_num[1])
    lista_str = []
    for i in lista_decimais:
        lista_str.append(i)
    parte_inteiro = lista_num[0]
    parte_decimal = lista_str[0]
    numero_final = parte_inteiro + '.' + parte_decimal
    return float(numero_final)


def rodar_audio(som):
    pygame.mixer.init()             # Inicia o módulo
    pygame.mixer.music.load(som)    # Carrega a música
    pygame.mixer.music.play()       # Toca a música
