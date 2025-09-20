import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        """
                Dibuja el jugador en la ventana de Pygame.

                Args:
                    win (pygame.Surface): Superficie donde se dibuja el jugador.

                Returns:
                    None
                """
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """
                Actualiza la posición del jugador según las teclas presionadas.

                Teclas controladas:
                    - Flecha izquierda: mover a la izquierda.
                    - Flecha derecha: mover a la derecha.
                    - Flecha arriba: mover hacia arriba.
                    - Flecha abajo: mover hacia abajo.

                Llama a `update()` para actualizar el rectángulo del jugador.

                Returns:
                    None
                """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        """
                Actualiza el rectángulo que representa la posición y tamaño del jugador.

                Esto permite que el dibujo se mantenga
                sincronizado con la posición actual del jugador.

                Returns:
                    None
                """
        self.rect = (self.x, self.y, self.width, self.height)