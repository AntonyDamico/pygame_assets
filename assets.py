# pylint: disable=E1101
# pylint: disable=E1121
import pygame
from . import colors

def text_objects(text, font, font_color=colors.NEGRO, font_size=20):
    """
    Función para crear ojetos de texto en pygame
    Parámetros
    ----------
    str text: texto que se le va a poner al objeto
    str font: fuente para el texto
    tupple font_color: color para el texto | default=colors.Negro (0,0,0)
    font_size: tamaño de la fuente | default=20
    """
    custom_text = pygame.font.Font(font, font_size)
    text_surface = custom_text.render(text, True, font_color)
    return text_surface, text_surface.get_rect()

def draw_square(game_display, x, y, w, h, color=None):
    s = pygame.Surface((w, h))
    s.fill(color)
    game_display.blit(s, (x, y))

def print_text(game_display, text, x, y, font_size=25, font_color=colors.NEGRO):
    """
    Imprime un texto en la pantalla dada una posición

    Parámetros
    ----------
    str texto: Texto que se desea imprimir
    int x: posición x del texto
    int y: posición y del texo
    """
    font = pygame.font.SysFont(None, font_size)
    custom_text = font.render(text, True, font_color)
    game_display.blit(custom_text, (x, y))

def imprimir_imagen(gameDisplay, x, y, img):
    """
    Imprime una imágen en la pantalla dada una posición

    Parámetros
    ----------
    object game_display: objeto de display de pygame - pygame.display.set_mode((w, h))
    int x: posición x de la imagen
    int y: posición y de la imagen
    str img: ruta a la imágen
    """
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))

def boton(game_display, x, y, w, h, inactive_color, active_color,  text='', text_color=colors.NEGRO, font='freesansbold.ttf', font_size=20, action=None, parameters=[]):
    """
    Función para crear un botón
    Parámetros
    ----------
    object game_display: objeto de display de pygame - pygame.display.set_mode((w, h))
    int x: posición x del botón
    int y: posición y del botón 
    int w: ancho del botón
    int h: alto del botón
    tupple inactive_color: color del botón cuando no tiene el cursor encima
    tupple active_color: color del botón cuando tiene el cursor encima
    str text: Mensaje del botón | default=None
    tupple text_color: color del texto del botón | default=colors.Negro = (0,0,0)
    int font_size: tamaño del texto en el botón | default=20
    function action: función que va a realizar el botón | default=None
    array parameters: parametrós para la función del botón | default=[]
    """

    # Posición del cursor
    mouse = pygame.mouse.get_pos()
    # Dice si el boton ha sido presionado o no
    click = pygame.mouse.get_pressed()
     
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        # Si el cursor está encima del botón, cambia a su color activo
        pygame.draw.rect(game_display, active_color, (x, y, w, h))
        # Comprueba si el botón fue presionado y posee alguna acción
        if click[0] == 1 and action != None:
            if parameters:
                action(parameters[0])
            else:
                action()
    else:
        # Dibuja el botón con su color inactivo
        pygame.draw.rect(game_display, inactive_color, (x, y, w, h))

    # Fuente y tamano del texto del botón
    text_surface, text_rectangle = text_objects(text, font, font_color=text_color, font_size=font_size)
    # Posicionando el botón
    text_rectangle.center = ((x+(w/2)), (y+(h/2)))
    # Poniendo el botón en pantalla
    game_display.blit(text_surface, text_rectangle)