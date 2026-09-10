import pygame


pygame.init()

x = 400
y = 300

screen = pygame.display.set_mode((1994, 1000))

square = pygame.Rect(1003, 500, 68, 66)


speed = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square.x -= speed
    if keys[pygame.K_RIGHT]:
        square.x += speed
    if keys[pygame.K_UP]:
        square.y -= speed
    if keys[pygame.K_DOWN]:
        square.y += speed
    
    screen.fill((74, 10, 11))


    pygame.draw.rect(screen, (81, 113, 135), square)

    pygame.display.flip()

pygame.quit()