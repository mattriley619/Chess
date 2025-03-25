# Example file showing a circle moving on screen
import pygame
import board

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
x = board.Board





def draw_chess_board(screen):
    screen_width, screen_height = screen.get_size()
    tile_size = min(screen_width // 8, screen_height // 8)  # Dynamically calculate tile size
    colors = [(255, 255, 255), (0, 0, 0)]  # White and black
    x_offset = (screen_width - (tile_size * 8)) // 2  # Center the chessboard horizontally
    y_offset = (screen_height - (tile_size * 8)) // 2  # Center the chessboard vertically
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(
                screen,
                color,
                (x_offset + col * tile_size, y_offset + row * tile_size, tile_size, tile_size)
            )


def draw_chess_pieces(screen):
    image = pygame.image.load("kingBlack.png").convert_alpha()

    screen_width, screen_height = screen.get_size()
    tile_size = min(screen_width // 8, screen_height // 8)  # Dynamically calculate tile size
    image = pygame.transform.scale(image, (tile_size - 10, tile_size - 10))  # Scale image to fit tile size
    x_offset = (screen.get_width() - (tile_size * 2 - 10)) // 2  # Horizontal offset
    y_offset = (screen.get_height() - (tile_size * 8 - 10)) // 2  # Vertical offset
    screen.blit(image, (x_offset, y_offset))  # Draw the image at the top-left tile's center


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((59,59,59))
    draw_chess_board(screen)

    draw_chess_pieces(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 240
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(240) / 1000

pygame.quit()