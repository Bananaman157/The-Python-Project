import pygame
import sys

sys.path.insert(0, '/home/ascte/.local/lib/python3.8/site-packages')
import youtube_dl

import pafy 
import vlc
from playsound import playsound



pygame.init()


screen=pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
fps = 60
size = [200,200]
bg= [0,0,0]
height=150
width=150
Font = pygame.font.SysFont('freesansbold.ttf',50)
Text = Font.render("Meme", True, (255,255,255))
button = pygame.Rect(150,150,width,height)
dababy= pygame.image.load("dababy.png")
dababy= [pygame.transform.scale(dababy, (400,400))]
running=True

screen.fill(bg)

pygame.draw.rect(screen, [214,214,255], button)
screen.blit(Text, (width+25, height+50))

while running == True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False


    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos

        if button.collidepoint(mouse_pos):
            print('button was pressed at {0}'.format(mouse_pos))
            image=True
        
        if image==True:
            screen.blit(dababy[0],(0,0))
            pygame.display.flip()
            
            playsound("/home/ascte/Documents/GitHub/The-Python-Project/Dababy.mp3")
            
            
    
    

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit




    
    #screen.fill((214,214,255))
    #pygame.display.flip()


