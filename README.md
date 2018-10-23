# pygame_assets
Clase para facilitar el uso de elementos comunes de pygame y mantener código limpio, posee métodos para crear botones, texto, rectángulos, etc.

### Requisitos
* [python 3](https://www.python.org/) 
* [pygame](https://www.pygame.org/) - pip install pygame
* opcional [git](https://git-scm.com) - para trabajar con el repositorio 

## Instalación
Primero se debe clonar el repositorio para tener el código, teniendo instalado git, ingresa en el command line o cmd
```
git clone https://github.com/AntonyDamico/pygame_assets
```

Luego se debe colocar el directorio de assets en el del proyecto

```bash
├── proyecto
│   ├── assets
│   │   ├── __init.py__
│   │   ├── assets.py
│   │   ├── colors.py
│   └── Archivos del proyecto
```

Una vez cumplido esto se puede importar los archivos en el proyecto y usarlos libremente
```
from assets import colors
from assets.AssetsManager import AssetsManager

ancho_pantalla = 1000
alto_pantalla = 500
titulo = 'nueva ventana'
color_fondo = colors.NEGRO

assets = AssetsManager(ancho_pantalla, alto_pantalla, titulo, color_fondo)
assets.draw_square(20, 20, 50, 60, color=colors.AZUL)
```

### Ejemplo:
El ejemplo en el archivo example.py muestra como puede ser usada la libreria, ahí se utilizan
los métodos para imprimir texto, botones y cuadrados, además, cómo se deben manejar las funciones de los botones.
Para ejecutar el ejemplo simplemente puedes usar python en el command line al clonar el repositorio
```
python example.py
```

## Uso
### Métodos:
* constructor
```
Constructor de la clase

    Parámetros
    ----------
    int w_screen: ancho de la pantalla
    int h_screen: alto de la pantalla
    str title: título de la ventana de pygame | default=""
    tupple bg_color: color del fondo de la ventana | default=colors.BLANGO
```

* background_color()
```
Función para cambiar el color de fondo de pantalla

    Parámetros
    ----------
    tupple color: color del fondo de la ventana | default=colors.BLANGO
```

* draw_square()
```
Imprime un rectángulo en la pantalla dada una posición y tamaño

    Parámetros
    ----------
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

* draw_circle()
```
Imprime un circulo a la pantalla

    Parámetros
    ----------
    int x: posición x del círculo
    int y: posición y del círculo
    int radius: radio del círculo
    tupple color: color del círculo | default=color.NEGRO
    int w: cantidad de relleno del círculo, dejar en 0 para que esté relleno completamente
```

* draw_line()
```
Imprime una línea a la pantalla

    Parámetros
    ----------
    int initial_x: posición inicial en x
    int initial_y: posición inicial en y
    int final_x: posición final en x
    int final_y: posición final en y
    tupple color: color de la línea | default=color.NEGRO
    int w: grosor de la línea | default=1
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
    int x: posición x de la imagen
    int y: posición y de la imagen
    str img: ruta a la imágen
```

* button()
```
Función para crear un botón

    Parámetros
    ----------
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
