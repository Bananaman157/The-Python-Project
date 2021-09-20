import yaml
import pygame
##sets the size of the screen
screen = pygame.display.set_mode([500,500])



running = True
while running:



##Makes it where if you press x it colses the tab
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   #changes color of the screen 
    screen.fill((35, 39, 42))
    
    #makes the play button
    pygame.draw.circle(screen, (201,214,255),(250,400),35)
    

    #displays the colors    
    pygame.display.flip()
    
