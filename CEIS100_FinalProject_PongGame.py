
import random
import math
import pygame
from pygame.locals import *


def main():

    run = 1
    while run == 1:

        # Constants/Setting Grid
        WINSIZE = [800,600]
        WHITE = [255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN = [0,255,0]
        BLUE = [0,0,255]
        BLOCKSIZE = [20,20]
        MAXX = 780
        MINX = 20
        MAXY = 580
        MINY = 0
        BLOCKSTEP = 20
        TRUE = 1
        FALSE = 0
        PADDLELEFTYVAL = 25 
        PADDLERIGHTYVAL = 775
        LEFT = 1
        RIGHT = 0
        PADDLESTEP = 4 
        
        # Variables
        paddleleftxy = [5,200]
        paddlerightxy = [775,200]
        scoreleft = 0
        scoreright = 0
        gameover = TRUE
        ballxy = [200,200]

        # Ball speed 
        ballspeed = 2
        balldy = 1
        balldx = 1

        # service for left/right
        # start score at 0
        ballservice = TRUE
        service = LEFT
        scoreleft = 0
        scoreright = 0


        ballcludge = 0 # added for problems with right paddle

        # Initialization
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('CEIS PONG')
        screen.fill(BLACK)
        paddle = pygame.image.load('paddle.bmp').convert()
        paddleerase = pygame.image.load('paddle_shadow.bmp').convert() #gets rid of paddle shadow
        ball = pygame.image.load('blue_ball.bmp').convert()
        ballerase = pygame.image.load('ball_shadow.bmp').convert() #gets rid of ball shadow
        textleft = [1,1,2,2]
        textright = [3,3,4,4]

        # Title Screen   
        while gameover == TRUE:
            # font for heading 
            font = pygame.font.SysFont("arial", 32)
            text_surface = font.render("A Game by Evan Bailey", True, GREEN)
            screen.blit(text_surface, (260,10))

            # font for game title
            font = pygame.font.SysFont("times", 50)
            text_surface = font.render("---------- CEIS PONG ----------", True, GREEN)
            screen.blit(text_surface, (95,100))

            # font for game instructions
            font = pygame.font.SysFont("arial", 32)
            text_surface = font.render("Instructions:", True, BLUE)
            screen.blit(text_surface, (325,200))
            text_surface = font.render("-Left paddle (A and Z to move)", True, GREEN)
            screen.blit(text_surface, (170,250))
            text_surface = font.render("-Right paddle (UP and DOWN to move)", True, GREEN)
            screen.blit(text_surface, (170,300))
            text_surface = font.render("-S or RETURN to serve the ball", True, GREEN)
            screen.blit(text_surface, (170,350))
            text_surface = font.render("-P to pause, R to resume, Q to quit", True, GREEN)
            screen.blit(text_surface, (170,400))
            text_surface = font.render("-Press N to start a new game", True, GREEN)
            screen.blit(text_surface, (170,450))
            pygame.display.update()

            # New game and quit functions
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[K_n]:
                gameover = FALSE
                screen.fill(BLACK)
                # Start in game music
                pygame.mixer.music.load('background_music2.wav')
                pygame.mixer.music.play(-1) #-1 so music never stops in game loop
            elif pressed_keys[K_q]:
                run = 0
                exit()

            clock.tick(20)
            

        # Game loop  
        while not gameover:

            # clear screen on paddles and ball and print scores
            screen.blit(paddleerase,paddleleftxy)
            screen.blit(paddleerase,paddlerightxy)
            screen.blit(ballerase,ballxy)
            
            ##In game fonts/locations
                #Player1
            font = pygame.font.SysFont("arial", 25)
            text_surface1 = font.render("Player 1", True, GREEN)
            screen.blit(text_surface1, (90,15))
                #Player2
            font = pygame.font.SysFont("arial", 25)
            text_surface1 = font.render("Player 2", True, GREEN)
            screen.blit(text_surface1, (620,15))
                #scores 
            font = pygame.font.SysFont("arial", 64)
            text_surface1 = font.render(str(scoreleft), True, WHITE)
            textleft = screen.blit(text_surface1, (115,40))
            text_surface1 = font.render(str(scoreright), True, WHITE)
            textright = screen.blit(text_surface1, (645,40))
                #Title
            font = pygame.font.SysFont("times", 32) 
            text_surface1 = font.render("CEIS PONG", True, GREEN)
            screen.blit(text_surface1, (315, 40))
                #In game instructions
            font = pygame.font.SysFont("arial", 20)
            text_surface1 = font.render("First Player To 7 WIns", True, WHITE, BLUE)
            screen.blit(text_surface1, (300, 80))

            # move paddles
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[K_a]:
                if paddleleftxy[1] > MINY:
                    paddleleftxy[1] = paddleleftxy[1] - PADDLESTEP

            elif pressed_keys[K_z]:
                if paddleleftxy[1] < MAXY - 80:
                    paddleleftxy[1] = paddleleftxy[1] + PADDLESTEP

                    
            if pressed_keys[K_UP]:
                if paddlerightxy[1] > MINY:
                    paddlerightxy[1] = paddlerightxy[1] - PADDLESTEP

            elif pressed_keys[K_DOWN]:
                if paddlerightxy[1] < MAXY - 80:
                    paddlerightxy[1] = paddlerightxy[1] + PADDLESTEP

            # serve the ball
            if (pressed_keys[K_s] or pressed_keys[K_RETURN]) and ballservice == TRUE:
                ballservice = FALSE
                if service == LEFT:
                    # random ball direction on serve
                    balldx = random.randrange(2,3)
                    balldy = random.randrange(-3,3)
                    service = RIGHT
                else:
                    # random ball direction on serve
                    balldx = random.randrange(2,3)
                    balldy = random.randrange(-3,3)
                    service == LEFT
                
            if pressed_keys[K_q]:
                run = 0
                exit()

            # Pause screen
            if pressed_keys[K_p]:
                gamepaused = TRUE
                font = pygame.font.SysFont("arial", 32)
                paused_surface = font.render("PAUSED: Press 'R' To Resume", True, GREEN)
                paused_rect = screen.blit(paused_surface, (200,250))#275originallyfont64
                pygame.display.update()
                #font = pygame.font.SysFont("arial",32)
                #paused_surface = font.render("-Press 'R' To Resume", True, BLUE)
                #paused_rect = screen.blit(paused_surface, (250,400))
                #pygame.display.update()

                while gamepaused == TRUE:

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                    
                    pressed_keys = pygame.key.get_pressed()

                    if pressed_keys[K_r]:
                        gamepaused = FALSE
                    clock.tick(20)

                pygame.draw.rect(screen,BLACK,paused_rect)
                


            # if not serving just move the ball
            if ballservice is not TRUE:
                # have we hit the left paddle
                if ballxy[0] <(paddleleftxy[0] + 20) and ballxy[1] > (paddleleftxy[1] - 18) and ballxy[1] < (paddleleftxy[1] + 98):
                    balldx = -balldx
                    if pressed_keys[K_a] or pressed_keys[K_z]:
                        balldy = random.randrange(2,4)
                    else:
                        balldy = random.randrange(0,3)
                        
                # have we hit the right paddle
                elif ballxy[0] > (paddlerightxy[0] - 20) and ballxy[1] > (paddlerightxy[1] - 18) and ballxy[1] <= (paddlerightxy[1] + 98):

                    # ballcludge counter to make sure ball did not bounce through paddle
                    if ballcludge == 0:
                        balldx = -balldx
                        if pressed_keys[K_UP] or pressed_keys[K_DOWN]:
                            balldy = random.randrange(2,4)
                        else:
                            balldy = random.randrange(0,3)
                        ballcludge = 1
                    else:
                        ballcludge = ballcludge + 1
                        if ballcludge == 4:
                            ballcludge = 0
                            
                # has ball hit the top of screen
                elif ballxy[1] <= MINY:
                    balldy = -balldy
                elif ballxy[1] >= MAXY:
                    balldy = -balldy
                    
                # has ball passed the left paddle
                elif ballxy[0] <= MINX:
                    ballservice = TRUE
                    service = RIGHT
                    scoreright = scoreright + 1 # right player scores
                        # clear the score
                    pygame.draw.rect(screen,BLACK,textright)
                
                elif ballxy[0] >= MAXX:
                    ballservice = TRUE
                    service = LEFT
                    scoreleft = scoreleft + 1 # left player scores
                        # clear the score 
                    pygame.draw.rect(screen,BLACK,textleft)
                       
                    
                    
                # moving ball
                ballxy[0] = ballxy[0] + (ballspeed * balldx)
                ballxy[1] = ballxy[1] + (ballspeed * balldy)

            # start ball on paddle at serve
            else:
                if service == LEFT:
                    ballxy[0] = paddleleftxy[0] + 25
                    ballxy[1] = paddleleftxy[1] + 40
                elif service == RIGHT:
                    ballxy[0] = paddlerightxy[0] - 25
                    ballxy[1] = paddlerightxy[1] + 40

            # Game over after score of 7
                if scoreleft == 7:
                    font = pygame.font.SysFont("arial", 50)
                    paused_surface = font.render("GAME OVER: Player 1 WINS!!", True, GREEN)
                    paused_rect = screen.blit(paused_surface, (50,250))
                    pygame.display.update()
                    exit()
                elif scoreright == 7:
                    font = pygame.font.SysFont("arial", 50)
                    paused_surface = font.render("GAME OVER: Player 2 WINS!!", True, GREEN)
                    paused_rect = screen.blit(paused_surface, (50,250))
                    pygame.display.update()
                    exit()
                    
            #render screen 
            screen.blit(paddle,paddleleftxy)
            screen.blit(paddle,paddlerightxy)
            screen.blit(ball,ballxy)
            pygame.display.update()

          
            clock.tick(100)
        

if __name__ == '__main__':
    main()

