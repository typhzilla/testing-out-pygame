import pygame
#import random

#window stuff
WIDTH, HEIGHT = int(640*1.5), int(360*1.5) #calkulaytor skilzz
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bittyproto!")

#text shit
pygame.font.init()

white = pygame.color.Color('#ffffff')
black = pygame.color.Color('#000000')
font = pygame.font.Font('asset/Cascadia.ttf', 12)

#time/fps stuff
clock = pygame.time.Clock()
FPS = 60

def fpsCounter():
	clock.tick(FPS)
	display = font.render('fps: ' + str(float(round(clock.get_fps(), 2))), False, white)
	WIN.blit(display, (0, 0))
	pygame.display.update()

"""###################
VISUAL SHIT (PROBABLY)
###################"""

def messageBox(character, text):
	#todo Eventually(TM)
	pass

"""
character stuff, redoing it again because i dont want it to redraw all the fucking time
shit looks like if you were to paste an image and use it as a brush in mspaint if you 
know what i mean lol

NVM IM SO FUCKING STUPID, I HAD TO ADD A BG
i really should stop skipping over steps in tutorials that i think arent important :ratchet:
"""

posX = 130
posY = 300
#angle = 0

SPEED = 5
ACCEL = 2

WHITEBOX_SPRITE = pygame.image.load("asset/char/no_tex.png")
WHITEBOX_WIDTH, WHITEBOX_HEIGHT = 30, 30

def drawPlayerCharacter(x, y):
	#placeholder shit, ill make actual sprites eventually lol
	global WHITEBOX_SPRITE

	WIN.blit(WHITEBOX_SPRITE, (x, y))

	pygame.display.update()

#the actual game loop so it can run
def main():
	global posX
	global posY
	global angle

	xIn = 1

	run = True
	while run:
		WIN.fill(black)	
		fpsCounter()
		drawPlayerCharacter(posX, posY)
		
		"""
		posX += 3*xIn
		if posX >= 800:
			xIn = -1
		if posX <= 120:
			xIn = 1
		"""

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False	

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_LEFT]:
			posX -= SPEED
			print ("moved right")
		if keys_pressed[pygame.K_RIGHT]:
			posX += SPEED
			print ("moved left")

			"""
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pygame.key.set_repeat(0)
					posX -= 10
					print ("moved left")
				elif event.key == pygame.K_RIGHT:
					posX += 10
					print ("moved right")	
			"""
	pygame.quit()

if __name__ == "__main__":
	main()