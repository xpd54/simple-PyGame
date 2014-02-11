import pygame,sys
from pygame.locals import *
import time
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Image")
WHITE=(255,255,255)
i=0
while True:
	DISPLAYSURF.fill(WHITE)
	if i==4:
		i=0
	i=i+1
	image='walk/walk'+str(i)+'.png'
	walk1=pygame.image.load(image)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.quit()
	DISPLAYSURF.blit(walk1,(170,30))
	time.sleep(0.5)
	pygame.display.update()
