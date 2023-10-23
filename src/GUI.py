import time
import check
import pygame

def start():
    check.bef_time = time.time()
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width = 800
    screen_height = 400
    system_info = check.run_health_checks()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("System Info")

    # Set up the font
    font = pygame.font.Font(None, 24)


    # Calculate the height of each box
    box_height = 30

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))

        # Render and display the system info
        for i, info in enumerate(system_info):
            # Calculate the position of the box
            box_x = 10
            box_y = 10 + i * box_height

            # Render the box
            pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, screen_width - 20, box_height))

            # Render the text
            text_surface = font.render(info, True, (0, 0, 0))
            screen.blit(text_surface, (box_x + 10, box_y + 5))

        # Update the display
        pygame.display.flip()
        time.sleep(0.2)
        system_info = check.run_health_checks()

    # Quit Pygame
    pygame.quit()
