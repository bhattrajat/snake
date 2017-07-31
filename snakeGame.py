import pygame
import random

#basic initialization
pygame.init()
white = (255,255,255)
red = (255,0,0)
green = (0,100,0)
blue = (0,0,255)
black = (0,0,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height)) #create display
pygame.display.set_caption("snake") #create title
icon = pygame.image.load("gameicon.png")
pygame.display.set_icon(icon)
img = pygame.image.load("snakehead.png")
img2 = pygame.image.load("apple.jpg")
block_size = 20
FPS = 10
gameExit = False
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms",25)
direction = "up"

def text_objects(text,color):
    textSurf = font.render(text,True,color)
    return textSurf,textSurf.get_rect()

def print_message(msg,color):
    textSurf,textRect = text_objects(msg,color)
    textRect.center = (display_width / 2),(display_height / 2)
   #message = font.render(msg,True,color)
   #gameDisplay.blit(message,[display_width/2,display_height/2])
    gameDisplay.blit(textSurf,textRect)

def score(score):
    score_text = font.render("Score: "+str(score),True,green)
    gameDisplay.blit(score_text,[0,0])
    
def snake(block_size,snakeList):
    if direction == "up":
        head = img
    elif direction == "left":
        head = pygame.transform.rotate(img,90)
    elif direction == "down":
        head = pygame.transform.rotate(img,180)
    elif direction == "right":
        head = pygame.transform.rotate(img,270)
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for xy in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,green,[xy[0],xy[1],block_size,block_size])
        
def gameLoop():
    global direction
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    gameExit = False
    gameOver = False
    apple_x = random.randrange(0,display_width-block_size,20)
    apple_y = random.randrange(0,display_height-block_size,20)
    snakeList = []
    snakeLength = 1
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            print_message("GAME OVER press  q to quit and r to restart",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        gameLoop()
            clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction == "right":
                        pass
                    else:
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if direction == "left":
                        pass
                    else:
                        direction = "right"
                        lead_x_change = block_size
                        lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if direction == "down":
                        pass
                    else:
                        direction = "up"
                        lead_x_change = 0
                        lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    if direction == "up":
                        pass
                    else:
                        direction = "down"
                        lead_x_change = 0
                        lead_y_change = block_size
        score(snakeLength - 1)
       
        #display collision
        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver = True
        #self collision
        for xy in snakeList[:-1]:
            if snakeList[-1][0] == xy[0]  and snakeList[-1][1] == xy[1]: 
                gameOver = True
        if lead_x == apple_x and lead_y == apple_y:
            apple_x = random.randrange(0,display_width-block_size,20)
            apple_y = random.randrange(0,display_height-block_size,20)
            snakeLength += 1
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        #pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,block_size,block_size])
        gameDisplay.blit(img2,(apple_x,apple_y))
        score(snakeLength - 1)
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        snake(block_size,snakeList)
        
        pygame.display.update()
        clock.tick(FPS)
    
gameLoop()
