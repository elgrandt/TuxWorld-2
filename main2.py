import pygame
import gui
import iosys.events as iv

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode((800,600))
    EVENTS = iv()
    
    
    elementos = []
    
    texto = gui.text_input()
    texto.add_allowed_keys(gui.keyLetters, gui.letterCode)
    texto.set_background((255,255,255))
    texto.set_position((100,50))
    texto.set_alpha_states(0.9, 1)
    
    movil = gui.area_movil.area_movil()
    movil.set_surface_dimensions((500,300))
    movil.enableA(10)
    movil.enableB(10)
    movil.set_position((200,100))
    surface = pygame.image.load("gui/display.png")
    movil.set_surface(surface)
    
    
    #elementos.append(texto)
    elementos.append(movil)
    elementos.append(texto)

    on = True
    CLOCK = pygame.time.Clock()
    while on == True:
        SCREEN.fill((200,200,200))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                on = False
        EVENTS.update_mouse(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        EVENTS.update_keyboard(pygame.key.get_pressed())
       
        for x in range(len(elementos)):
            elementos[x].logic_update(EVENTS)
            elementos[x].graphic_update(SCREEN)
        
        CLOCK.tick(40)
        
        pygame.display.update()
if __name__ == "__main__":
    main()
