import pygame
import time
import random
pygame.init()
white=[255,255,255]
blue=[0,0,255]
green=[0,180,0]
red=[255,0,0]
cyan=[0,225,255]
magneta=[255,0,255]
col=[160,200,85]
surface_width=600
surface_height=600
clock=pygame.time.Clock()
fps=30
game_surface=pygame.display.set_mode([surface_width,surface_height])
pygame.display.set_caption("Snake_Game")
font=pygame.font.SysFont(None,25,True,True)
pygame.display.update()
msg1="Snake hits the wall,game over!!!"
msg2="Press Escape to exit or Press F to play again"
msg4="Snake run onto itself,game over!!!"
def message_to_screen(text,color):
    screen_surface=font.render(text,True,color,None)
    game_surface.blit(screen_surface,[surface_width/6,surface_height/2])
    pygame.display.update()
def SnakeBody(width,height,List):
    for X in List:
        pygame.draw.rect(game_surface,blue,[X[0],X[1],width,height],0)
def GameLoop():
    game_is_on=True
    game_over=False
    x_init=300
    y_init=300
    height=15
    width=15
    AppleSize=10
    x_change=0
    y_change=0
    mov_dis=10
    rand_AppleX=random.randint(0,surface_width-AppleSize)
    rand_AppleY=random.randint(0,surface_height-AppleSize)
    score=0
    List=[]
    SnakeLength=1
    while game_is_on:
        while game_over:
            message_to_screen(msg2,cyan)
            time.sleep(1)
            game_surface.fill(white)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    msg3="Your Score is:"+str(score)
                    message_to_screen(msg3,green)
                    time.sleep(1)
                    game_is_on=False
                    game_over=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        msg3="Your Score is:"+str(score)
                        message_to_screen(msg3,green)
                        time.sleep(1)
                        game_is_on=False
                        game_over=False
                    elif event.key==pygame.K_f:
                        game_over=False
                        GameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_is_on=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-mov_dis
                    y_change=0
                elif event.key==pygame.K_RIGHT:
                    x_change=mov_dis
                    y_change=0
                elif event.key==pygame.K_UP:
                    y_change=-mov_dis
                    x_change=0
                elif event.key==pygame.K_DOWN:
                    y_change=mov_dis
                    x_change=0
        game_surface.fill(white)
        x_init+=x_change
        y_init+=y_change
        Head=[]
        Head.append(x_init)
        Head.append(y_init)
        List.append(Head)
        if len(List)>SnakeLength:
            del List[0]
        if game_is_on:    
            SnakeBody(width,height,List)
            pygame.draw.rect(game_surface,red,[rand_AppleX,rand_AppleY,AppleSize,AppleSize],0)
        pygame.display.update()
        clock.tick(fps)
        if SnakeLength>1 and game_is_on:
            for seg in List[1:-1]:
                if seg==Head:
                    game_surface.fill(white)
                    message_to_screen(msg4,col)
                    time.sleep(1)
                    game_surface.fill(white)
                    game_over=True
        if ((x_init>rand_AppleX and x_init<rand_AppleX+AppleSize)or (x_init+width>rand_AppleX and x_init+width<rand_AppleX+AppleSize)) and ((y_init>rand_AppleY and y_init<rand_AppleY+AppleSize)or (y_init+height>rand_AppleY and y_init+height<rand_AppleY+AppleSize)):
            rand_AppleX=random.randint(0,surface_width-AppleSize)
            rand_AppleY=random.randint(0,surface_height-AppleSize)
            score+=1
            SnakeLength+=1
        elif (rand_AppleX>x_init and rand_AppleX+AppleSize<x_init+width):
            if (rand_AppleY>y_init and rand_AppleY+AppleSize<y_init+height):
                rand_AppleX=random.randint(0,surface_width-AppleSize)
                rand_AppleY=random.randint(0,surface_height-AppleSize)
                score+=1
                SnakeLength+=1
        if x_init==surface_width or x_init==0 or y_init==0 or y_init==surface_height:
            game_surface.fill(white)
            message_to_screen(msg1,magneta)
            time.sleep(2)
            game_surface.fill(white)
            game_over=True
    pygame.quit()
    quit()
GameLoop()
