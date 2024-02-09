import pygame
import tkinter as tk
from tkinter import messagebox
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60
car_speed = 10
obstacle_speed = 5
obstacle_frequency = 45 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Car Racing Game")


car_img = pygame.image.load("assets\\images\\car.png")
car_img = pygame.transform.scale(car_img, (100, 160))  


clock = pygame.time.Clock()

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80  
        self.height = 160  
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(car_img, (self.x, self.y))

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

class Obstacle:
    def __init__(self, x, y, width, height, color_variation, shape_variation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_variation = color_variation
        self.shape_variation = shape_variation
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.rect.topleft = (self.x, self.y) 

       
        if self.color_variation == 1:
            color = RED
        else:
            color = WHITE

        if self.shape_variation == 1:
            pygame.draw.rect(screen, color, self.rect)
        else:
            pygame.draw.circle(screen, color, self.rect.center, self.width // 2)

def check_collision(car, obstacle):
    
    return car.rect.colliderect(obstacle.rect)

def game_loop():
    car = Car(WIDTH // 2 - 40, HEIGHT - 240)  
    obstacles = []

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and car.x > 0:
            car.x -= car_speed
        if keys[pygame.K_d] and car.x < WIDTH - car.width:
            car.x += car_speed

        
        if random.randrange(0, obstacle_frequency) == 0:
            obstacle_width = random.randint(50, 100)
            obstacle_height = random.randint(50, 100)
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            color_variation = random.randint(1, 2) 
            shape_variation = random.randint(1, 2)  
            obstacles.append(Obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height, color_variation, shape_variation))

       
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score += 1

            # Check for collisions with the car
            if check_collision(car, obstacle):
                game_over(score)

       
        car.update_rect()

       
        screen.fill(BLACK)
        car.draw()
        for obstacle in obstacles:
            obstacle.draw()

      
        font = pygame.font.SysFont(None, 30)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

def game_over(score):
    pygame.mixer.music.stop()
    response = messagebox.askyesno("Game Over", "Your car crashed! Your score: {}\nDo you want to play again?".format(score))
    if response:
        
        game_loop()
    else:
        pygame.quit()
        quit()

def start_game():
    root.destroy()
    pygame.mixer.music.load("assets\\music\\background_music.mp3")
    pygame.mixer.music.play(1)
    game_loop()

root = tk.Tk()
root.title("Car Racing Game")


label = tk.Label(root, text="2D Car Racing Game", font=("Helvetica", 16))
label.pack(pady=10)


start_button = tk.Button(root, text="Start Game", command=start_game, font=("Helvetica", 14))
start_button.pack(pady=20)


root.mainloop()
