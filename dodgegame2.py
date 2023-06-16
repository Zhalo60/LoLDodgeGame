import pygame, time, random

winwidth = 1600
winheight = 1000
playerx = 300
playery = 400
laserx = 800
lasery = -100
laserINDCx = 800
laserINDCy = -100
vertlaserx = -100
vertlasery = 500
vertlaserINDCx = -100
vertlaserINDCy = 500
difficulty = 1.5
vertdifficulty = 1.5
deathcount = 0

class Player(pygame.sprite.Sprite):

    def __init__(self, speed, color):
        super().__init__()
        self.image = pygame.Surface((50, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, 'purple', self.image.get_rect())
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2(playerx, playery)
        self.target = pygame.Vector2(playerx, playery)
        self.speed = speed

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length != 0:
            move.normalize_ip()
            move = move * min(move_length, self.speed)
            self.pos += move

        self.rect.center = self.pos

class Laser(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((winwidth, 100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.rect = self.image.get_rect(center=(laserx, lasery))

class LaserINDC(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((winwidth, 100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 50))
        self.rect = self.image.get_rect(center=(laserINDCx, laserINDCy))

class vertLaser(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.rect = self.image.get_rect(center=(vertlaserx, vertlasery))

class vertLaserINDC(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 50))
        self.rect = self.image.get_rect(center=(vertlaserINDCx, vertlaserINDCy))

def main():

    global lasery
    global laserINDCy
    global vertlaserx
    global vertlaserINDCx
    global difficulty
    global vertdifficulty
    global deathcount

    pygame.init()

    screen = pygame.display.set_mode((winwidth, winheight), pygame.SRCALPHA)
    pygame.display.set_caption("League Of Legends")

    clock = pygame.time.Clock()
    start_time = time.time()

    clock2 = pygame.time.Clock()
    start_time2 = time.time()

    clock3 = pygame.time.Clock()
    start_time3 = time.time()

    clock4 = pygame.time.Clock()
    start_time4 = time.time()

    player = pygame.sprite.Group(Player(6, pygame.Color(255, 0, 0, 255)))

    laser = Laser()
    laser_group = pygame.sprite.Group()
    laser_group.add(laser)

    laserINDC = LaserINDC()
    laserINDC_group = pygame.sprite.Group()
    laserINDC_group.add(laserINDC)

    vertlaser = vertLaser()
    vertlaser_group = pygame.sprite.Group()
    vertlaser_group.add(vertlaser)

    vertlaserINDC = vertLaserINDC()
    vertlaserINDC_group = pygame.sprite.Group()
    vertlaserINDC_group.add(vertlaserINDC)

    running = True
    while running:

        time_alive = time.time()
        time_difference = time_alive - start_time

        time_alive2 = time.time()
        time_difference2 = time_alive2 - start_time2

        time_alive3 = time.time()
        time_difference3 = time_alive3 - start_time3

        time_alive4 = time.time()
        time_difference4 = time_alive4 - start_time4

        # font = pygame.font.SysFont("Arial", 60, False, False)
        # font_image = font.render(str(round(time_difference, 2)), True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for movement in player.sprites():
                    movement.target = pygame.mouse.get_pos()

        if pygame.sprite.groupcollide(player, laser_group, True, True):
            player = pygame.sprite.Group(
            Player(6, pygame.Color(160, 32, 240, 255)))
            laser = Laser()
            laser_group = pygame.sprite.Group()
            laser_group.add(laser)
            start_time = time_alive
            start_time2 = time_alive2
            start_time3 = time_alive3
            start_time4 = time_alive4
            deathcount += 1

        if pygame.sprite.groupcollide(player, vertlaser_group, True, True):
            player = pygame.sprite.Group(
            Player(6, pygame.Color(160, 32, 240, 255)))
            vertlaser = vertLaser()
            vertlaser_group = pygame.sprite.Group()
            vertlaser_group.add(vertlaser)
            start_time = time_alive
            start_time2 = time_alive2
            start_time3 = time_alive3
            start_time4 = time_alive4
            deathcount += 1

        if time_difference >= 1:
            laserINDCy = random.randint(100, 900)
            laserINDC = LaserINDC()
            laserINDC_group = pygame.sprite.Group()
            laserINDC_group.add(laserINDC)
            start_time = time_alive

        if time_difference2 >= difficulty:
            lasery = laserINDCy
            laser = Laser()
            laser_group = pygame.sprite.Group()
            laser_group.add(laser)
            start_time = time_alive
            start_time2 = time_alive2

        if time_difference3 >= 1:
            vertlaserINDCx = random.randint(100, 1500)
            vertlaserINDC = vertLaserINDC()
            vertlaserINDC_group = pygame.sprite.Group()
            vertlaserINDC_group.add(vertlaserINDC)
            start_time3 = time_alive3

        if time_difference4 >= vertdifficulty:
            vertlaserx = vertlaserINDCx
            vertlaser = vertLaser()
            vertlaser_group = pygame.sprite.Group()
            vertlaser_group.add(vertlaser)
            start_time3 = time_alive3
            start_time4 = time_alive4

        if deathcount >= 3:
            lasery = random.randint(100, 900)
            vertlaserx = random.randint(100, 1500)

            laserINDCy = lasery
            vertlaserINDCx = vertlaserx

            laser = Laser()
            laser_group = pygame.sprite.Group()
            laser_group.add(laser)

            vertlaser = vertLaser()
            vertlaser_group = pygame.sprite.Group()
            vertlaser_group.add(vertlaser)

            laserINDC = LaserINDC()
            laserINDC_group = pygame.sprite.Group()
            laserINDC_group.add(laserINDC)

            vertlaserINDC = vertLaserINDC()
            vertlaserINDC_group = pygame.sprite.Group()
            vertlaserINDC_group.add(vertlaserINDC)

            deathcount = 0



        player.update()
        screen.fill('dark green')
        player.draw(screen)
        laser_group.draw(screen)
        laserINDC_group.draw(screen)
        vertlaser_group.draw(screen)
        vertlaserINDC_group.draw(screen)
        # screen.blit(font_image, [winwidth // 2 - 60, 100])
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()