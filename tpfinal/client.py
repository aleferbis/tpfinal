import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win,player, player2):
    """
        Dibuja y actualiza todos los elementos de la ventana del juego para un frame.

        Esta función se encarga de:
            - Limpiar la pantalla estableciendo un fondo blanco.
            - Dibujar al jugador local (`player`) y al jugador remoto (`player2`) en sus posiciones actuales.
            - Actualizar la ventana para que los cambios sean visibles en pantalla.

        Args:
            win (pygame.Surface): La superficie principal de Pygame donde se dibuja el juego.
            player (Player): Objeto Player que representa al jugador 1.
            player2 (Player): Objeto Player que representa al jugador 2.

        Returns:
            None
        """
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()