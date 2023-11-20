import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("sans", 20)
TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 130
tube1_x = 600
tube2_x = 800
tube3_x = 1000
background_image = pygame.image.load("background-day.png")
background_image = pygame.transform.scale(background_image, (400,600))
bird_image = pygame.image.load("bird.png")
tube_image = pygame.image.load("pipe-green_inv.png")
tube_width = 400
tube_image = pygame.transform.scale(tube_image, (50,tube_width))
tube_image_inv = pygame.image.load("pipe-green.png")
tube_image_inv = pygame.transform.scale(tube_image_inv, (50,tube_width))
# tube_image = pygame.transform.scale(tube_image, (400,600))
tube1_height = randint(0,330)
tube2_height = randint(0,330)
tube3_height = randint(0,330)
BIRD_X = 50
BIRD_Y = 50
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5
tube1_pass = False
tube2_pass = False
tube3_pass = False
game_over = False
while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_image, (0,0))
    # TUBE
    tube1_rect = screen.blit(tube_image, (tube1_x, -tube1_height))
    tube2_rect = screen.blit(tube_image, (tube2_x, -tube2_height))
    tube3_rect = screen.blit(tube_image, (tube3_x, -tube3_height))


    # TUE INVERSE
    tube1_rect_inv = screen.blit(tube_image_inv, (tube1_x, TUBE_GAP - tube1_height + tube_width))
    tube2_rect_inv = screen.blit(tube_image_inv, (tube2_x, TUBE_GAP - tube2_height + tube_width))
    tube3_rect_inv = screen.blit(tube_image_inv, (tube3_x, TUBE_GAP - tube3_height + tube_width))
    tube1_x -= TUBE_VELOCITY
    tube2_x -= TUBE_VELOCITY
    tube3_x -= TUBE_VELOCITY
    #DRAW SAND
    sand_rect = pygame.draw.rect(screen,YELLOW,(0,599,400,1))
    #DRAW SKY
    sky_rect = pygame.draw.rect(screen,BLUE,(0,0,400,1))
    # DRAW BIRD
    # bird_rect = pygame.draw.rect(screen, RED, (BIRD_X,BIRD_Y, BIRD_WIDTH,BIRD_HEIGHT))
    bird_rect = screen.blit(bird_image, (BIRD_X,BIRD_Y))
    # BIRD Fall
    BIRD_Y += bird_drop_velocity
    bird_drop_velocity += GRAVITY
    #Generate NEW TUBE
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(0,330)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(0, 330)
        tube2_pass = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(0, 330)
        tube3_pass = False
    score_txt = font.render("Score: " + str(score),True,BLACK)
    screen.blit(score_txt, (5,5))
    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score += 1
        tube3_pass = True
    # check collision
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand_rect,sky_rect]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            game_over_txt = font.render("Game Over, score: " + str(score), True,BLACK)
            screen.blit(game_over_txt, (100,300))
            continue_txt = font.render("Press Space to continue", True, BLACK)
            screen.blit(continue_txt, (100, 350))
            game_over = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    BIRD_Y = 400
                    TUBE_VELOCITY = 3
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    score = 0
                    game_over = False
                print("xxx")
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
    pygame.display.flip()

pygame.quit()