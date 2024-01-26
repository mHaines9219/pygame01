import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_radius = 50  # Define the player's radius
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def keep_player_on_screen(player_pos, screen_width, screen_height, player_radius):
    # Check and adjust for each boundary
    if player_pos.x - player_radius < 0:
        player_pos.x = player_radius
    elif player_pos.x + player_radius >= screen_width:
        player_pos.x = screen_width - player_radius

    if player_pos.y - player_radius < 0:
        player_pos.y = player_radius
    elif player_pos.y + player_radius > screen_height:
        player_pos.y = screen_height - player_radius

    return player_pos


while running:
    dt = clock.tick(60) / 1000.0
    print(
        "player pos x is"
        + str(player_pos.x)
        + "player pos y is"
        + str(player_pos.y)
        + "screen width is"
        + str(screen.get_width())
        + "screen height is"
        + str(screen.get_height())
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Update player position based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 2000 * dt
    if keys[pygame.K_s]:
        player_pos.y += 2000 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 2000 * dt
    if keys[pygame.K_d]:
        player_pos.x += 2000 * dt

    # Ensure player stays on screen
    player_pos = keep_player_on_screen(
        player_pos, screen.get_width(), screen.get_height(), player_radius
    )

    # Draw the red player circle
    pygame.draw.circle(
        screen, "white", (int(player_pos.x), int(player_pos.y)), player_radius
    )

    # Draw the green circle in the bottom-right corner
    green_circle_x = screen.get_width() - player_radius  # X position
    green_circle_y = screen.get_height() - player_radius  # Y position
    pygame.draw.circle(screen, "green", (green_circle_x, green_circle_y), player_radius)

    purple_circle_x = 0 + player_radius  # X position
    purple_circle_y = screen.get_height() - player_radius  # Y position
    pygame.draw.circle(
        screen, "purple", (purple_circle_x, purple_circle_y), player_radius
    )
    yellow_circle_x = 0 + player_radius  # X position
    yellow_circle_y = 0 + player_radius  # Y position
    pygame.draw.circle(
        screen, "yellow", (yellow_circle_x, yellow_circle_y), player_radius
    )
    red_circle_x = screen.get_width() - player_radius  # X position
    red_circle_y = 0 + player_radius  # Y position
    pygame.draw.circle(screen, "red", (red_circle_x, red_circle_y), player_radius)

    pygame.display.flip()

pygame.quit()
