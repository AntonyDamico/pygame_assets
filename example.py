# pylint: disable=E1101
import pygame
from assets import colors
from assets.AssetsManager import AssetsManager

pygame.init()
# Tamaño de la ventana
ancho_pantalla = 1000
alto_pantalla = 500

# Inicializando el assets manager
assets = AssetsManager(ancho_pantalla, alto_pantalla, 'Ejemplo')
clock = pygame.time.Clock()

# Cambiando el color de fondo a negro
assets.background_color(colors.NEGRO)

def mostrar_cuadrado(x, y):
    assets.draw_square(x, y, 200, 50, color=colors.ROJO)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        assets.print_text('Ejemplo', ancho_pantalla*0.40, alto_pantalla*0.20, font_size=50, font_color=colors.BLANCO)
        assets.print_text('Presionar botón para mostrar cuadrado', ancho_pantalla*0.30, alto_pantalla*0.30, font_size=30, font_color=colors.BLANCO)

        assets.button(250, 250, 100, 100, colors.GRIS, colors.AZUL, text='presionar', action=mostrar_cuadrado, args=[200, 400])

        pygame.display.update()
        clock.tick(15)


game_loop()