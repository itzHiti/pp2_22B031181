import pygame, math

pygame.init()

def main():
    res = w, h = 1080, 720
    screen = pygame.display.set_mode(res)
    clock = pygame.time.Clock()

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    color = BLUE
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    List = [RED,GREEN,BLUE]
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)

    x = 0
    y = 0
    c = 0

    drawrect = 0 ### if you draw, then == 1
    drawcircle = 0
    drawsquare = 0
    drawRightTriangle = 0
    drawEqualTriangle = 0
    drawRhombus = 0

    isPressed = False
    screen.fill(WHITE)
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_SPACE:
                    drawrect = 1
                elif event.key == pygame.K_c:
                    drawcircle = 1
                elif event.key == pygame.K_s:
                    drawsquare = 1
                elif event.key == pygame.K_t:
                    drawRightTriangle = 1
                elif event.key == pygame.K_y:
                    drawEquilTriangle = 1
                elif event.key == pygame.K_u:
                    drawRhombus = 1
            
            # Eraser and rectangle
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for i in range(1030,1045):
                    for j in range(40, 55):
                        if i == x and j == y:
                            if c>2:
                                c=0
                            color = List[c]
                            c+=1
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for i in range(1030,1045):
                    for j in range(1, 16):
                        if i == x and j == y:
                            color = WHITE
                isPressed = True 
            
            # Eraser 
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False

            if event.type == pygame.MOUSEMOTION and isPressed == True and drawrect == drawcircle == drawsquare == 0:         
                (x, y) = pygame.mouse.get_pos()   # returns the position of mouse cursor
                if color == WHITE:
                    pygame.draw.rect(screen, color, (x-20,y-20,40,40))
                else:
                    pygame.draw.circle( screen,color, (x, y), 10)
            
            if isPressed == True and drawrect == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.rect(screen, color, (x-25,y-20,50,40))
                drawrect = 0
            
            elif isPressed == True and drawcircle == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.circle( screen,color, (x, y), 20)
                drawcircle = 0
            elif isPressed and drawsquare == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.rect( screen, color, (x-25, y-25,50,50))
                drawsquare = 0
            elif isPressed and drawRightTriangle == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, color, [(x, y), (x, y-100), (x+70, y)])
                drawingRightTriangle = 0
            elif isPressed and drawEqualTriangle == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y-100*math.sqrt(3)//2)])
                drawEqualTriangle = 0
            elif isPressed and drawRhombus == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y-100*math.sqrt(3)//2)])
                pygame.draw.polygon(screen, color, [(x, y), (x+100, y), (x+50, y+100*math.sqrt(3)//2)])
                drawRhombus = 0


        # Little GUI
        pygame.draw.rect(screen, BLACK, (1030,1,15,15), 1)
        eraser = font_small.render("Eraser (press me): ", True, BLACK)
        screen.blit(eraser, (833, -6)) #^^ - 197
        pygame.draw.rect(screen, color, (1030,40,15,15))
        pygame.draw.rect(screen, BLACK, (1028,38,17,17), 2)
        col = font_small.render("Color: ", True, BLACK)
        screen.blit(col, (960, 30)) #^^ - 68
        
        pygame.display.flip()
        
        clock.tick(60)

main()