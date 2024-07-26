import pygame, sys, random
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.sprite = pygame.image.load('bird.png')
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), self.sprite.get_height())
        self.velocity = 5

class Pipe:
    def __init__(self, y, height, isUpperPipe):
        temp = pygame.image.load('pipe.png')
        if isUpperPipe:
            temp = pygame.transform.flip(temp, False, True)
        self.sprite = pygame.transform.scale(temp, (temp.get_width(), height))
        self.rect = pygame.Rect(screen_width, y, self.sprite.get_width(), height)
        self.velocity = -5

class ScorePipe:
    def __init__(self, x):
        self.rect = pygame.Rect(x, 0, 1, screen_height)
        self.passed = False
        self.velocity = -5

pygame.init()

screen_width = 1280
screen_height = 720

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

font = pygame.font.Font(None, 74)

player = Player(100, 0)

gravity = 0.5

pipes = []
score_pipes = []
score = 0

def create_pipes():
    height1 = random.randint(0, screen_height - (int(screen_height/2)))
    height2 = screen_height - (height1 + 250)
    pipe1 = Pipe(0, height1, True)
    pipe2 = Pipe(height1 + 250, height2, False)
    pipes.append(pipe1)
    pipes.append(pipe2)
    score_pipe = ScorePipe(pipe1.rect.right)
    score_pipes.append(score_pipe)

def check_collisions(player, pipes):
    for pipe in pipes:
        if player.rect.colliderect(pipe.rect):
            return True
    return False

def update_score(player, score_pipes):
    global score
    for score_pipe in score_pipes:
        if player.rect.colliderect(score_pipe.rect) and not score_pipe.passed:
            score += 1
            score_pipe.passed = True

def reset_game():
    global game_over, score, player, pipes, score_pipes
    game_over = False
    player = Player(100,0)
    pipes = []
    score_pipes = []
    score = 0

ADD_PIPE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_PIPE_EVENT, 1200)

game_over = False
game_over_image = pygame.image.load('gameover.png')
reset_text = "Press Space Bar To Restart"
reset_text_image = font.render(reset_text, True, (100,0,0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                else:
                    player.velocity = -10
        if event.type == ADD_PIPE_EVENT:
            if not game_over:
                create_pipes()

    if not game_over:
        player.velocity += gravity

        if player.rect.y + player.rect.height < screen_height:
            player.rect.y += player.velocity

        else :
            game_over = True

        if player.rect.y < 0:
            game_over = True
    
        for pipe in pipes:
            pipe.rect.x += pipe.velocity

        for score_pipe in score_pipes:
            score_pipe.rect.x += score_pipe.velocity

        if check_collisions(player, pipes):
            game_over = True
        else:
            update_score(player, score_pipes)

    screen.fill(white)

    screen.blit(background, (0,0))
    screen.blit(player.sprite, player.rect)

    for pipe in pipes:
        screen.blit(pipe.sprite, pipe.rect)

    score_text = font.render(str(score), True, black)
    screen.blit(score_text, (screen_width - 100, 50))

    if game_over:
        screen.blit(game_over_image, ((screen_width - game_over_image.get_width()) // 2, (screen_height - game_over_image.get_height()) // 2))
        screen.blit(reset_text_image, ((screen_width - reset_text_image.get_width()) // 2, (screen_height - reset_text_image.get_height()) // 2 + 100))

    pygame.display.update()

    clock.tick(60)
