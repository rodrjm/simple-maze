import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto")

# Jugador
player_size = 30
player_x = 50
player_y = 50
player_speed = 5

# Salida
exit_size = 30
exit_x = WIDTH - exit_size - 50
exit_y = HEIGHT - exit_size - 50

# Obstáculos
obstacle_size = 50
obstacle_count = 10
obstacles = set()

# Funciones
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

def draw_exit(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, exit_size, exit_size])

def draw_obstacle(x, y, width, height):
    pygame.draw.rect(screen, RED, [x, y, width, height])

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 37))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # Verificar colisión con obstáculos
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            game_over()

    # Verificar llegada a la salida
    exit_rect = pygame.Rect(exit_x, exit_y, exit_size, exit_size)
    if player_rect.colliderect(exit_rect):
        print("¡Has encontrado la salida! Ganaste.")
        running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Dibujar jugador y salida
    draw_player(player_x, player_y)
    draw_exit(exit_x, exit_y)

    # Generar nuevos obstáculos
    while len(obstacles) < obstacle_count:
        obstacle_x = random.randrange(WIDTH - obstacle_size)
        obstacle_y = random.randrange(HEIGHT - obstacle_size)
        obstacle = (obstacle_x, obstacle_y, obstacle_size, obstacle_size)

        # Asegurar que los obstáculos no se superpongan con el jugador ni la salida
        if (
            not player_rect.colliderect(pygame.Rect(obstacle)) and
            not exit_rect.colliderect(pygame.Rect(obstacle))
        ):
            obstacles.add(obstacle)

    # Dibujar obstáculos
    for obstacle in obstacles:
        draw_obstacle(*obstacle)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
sys.exit()