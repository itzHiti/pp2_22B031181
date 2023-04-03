import pygame

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

    radius = 15
    x = 0
    y = 0
    z = 0
    mode = 'blue'
    points = []

    drawrect = 0
    drawcircle = 0

    isPressed = False
    
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
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_SPACE:
                    drawrect = 1
                    drawcircle = 0
                elif event.key == pygame.K_c:
                    drawcircle = 1
                    drawrect = 0
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
            
        ###ERASER+RECT###
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for i in range(650,665):
                    for j in range(40, 55):
                        if i == x and j == y:
                            if z>2:
                                z=0
                            color = List[z]
                            z+=1
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for i in range(650,665):
                    for j in range(1, 16):
                        if i == x and j == y:
                            color = WHITE
                isPressed = True 
            ###ERASER###
            
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION and isPressed == True and drawrect == drawcircle == 0:         
                (x, y) = pygame.mouse.get_pos()   # returns the position of mouse cursor, cuz we need x and y to modify
                if color == WHITE:
                    pygame.draw.rect(screen, color, (x-20,y-20,40,40))
                else:
                    pygame.draw.circle( screen, color, (x, y), 10)
            if isPressed == True and drawrect == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.rect(screen, color, (x-25,y-20,50,40))
                drawrect = 0
            elif isPressed == True and drawcircle == 1:  
                (x, y) = pygame.mouse.get_pos()
                pygame.draw.circle( screen, color, (x, y), 20)
                drawcircle = 0
                
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, BLACK, (650,1,15,15), 1)
        pygame.draw.rect(screen, color, (650,40,15,15))
        pygame.draw.rect(screen, BLACK, (648,38,17,17), 2)
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()