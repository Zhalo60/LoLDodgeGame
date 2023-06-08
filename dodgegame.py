import pygame

winwidth = 1600
winheight = 1000
class Player(pygame.sprite.Sprite):
    def __init__(self, speed, color):
        super().__init__()
        self.image = pygame.Surface((50, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, self.image.get_rect())
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2(winwidth/2, winheight/2)
        self.target = pygame.Vector2(winwidth/2, winheight/2)
        self.speed = speed

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length != 0:
            move.normalize_ip()
            move = move * min(move_length, self.speed)
            self.pos += move

        self.rect.center = self.pos

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 1000))
    pygame.display.set_caption("League Of Legends")
    clock = pygame.time.Clock()

    group = pygame.sprite.Group(Player(6, pygame.Color('purple')))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ship in group.sprites():
                    ship.target = pygame.mouse.get_pos()

        group.update()
        screen.fill('dark green')
        group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
