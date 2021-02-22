import os
import sys

import pygame
import requests

i = 0
maps = []

a, b, c, d = 10, 10, 10, 10

map_request = [f"http://static-maps.yandex.ru/1.x/?ll={a},{b}&spn={c},{d}&l=map"]

pygame.init()
screen = pygame.display.set_mode((600, 450))

running = True

while running:
    response = requests.get(map_request[i])

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
pygame.quit()

os.remove(map_file)
