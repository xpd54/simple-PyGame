import pygame,sys,time,math,os,random
from pygame.locals import *
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
windowsWidth=700
windowsHeight=500
DISPLAYSURF=pygame.display.set_mode((windowsWidth,windowsHeight),0,32)
pygame.display.set_caption("boom")
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
WHITE=(255,255,255)
greenBall=pygame.image.load('image/green.png')
blueBall=pygame.image.load('image/blue.png')
blastShow=pygame.image.load('image/firework.png')
fireSound = pygame.mixer.Sound('music/fire.wav')
pygame.mixer.music.load('music/theme.mp3')
flip=True
x=0
vi=30
pygame.mixer.music.play(-1, 0.0)

flag1=False
flag2=False
y0=0
cnt=0
def throughBall(colorBall,x,y0):
	y=windowsHeight-(y0+round((x*math.tan(math.pi/4)-5*(x/(vi*math.cos(math.pi/4)))**2)))
	if y>=25:	
		if flag1==False:
			DISPLAYSURF.blit(colorBall,(x,y))
	if mouseClicked and flag1==False:
		if (x<mousex and x+48>mousex) and (y<mousey and y+48>mousey):
			fireSound.play()
			DISPLAYSURF.fill(WHITE)
			DISPLAYSURF.blit(blastShow,(x,y))
			flag1=True
			cnt+=5
			#DISPLAYSURF.blit(blastShow,(x,y))	
			DISPLAYSURF.blit(blueBall,(windowsWidth-x,y))
			pygame.display.update()
			#time.sleep(2)
			
	if x>windowsWidth or y>windowsHeight or y<25:
		x=0
		vi=random.randint(30,400)
		y0=random.randint(0,250)	
		flag1=False
	x+=5

while True:
		
	mouseClicked = False
	DISPLAYSURF.fill(WHITE)
	fob=pygame.font.Font('freesansbold.ttf',20)
	tob=fob.render('Score='+str(cnt),True,(255,0,0),(0,0,0))
	tob1=tob.get_rect()
	y=windowsHeight-(y0+round((x*math.tan(math.pi/4)-5*(x/(vi*math.cos(math.pi/4)))**2)))
	if y>=25:	
		if flag1==False:
			DISPLAYSURF.blit(greenBall,(x,y))
		DISPLAYSURF.blit(blueBall,(windowsWidth-x,y))
	#pygame.draw.rect(DISPLAYSURF,(0,0,0),(0,0,windowsWidth,25))
	DISPLAYSURF.blit(tob,(0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex,mousey=event.pos
		elif event.type == MOUSEBUTTONUP:
			mousex,mousey=event.pos
			mouseClicked = True
	if mouseClicked and flag1==False:
		if (x<mousex and x+48>mousex) and (y<mousey and y+48>mousey):
			fireSound.play()
			DISPLAYSURF.fill(WHITE)
			DISPLAYSURF.blit(blastShow,(x,y))
			flag1=True
			cnt+=5
			#DISPLAYSURF.blit(blastShow,(x,y))	
			DISPLAYSURF.blit(blueBall,(windowsWidth-x,y))
			pygame.display.update()
			#time.sleep(2)
			
	if x>windowsWidth or y>windowsHeight or y<25:
		x=0
		vi=random.randint(30,400)
		y0=random.randint(0,250)	
		flag1=False
	x+=5
	pygame.display.update()
	fpsClock.tick(FPS)
