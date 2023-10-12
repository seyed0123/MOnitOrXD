import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("System Info")

# Set up the font
font = pygame.font.Font(None, 24)

# Define the initial system info
system_info = [
    "CPU usage : 4.3% , CPU model: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz , number of CORS: 8",
    "memory usage: 59.4%",
    "Disk name:C:,disk free:2.7350006103515625  GB ,Disk usage: 97.7% , Disk FS typeNTFS",
    "Disk name:E:,disk free:40.280372619628906  GB ,Disk usage: 86.7% , Disk FS typeNTFS",
    "Disk name:F:,disk free:113.49983978271484  GB ,Disk usage: 62.5% , Disk FS typeNTFS",
    "Disk name:G:,disk free:37.33733367919922  GB ,Disk usage: 87.9% , Disk FS typeNTFS",
    "GPU model :NVIDIA GeForce GTX 960M, memory Free:3.9609375 GB , memory usage:0.9765625% , GPU temperature: 0.0",
    "network traffic: 56409571.00 MB",
    "Battery charge:96% , charging:True"
]

# Calculate the height of each box
box_height = 30

# Function to update the system info
def update_system_info():
    # TODO: Implement your logic to update the system info here
    # For now, we'll just update the first line with a random number
    system_info[0] = f"CPU usage : {round(pygame.time.get_ticks() / 1000 % 100, 2)}% , CPU model: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz , number of CORS: 8"

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                update_system_info()

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

# Quit Pygame
pygame.quit()
