import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:
    # poll for events
    dt = clock.tick(60) / 1000.0
    # pygame.quit event is when user clicked x to close window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with a color to wipe away previous frame
    screen.fill("blue")

    # render game logic

    pygame.draw.circle(screen, "red", player_pos, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
    # flip() the displaty to pout your work on screen

    pygame.display.flip()

    clock.tick(60)  # limit fps to 60

pygame.quit()
