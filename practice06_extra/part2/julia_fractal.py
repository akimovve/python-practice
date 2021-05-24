import pygame

pygame.init()

sc = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Множества Жюлиа')
sc.fill((0, 0, 0))

space = 200  # Область рисования
scale = space / 2  # Масштабный коэффициент
num = 100  # Число итераций для проверки принадлежности к множеству Жюлиа


def func(z):
    return z ** 2 - complex(0.8, 0.156)


for y in range(-space, space):
    for x in range(-space, space):
        a = x / scale  # Действительная часть
        b = y / scale  # Мнимая часть
        z = complex(a, b)

        counter = 0
        for counter in range(100):
            z = func(z)
            if abs(z) > 2:
                break

        if counter == num - 1:
            r = g = b = 255
        else:
            r = (counter % 2) * 32 + 220
            g = (counter % 2) * 16 + 136
            b = counter % 6

        pygame.draw.circle(sc, (r, g, b), (x + space, y + space), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
