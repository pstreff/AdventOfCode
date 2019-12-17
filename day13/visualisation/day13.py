from Computer import Computer
import pygame


screen_width = 45
screen_height = 30
scaling_factor = 10

pygame.init()
win = pygame.display.set_mode((screen_width*scaling_factor, screen_height*scaling_factor))
screen = pygame.Surface((screen_width, screen_height))

run = True
comp = Computer()

block_tiles = 0
score = 0
paddle_pos = old_paddle_pos = (0, 0)
ball_pos = old_ball_pos = (0, 0)
output = []

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    comp.run()
    output.append(comp.output)
    comp.un_halt()
    comp.run()
    output.append(comp.output)
    comp.un_halt()
    comp.run()
    output.append(comp.output)
    comp.un_halt()

    if comp.needsInputs:
        if ball_pos[0] > paddle_pos[0]:
            comp.set_input(1)
        elif ball_pos[0] < paddle_pos[0]:
            comp.set_input(-1)
        else:
            comp.set_input(0)

    if output[0] == -1 and output[1] == 0:
        score = output[2]

    if output[2] == 1:  # wall
        screen.set_at((output[0], output[1]), (255,255,255))

    if output[2] == 4:
        old_ball_pos = ball_pos
        ball_pos = (output[0], output[1])

    if output[2] == 3:
        old_paddle_pos = paddle_pos
        paddle_pos = (output[0], output[1])

    if output[2] == 2:  # block
        screen.set_at((output[0], output[1]), (151,255,255))

    screen.set_at((ball_pos[0], ball_pos[1]), (255, 0, 0))
    screen.set_at((old_ball_pos[0], old_ball_pos[1]), (0, 0, 0))
    screen.set_at((paddle_pos[0], paddle_pos[1]), (127, 255, 0))
    screen.set_at((old_paddle_pos[0], old_paddle_pos[1]), (0, 0, 0))

    output.clear()
    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))

    pygame.display.update()

    if comp.finished:
        print('Score: ', score)
        exit(12345)
