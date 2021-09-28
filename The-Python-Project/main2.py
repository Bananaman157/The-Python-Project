import pygame
import sys

sys.path.insert(0, '/home/ascte/.local/lib/python3.8/site-packages')
import youtube_dl

import pafy 
import vlc
from playsound import playsound
from pygame import mixer


pygame.init()
playlist=[]


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

def get_songs():
    length=int(input("how many?"))
    global playlist
    
    for i in range(length):
        song=input("what file?")
        playlist.append(song)

        


def play_songs():
    
    for event in pygame.event.get():
 

        if event.type == pygame.KEYDOWN:
            play=True
            if event.key == pygame.K_0:
                playsound(f"/home/ascte/Downloads/Music/{playlist[0]}")
        
            if event.key == pygame.K_1:
                playsound(f"/home/ascte/Downloads/Music/{playlist[1]}")
            if event.key == pygame.K_2:
                playsound(f"/home/ascte/Downloads/Music/{playlist[2]}")
        
            if event.key == pygame.K_3:
                playsound(f"/home/ascte/Downloads/Music/{playlist[3]}")
            if event.key == pygame.K_4:
                playsound(f"/home/ascte/Downloads/Music/{playlist[4]}")
            if event.key == pygame.K_5:
                playsound(f"/home/ascte/Downloads/Music/{playlist[5]}")
            if event.key == pygame.K_6:
                playsound(f"/home/ascte/Downloads/Music/{playlist[6]}")
            if event.key == pygame.K_7:
                playsound(f"/home/ascte/Downloads/Music/{playlist[7]}")
            if event.key == pygame.K_8:
                playsound(f"/home/ascte/Downloads/Music/{playlist[8]}")
            if event.key == pygame.K_9:
                playsound(f"/home/ascte/Downloads/Music/{playlist[9]}")

        

get_songs()
print(playlist)
screen.fill(bg)
pygame.draw.rect(screen, [214,214,255], button)
screen.blit(Text, (width+25, height+50))

while running == True:
    mixer.init
    
    play_songs()
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
            
            playsound(f"/home/ascte/Downloads/Music/Dababy.mp3")

    
            

            
            
    
    

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit




    
    #screen.fill((214,214,255))
    #pygame.display.flip()


