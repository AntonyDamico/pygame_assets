# pygame_assets
Esta es una colección de métodos creada para facilitar el uso de pygame y limpiar el código. Tiene métodos para crear rectangulos, texto, botones e imágenes.

## Instalación
Primero se debe clonar el repositorio para tener el código
```
git clone https://github.com/AntonyDamico/pygame_assets
```

Luego se debe colocar el directorio de pygame_assets en el del proyecto

```bash
├── proyecto
│   ├── pygame_assets
│   │   ├── __init.py__
│   │   ├── assets
│   │   ├── colors
│   └── Archivos del proyecto
```

Una vez cumplido esto se puede importar los archivos en el proyecto y usarlos libremente
```
from pygame_assets import assets, colors

assets.draw_square(20, 20, 50, 60, color=colors.NEGRO)
```

## Uso
### Métodos:
* draw_square()
```
Imprime un rectángulo en la pantalla dada una posición y tamaño

    Parámetros
    ----------
    object game_display: objeto de display de pygame - pygame.display.set_mode((w, h))
    int x: posición x del rectángulo
    int y: posición y del rectángulo
    int w: ancho del rectángulo
    int h: alto del rectángulo
    tupple color: color del rectángulo | default=None
```

* print_text()
```
Imprime un texto en la pantalla dada una posición

    Parámetros
    ----------
    str texto: Texto que se desea imprimir
    int x: posición x del texto
    int y: posición y del texo
```

* print_image()
```
    Imprime una imágen en la pantalla dada una posición

    Parámetros
    ----------
    object game_display: objeto de display de pygame - pygame.display.set_mode((w, h))
    int x: posición x de la imagen
    int y: posición y de la imagen
    str img: ruta a la imágen
```

* button()
```
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
```
