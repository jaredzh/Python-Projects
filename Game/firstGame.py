import pygame
import os
pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("First Game")

# mydir = os.path.dirname('/Users/jaredzh12/PycharmProjects/firstGame/Game/firstGame.py')
# bg = pygame.image.load(os.path.join(mydir, 'bg1.jpg'))


def imageLoad(file):
    directory = os.path.dirname('/Users/jaredzh12/PycharmProjects/firstGame/Game/firstGame.py')
    image = pygame.image.load(os.path.join(directory, file))
    image.convert_alpha()
    return image


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(idle, (x, y))
    pygame.display.update()


bg = imageLoad('bg1.jpg')
idle = imageLoad('standing.png')
walkRight = [imageLoad('R1.png'), imageLoad('R2.png'), imageLoad('R3.png'), imageLoad('R4.png'), imageLoad('R5.png'),
             imageLoad('R6.png'), imageLoad('R7.png'), imageLoad('R8.png'), imageLoad('R9.png')]
walkLeft = [imageLoad('L1.png'), imageLoad('L2.png'), imageLoad('L3.png'), imageLoad('L4.png'), imageLoad('L5.png'),
            imageLoad('L6.png'), imageLoad('L7.png'), imageLoad('L8.png'), imageLoad('L9.png')]

clock = pygame.time.Clock()

x = 200
y = 200
width = 30
height = 50
vel = 5
isJump = False
jumpCount = 10

boolean = True
left = False
right = False
walkCount = 0


while boolean:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boolean = False

    # pygame.draw.rect(win, (200, 150, 20), (x, y, width, height))
    # pygame.display.update()

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x -= vel
        if x < 0:
            x += vel

    if key[pygame.K_RIGHT]:
        x += vel
        if x > 852 - width:
            x -= vel

    if not isJump:
        # if key[pygame.K_UP] and y > vel:
        #     y -= vel

        # if key[pygame.K_DOWN] and y < 500 - height - vel:
        #     y += vel

        if key[pygame.K_SPACE]:
            isJump = True

        if key[pygame.K_RIGHT]:
            right = True
            left = False

        if key[pygame.K_LEFT]:
            left = True
            right = False
    elif right:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            right = False

    elif left:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.25 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            left = False

    redrawGameWindow()

pygame.quit()