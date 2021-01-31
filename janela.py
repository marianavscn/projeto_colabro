import pygame
import funcoes as f

pygame.init()                                                   # inicia o pygame

janela = pygame.display.set_mode((800, 600))                    # criando janela

pygame.display.set_caption("PROJETO COLABRO")                   # nome da janela

f.printar_imagem('logo_colabro.jpg', janela)                    # mostra a 1a tela: a logo

fundo_timer = pygame.image.load('imagens/fundo_timer.png')      # carrega o fundo do timer

font = pygame.font.Font(None, 40)                               # define a fonte do contador
purple = pygame.Color((138, 66, 137))                           # e a cor
relogio = pygame.time.Clock()                                   # armazena o tempo
contador_fps = 0                                                # inicia o cont de FPS
dt = 0                                                          # Delta time - conta as ticks

janela_aberta = True                                            # controla quando a janela fica aberta

# variaveis auxiliares que permitem a execucao sequencial, sem antecipar eventos
abertura = True
labirinto = False
escolha = False
reiniciar = False
controle, guarda_evento, ponto = 0, 0, 0
decisao = ''

while janela_aberta:                                            # inicio do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False                               # fecha a janela

    # controla o contador
    contador_fps += dt                                          # incrementa o cont
    txt = font.render(str(round(contador_fps)), True, purple)   # printa o timer
    if labirinto:
        janela.blit(fundo_timer, (5, 5))                        # adiciona um fundo para o timer
        janela.blit(txt, (25, 22))                              # printa o timer na tela
    dt = relogio.tick(30) / 1000                                # controla o FPS
    cont_segundos = f.retira_decimais(contador_fps)             # transforma o cont_fps em cont_seg

    if abertura:
        teclas = pygame.key.get_pressed()                       # armazena teclas pressionadas
        if (cont_segundos == 2) and abertura:
            f.printar_imagem('inicia_espaco.jpg', janela)       # executa a funcao q carrega a img e printa
            controle = 1                                        # torna possivel a entrada no prox IF

        if (teclas[pygame.K_SPACE]) and (controle == 1):
            f.printar_imagem('use_fones.jpg', janela)
            guarda_evento = cont_segundos                       # armazena o momento que essa condicao aconteceu
            controle = 2                                        # torna possivel a entrada no prox IF

        if (cont_segundos == (guarda_evento + 4)) and (controle == 2):
            f.printar_imagem('comandos.jpg', janela)            # essa cond. é baseada na execucao da anterior + 4seg
            guarda_evento = cont_segundos
            controle = 3

        if (cont_segundos == (guarda_evento + 4)) and (controle == 3):
            f.printar_imagem('abertura.png', janela)
            f.rodar_audio('audios/Audio1.1.mp3')                # audio de abertura
            guarda_evento = cont_segundos
            controle = 4

        if (cont_segundos == (guarda_evento + 5)) and (controle == 4):  # 15s
            f.printar_imagem('explicacao.jpg', janela)
            f.rodar_audio('audios/Audio1.2.mp3')                # audio da explicacao
            guarda_evento = cont_segundos
            controle = 5

        if cont_segundos == (guarda_evento + 6) and (controle == 5):  # 62s
            controle = 10
            abertura = False                                    # faz com que o bloco 'abertura' execute apenas 1x
            labirinto = True                                    # possibilita a execucao do bloco labirinto

    if labirinto:
        if (cont_segundos == (guarda_evento + 6)) and (controle == 10):  # 62s
            contador_fps = 0                                    # zera o contador qd entra no labirinto
            f.printar_imagem('ponto1_labirinto01.png', janela)
            f.rodar_audio('audios/Audio3.mp3')                  # audio: seguir norte
            controle = 20

        if reiniciar:                                           # executa quando dá game over
            f.printar_imagem('ponto1_labirinto01.png', janela)
            f.rodar_audio('audios/Audio3.mp3')                  # audio: seguir norte
            ponto = 0
            reiniciar = False

        if cont_segundos == 15 and ponto != 50:                 # avisa que a água está subindo
            f.rodar_audio('audios/Audio15.mp3')                 # nos joelhos
            guarda_evento = cont_segundos

        if cont_segundos == 40 and ponto != 50:                 # avisa que a água está subindo
            f.rodar_audio('audios/Audio18.mp3')                 # cada vez mais

        if cont_segundos == 60 and ponto != 50:                 # morrendo afogado
            f.printar_imagem('gameover.png', janela)
            f.rodar_audio('audios/Audio16.mp3')                 # tempo esgotado
            ponto = 50

        for event in pygame.key.get_pressed():                  # para cada tecla apertada
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_v]:                            # permite voltar ao inicio pressionando V
                reiniciar = True

            if comandos[pygame.K_w] and ponto == 0:             # user no ponto 1 -> ponto 2
                f.printar_imagem('ponto2_labirinto01.png', janela)
                f.rodar_audio('audios/Audio4.mp3')              # audio: seguir LESTE ou OESTE
                ponto += 1

            if comandos[pygame.K_a] and ponto == 1:             # user no ponto 2 -> ponto 3
                f.printar_imagem('ponto3_labirinto01.png', janela)
                f.rodar_audio('audios/Audio5.mp3')              # audio: seguir SUL
                ponto += 1

            if comandos[pygame.K_s] and ponto == 2:             # user no ponto 3 -> ponto 4
                f.printar_imagem('ponto4_labirinto01.png', janela)
                f.rodar_audio('audios/Audio8.mp3')              # seguir OESTE
                ponto = 3

            if comandos[pygame.K_a] and ponto == 3:             # user no ponto 4 -> reiniciar
                f.printar_imagem('gameover.png', janela)
                f.rodar_audio('audios/Audio10.mp3')             # audio: beco sem saída
                ponto = 50

            if comandos[pygame.K_d] and ponto == 1:             # user no ponto 2 -> ponto 5
                f.printar_imagem('ponto5_labirinto01.png', janela)
                f.rodar_audio('audios/Audio9.mp3')              # audio: seguir NORTE ou SUL
                ponto = 21

            if comandos[pygame.K_w] and ponto == 21:            # user no ponto 5 -> ponto 7
                f.printar_imagem('ponto7_labirinto01.png', janela)
                f.rodar_audio('audios/Audio8.mp3')              # audio: seguir OESTE
                ponto = 22

            if comandos[pygame.K_s] and ponto == 21:            # user no ponto 5 -> ponto 6
                f.printar_imagem('ponto6_labirinto01.png', janela)
                f.rodar_audio('audios/Audio8.mp3')              # audio: seguir OESTE
                ponto = 24

            if comandos[pygame.K_a] and ponto == 24:            # user no ponto 6 -> ponto 9
                f.printar_imagem('ponto9_labirinto01.png', janela)
                f.rodar_audio('audios/Audio5.mp3')              # audio: seguir SUL
                ponto = 25

            if comandos[pygame.K_s] and ponto == 25:            # user no ponto 9 -> reiniciar
                f.printar_imagem('gameover.png', janela)
                f.rodar_audio('audios/Audio10.mp3')             # audio: beco sem saída
                ponto = 50

            if comandos[pygame.K_a] and ponto == 22:            # user no ponto 7 -> ponto 8
                f.printar_imagem('ponto8_labirinto01.png', janela)
                f.rodar_audio('audios/Audio6.mp3')              # audio: seguir NORTE
                ponto = 23

            if comandos[pygame.K_w] and ponto == 23:            # user no ponto 8 -> SAIR DO LABIRINTO
                f.printar_imagem('ganhou.png', janela)
                labirinto = False
                escolha = True
                ponto = 100

            if comandos[pygame.K_SPACE] and ponto == 50:        # quando perde, ao apertar 'espaco'
                contador_fps = 0
                reiniciar = True                                # entra no bloco 'if reiniciar'

    if escolha:
        if ponto == 100:                                        # se ganhou, aparece a imagem e o audio
            ponto = 101
            f.printar_imagem('ganhou.png', janela)
            f.rodar_audio('audios/Audio19.mp3')
            guarda_evento = cont_segundos

        if cont_segundos == (guarda_evento + 15) and (ponto == 101):
            f.printar_imagem('pilulas.png', janela)             # escolha das pilulas
            ponto = 200

        comandos2 = pygame.key.get_pressed()  # escolha pilulas
        if comandos2[pygame.K_d]:                               # escolhe a vermelha
            f.printar_imagem('pilula_vermelha.png', janela)
            decisao = 'd'

        if comandos2[pygame.K_a]:                               # escolhe a azul
            f.printar_imagem('pilula_azul.png', janela)
            decisao = 'e'

        if comandos2[pygame.K_RETURN] and decisao == 'd':
            f.printar_imagem('escolha_vermelha.png', janela)    # roda o audio da escolha vermelha
            f.rodar_audio('audios/Audiofinal.mp3')              # 78s

        if comandos2[pygame.K_RETURN] and decisao == 'e':       # se essa cond foi executada, o player volta ao
            ponto = 0                                           # ponto incial do labirinto
            contador_fps = 0
            escolha = False
            labirinto = True
            reiniciar = True

    pygame.display.update()

pygame.quit()
