import pygame

def dibujarCuadrado(x, y, w, h, gameDisplay, color=None):
    s = pygame.Surface((w, h))
    s.fill(color)
    gameDisplay.blit(s, (x, y))

def boton(x, y, w, h, inactive_color, active_color,  msg='', font_size=20, action=None, parameters=[]):
    """
    Función para crear un botón
    Parámetros
    ----------
    int x: posición x del botón
    int y: posición y del botón 
    int w: ancho del botón
    int h: alto del botón
    tupple inactive_color: color del botón cuando no tiene el cursor encima
    tupple active_color: color del botón cuando tiene el cursor encima
    str msg: Mensaje del botón | default=None
    int font_size: tamaño del texto en el botón | default=20
    function action: función que va a realizar el botón | default=None
    array parameters: parametrós para la función del botón | default=[]
    """

    # Posición del cursor
    mouse = pygame.mouse.get_pos()
    # Dice si el boton ha sido presionado o no
    click = pygame.mouse.get_pressed()

    dibujarCuadrado(x - 3, y - 3, w + 6, h + 6, negro)
     
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        # Si el cursor está encima del botón, cambia a su color activo (ac)
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        # Comprueba si el botón fue presionado y posee alguna opción
        if click[0] == 1 and action != None:
            if parameters:
                action(parameters[0])
            else:
                action()
    else:
        # Dibuja el botón con su color inactivo
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # Fuente y tamano del texto del botón
    textButton = pygame.font.Font('freesansbold.ttf', fuenteTam)
    TextSurf, TextRect = text_objects(msg, textButton)
    # Posicionando el botón
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    # Poniendo el botón en pantalla
    gameDisplay.blit(TextSurf, TextRect)