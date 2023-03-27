import pygame

res = w, h = 1080, 720
green = (0, 255, 0)
white = (0, 0, 0)

pygame.init() # This kicks things off. It initializes all the modules requigreen for PyGame.
done = False
screen = pygame.display.set_mode(res)
screen.fill((255, 255, 255))

# pygame.mixer - многоканальное аудио
# управлять звуками - pygame.mixer.Sound

snd1 = pygame.mixer.Sound("tsis7\snds\Like a G6 by Arukame Suzuya.mp3") # грузим треки
snd2 = pygame.mixer.Sound("tsis7\snds\Sunset by Blu Swing.mp3")
ml = [snd1, snd2] # грузим в (плей)лист :)

basicFont = pygame.font.SysFont(None, 38) # создаём шрифты
basicFont2 = pygame.font.SysFont(None, 33)
text1 = basicFont.render('Arukame Suzuya - Like a G6', True, 'black', 'white') # создаём текста
text2 = basicFont2.render('Blu Swing - Sunset', True, 'black', 'white')

screen.blit(text1, (142,130)) # отображаем текста на экране
screen.blit(text2, (150,260))

i = 0
sngnum = 0

while not done:
        if i == 0:
            pygame.draw.rect(screen, green, (90,95,417,105), 6) #x1, y1, x2, y2
            pygame.draw.rect(screen, white, (91,221,419,105), 6) # рисуем "боксы" с песнями из листа
        elif i == 1:
            pygame.draw.rect(screen, white, (90,95,417,105), 6)
            pygame.draw.rect(screen, green, (91,221,419,105), 6)

        pygame.draw.circle(screen, white, (180,576), 50, 5) # прошлый трек
        pygame.draw.lines(screen, white, True, [ [153,577] , [188,552], [188,602]], 3) 

        pygame.draw.circle(screen, white, (360,576), 50, 5) # пауза
        pygame.draw.line(screen, white, [342,552] , [342,595], 3)
        pygame.draw.line(screen, white, [377,552] , [377,595], 3)

        pygame.draw.circle(screen, white, (540,576), 50, 5) # следующий трек
        pygame.draw.lines(screen, white, True, [ [560,577] , [525,552], [525,602]], 3)
        for event in pygame.event.get():
            # for coordinates -> print(event)
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for a in range(-50, 51): # Цикл используем, чтобы мог находить нажатия по кругу как по X
                    for b in range(-50, 51): # так и по Y, чтобы пользователь мог нажимать в пределах кнопки.
                        # ^^ когда я смог до этого додуматся, то в этот момент я был так счастлив
                        if event.button == 1:  #  ЛКМ
                            if event.pos == (540+a, 576+b):
                                ml[i].stop()
                                i += 1
                                if i > (len(ml)-1):
                                    i = 0
                                ml[i].play()
                                sngnum = 1
                            elif event.pos == (180+a, 576+b):
                                ml[i].stop()
                                i -= 1
                                if i < 0:
                                    i = 1
                                ml[i].play()
                            elif event.pos == (360+a,576+b) and sngnum == 0:
                                pygame.mixer.unpause()
                                sngnum = 1
                            elif event.pos == (360+a,576+b) and sngnum == 1:
                                pygame.mixer.pause()
                                sngnum = 0
                    if event.button == 4:  #  Скролл вверх
                        for a in range(len(ml)): # Для каждого трека в листе
                            vol = ml[a].get_volume()
                            ml[a].set_volume(vol+0.1) # увеличиваем звук
                            a+=1
                    if event.button == 5:  #  Скролл вниз  
                        for a in range(len(ml)): # Для каждого трека в листе
                            vol = ml[a].get_volume()
                            ml[a].set_volume(vol-0.1) # уменьшаем звук
                            a+=1
            if event.type == pygame.KEYUP: # key released
                if event.key == pygame.K_RIGHT:
                    ml[i].stop()
                    i += 1
                    if i > (len(ml)-1):
                        i = 0
                    ml[i].play()
                    sngnum = 1
                elif event.key == pygame.K_LEFT:
                    ml[i].stop()
                    i -= 1
                    if i < 0:
                        i = 1
                    ml[i].play()
                    sngnum = 1
                elif event.key == pygame.K_SPACE and sngnum == 0:
                    pygame.mixer.unpause() # Возобновляет трек, вместо того, чтобы включать его заново (ml[i].play())
                    sngnum = 1
                elif event.key == pygame.K_SPACE and sngnum == 1:
                    pygame.mixer.pause() # Паузит трек, вместо того, чтобы останавливать его полностью (ml[i].stop())
                    sngnum = 0
                elif event.key == pygame.K_UP:
                    for a in range(len(ml)): # Для каждого трека в листе
                        vol = ml[a].get_volume()
                        ml[a].set_volume(vol+0.1) # увеличиваем звук
                        a+=1
                elif event.key == pygame.K_DOWN:
                    for a in range(len(ml)): # Для каждого трека в листе
                        vol = ml[a].get_volume()
                        ml[a].set_volume(vol-0.1) # уменьшаем звук
                        a+=1
                elif event.key == pygame.K_ESCAPE:
                    exit()
            elif event.type == pygame.KEYDOWN: # key pressed (hold)
                # logging: print("pressed")
                if event.key == pygame.K_LEFT:
                    pygame.draw.circle(screen, green, (180,576), 50, 5)
                    pygame.draw.circle(screen, white, (360,576), 50, 5)
                    pygame.draw.circle(screen, white, (540,576), 50, 5)
                elif event.key == pygame.K_RIGHT:
                    pygame.draw.circle(screen, white, (180,576), 50, 5)
                    pygame.draw.circle(screen, white, (360,576), 50, 5)
                    pygame.draw.circle(screen, green, (540,576), 50, 5)
                elif event.key == pygame.K_SPACE:
                    pygame.draw.circle(screen, white, (180,576), 50, 5)
                    pygame.draw.circle(screen, green, (360,576), 50, 5)
                    pygame.draw.circle(screen, white, (540,576), 50, 5)
        pygame.display.update()



# ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
# ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
# ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
# ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
# ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
# ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
# ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
# ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
# ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼    Yes, I am coding on Python. How did you know?
# ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
# ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
# ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
# ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
# ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
# ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
# ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄