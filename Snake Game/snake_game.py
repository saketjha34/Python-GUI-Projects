import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block = 20  
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Font settings
font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], snake_block, snake_block])

def your_score(score):
    value = font.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

def message(msg, color):
    mesg = font.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x_snake = width / 2
    y_snake = height / 2

    # Initial snake movement
    x_snake_change = 0
    y_snake_change = 0

    # Initial snake length
    snake_length = 1
    snake_list = []

    # Initial food position
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    # Score
    score = 0

    while not game_over:

        while game_close:
            game_display.fill(white)
            message("You lost! Press Q- To Quit or C- To Play Again", black)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x_snake_change == 0:
                    x_snake_change = -snake_block
                    y_snake_change = 0
                elif event.key == pygame.K_d and x_snake_change == 0:
                    x_snake_change = snake_block
                    y_snake_change = 0
                elif event.key == pygame.K_w and y_snake_change == 0:
                    y_snake_change = -snake_block
                    x_snake_change = 0
                elif event.key == pygame.K_s and y_snake_change == 0:
                    y_snake_change = snake_block
                    x_snake_change = 0

        # Check boundaries
        if x_snake >= width or x_snake < 0 or y_snake >= height or y_snake < 0:
            game_close = True

        x_snake += x_snake_change
        y_snake += y_snake_change
        game_display.fill(white)
        pygame.draw.rect(game_display, (255, 0, 0), [foodx, foody, snake_block, snake_block])
        snake_head = [x_snake, y_snake]
        snake_list.append(snake_head)

        # Maintain snake length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(score)

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x_snake == foodx and y_snake == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            snake_length += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
