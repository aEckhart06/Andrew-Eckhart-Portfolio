# Imports
import pygame, pymunk, pymunk.pygame_util, math

# Initiate Pygame
pygame.init()

# Screen Dimensions
screenW = 1280
screenH = 720

# RGB Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (150, 150, 150)
dark_grey = (100, 100, 100)
dark_blue = (0, 158, 203)

# Screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Super Ball Hitter')

# Space
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Start Button
start_button = pygame.Rect(screenW / 2 - 200, screenH / 2 - 50, 400, 100)
instructions = pygame.Rect(screenW / 2 - 500, screenH / 2 + 90, 960, 60)

# Define Holes
topl_hole = pygame.Rect(-20, -20, 110, 110)
topm_hole = pygame.Rect(screenW / 2 - 55, -50, 110, 110)
topr_hole = pygame.Rect(screenW - 90, -20, 110, 110)
botl_hole = pygame.Rect(-20, screenH - 90, 110, 110)
botm_hole = pygame.Rect(screenW / 2 - 55, screenH - 60, 110, 110)
botr_hole = pygame.Rect(screenW - 90, screenH - 90, 110, 110)

# Points Variable
player_points = 0


# Make a function that stores all the visuals to draw the table
def table():
    # Side and corner pockets
    pygame.draw.ellipse(screen, black, topl_hole)
    pygame.draw.ellipse(screen, black, topm_hole)
    pygame.draw.ellipse(screen, black, topr_hole)
    pygame.draw.ellipse(screen, black, botl_hole)
    pygame.draw.ellipse(screen, black, botm_hole)
    pygame.draw.ellipse(screen, black, botr_hole)
    # Side borders
    pygame.draw.polygon(screen, red, [(40, 0), (screenW / 2 - 37, 0), (screenW / 2 - 37, 60), (100, 60)])
    pygame.draw.polygon(screen, red, [(screenW / 2 + 37, 0), (1240, 0), (1180, 60), (screenW / 2 + 37, 60)])
    pygame.draw.polygon(screen, red, [(0, 40), (0, screenH - 50), (60, screenH - 100), (60, 100)])
    pygame.draw.polygon(screen, red,
                        [(screenW, 40), (screenW, screenH - 50), (screenW - 60, screenH - 100), (screenW - 60, 100)])
    pygame.draw.polygon(screen, red, [(40, screenH), (screenW / 2 - 37, screenH), (screenW / 2 - 37, screenH - 60),
                                      (100, screenH - 60)])
    pygame.draw.polygon(screen, red, [(screenW / 2 + 37, screenH), (1240, screenH), (1180, screenH - 60),
                                      (screenW / 2 + 37, screenH - 60)])

    # List to store border positions


border_list = [[(40, 0), (screenW / 2 - 37, 0), (screenW / 2 - 37, 60), (100, 60)], [(screenW / 2 + 37, 0), (1240, 0),
                                                                                     (1180, 60),
                                                                                     (screenW / 2 + 37, 60)],
               [(0, 40), (0, screenH - 50), (60, screenH - 100), (60, 100)],
               [(screenW, 40), (screenW, screenH - 50), (screenW - 60, screenH - 100), (screenW - 60, 100)],
               [(40, screenH), (screenW / 2 - 37, screenH), (screenW / 2 - 37, screenH - 60), (100, screenH - 60)],
               [(screenW / 2 + 37, screenH), (1240, screenH), (1180, screenH - 60), (screenW / 2 + 37, screenH - 60)]]


# Check if the mouse is hovering over the position where the start button will be
def check_hovering():
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if screenW / 2 - 200 <= mouse_x <= screenW / 2 + 200 and screenH / 2 - 50 <= mouse_y <= screenH / 2 + 50:
        return True
    else:
        return False


# Check if the mouse is clicked over the start button
def check_start_pressed():
    if check_hovering() and pygame.mouse.get_pressed()[0]:
        return True
    else:
        return False


# Create each ball and take each ball's position and its color as arguments
def create_ball(pos, color):
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 20)
    shape.mass = 0.1
    shape.elasticity = 0.9
    shape.color = (color[0], color[1], color[2], 100)
    # Use pivot for friction
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0
    pivot.max_force = 30
    space.add(body, shape, pivot)
    return shape


# Create each border and take the dimensions of each border as arguments
def create_borders(dimensions):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    shape = pymunk.Poly(body, dimensions)
    shape.mass = 1000
    shape.elasticity = 0.3
    shape.friction = 0.4
    shape.color = (255, 0, 0, 100)
    space.add(body, shape)
    return shape


# Balls
b1 = create_ball((421, 340), dark_blue)
b2 = create_ball((380, 319), dark_blue)
b3 = create_ball((380, 361), dark_blue)
b4 = create_ball((339, 299), dark_blue)
b5 = create_ball((339, 340), dark_blue)
b6 = create_ball((339, 381), dark_blue)
b7 = create_ball((298, 278), dark_blue)
b8 = create_ball((298, 319), dark_blue)
b9 = create_ball((298, 361), dark_blue)
b10 = create_ball((298, 402), dark_blue)
b11 = create_ball((257, 258), dark_blue)
b12 = create_ball((257, 299), dark_blue)
b13 = create_ball((257, 340), dark_blue)
b14 = create_ball((257, 381), dark_blue)
b15 = create_ball((257, 422), dark_blue)
bw = create_ball((700, 340), white)
# Ball list
b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
# List to check if a ball has been scored or not
ball_point_list = []
for ball in b_list:
    ball_point_list.append(False)


# Checks if a ball has been scored and changes the corresponding value in the ball_point_list
def point_system():
    global player_points, ball_point_list
    for eachBall in b_list:
        if eachBall.body.position.x < 0 or eachBall.body.position.x > screenW or eachBall.body.position.y < 0 or eachBall.body.position.y > screenH:
            index = b_list.index(eachBall)
            ball_point_list[index] = True
        player_points = 0
        for x in ball_point_list:
            if x:
                player_points += 1
    return player_points


# Return the white ball to its original position
def bw_return():
    global bw
    if bw.body.position.x <= 0 or bw.body.position.x >= screenW or bw.body.position.y >= screenH or \
            bw.body.position.y <= 0:
        bw = create_ball((700, 340), white)


# Create the borders on the screen
for b in border_list:
    create_borders(b)


# Fint the current position of the mouse
def mouse_pos1():
    return pygame.mouse.get_pos()


# Calculate the total distance between two different points
def calc_distance(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)


# Calculate the angle relative to the horizontal between two different points
def calc_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


# Determine the impulse applied to the white ball in the x and y direction
def force_fun():
    mouse_pos2 = pygame.mouse.get_pos()
    angle = calc_angle(mouse_pos_1, mouse_pos2)
    impulse_pointx = calc_distance(mouse_pos_1, mouse_pos2) * math.cos(angle)
    if impulse_pointx >= 300:
        impulse_pointx = 300
    elif impulse_pointx <= -300:
        impulse_pointx = -300
    impulse_pointy = calc_distance(mouse_pos_1, mouse_pos2) * math.sin(angle)
    if impulse_pointy >= 300:
        impulse_pointy = 300
    elif impulse_pointy <= -300:
        impulse_pointy = -300
    bw.body.apply_impulse_at_local_point((impulse_pointx * -1, impulse_pointy * -1), (0, 0))


# Game start and game done variables
game_done = False
game_start = True


# Game function for game visuals
def game(start, finish):
    global game_start
    if start:
        table()
        pygame.draw.rect(screen, black, start_button)
        font = pygame.font.SysFont("Ariel", 100)
        start_text = font.render('PLAY', True, white)
        screen.blit(start_text, (screenW / 2 - 100, screenH / 2 - 30))

        pygame.draw.rect(screen, black, instructions)
        font = pygame.font.SysFont("Ariel", 50)
        start_text = font.render('Click and drag your mouse to fire the white ball', True,
                                 white)
        screen.blit(start_text, (screenW / 2 - 420, screenH / 2 + 100))
        if check_hovering() and check_start_pressed():
            game_start = False
    elif finish:
        screen.fill(black)

        font = pygame.font.SysFont("Ariel", 100)
        game_over = font.render('Game Over', True, white)
        screen.blit(game_over, (screenW / 2, screenH / 2))
    else:
        # Visuals
        table()
        font = pygame.font.SysFont("Ariel", 50)

        score_num = font.render(str(player_points), True, white)
        screen.blit(score_num, (screenW / 2, screenH / 2))


# Game running
game_running = True
# Clock
clock = pygame.time.Clock()
# FPS
FPS = 120
while game_running:
    clock.tick(FPS)
    space.step(1 / FPS)
    screen.fill(dark_grey)
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos_1 = mouse_pos1()
        if event.type == pygame.MOUSEBUTTONUP:
            force_fun()
        if player_points >= 15:
            game_done = True

    # Call the game's visuals
    if game_start:
        game(True, False)
    elif game_done:
        game(False, True)
    else:
        game(False, False)

    point_system()
    bw_return()
    # Call the bodies from pymunk to be drawn
    if not game_start and not game_done:
        space.debug_draw(draw_options)
    # Update the game after every frame
    pygame.display.update()
# Quit
pygame.quit()
