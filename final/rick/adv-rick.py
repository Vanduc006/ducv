import pygame, sys


# Tạo khung cho App
pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Rick app")
# lấy ảnh 
# nút nà
button = pygame.image.load('button2.png').convert()
button = pygame.transform.scale2x(button)
#nền nà
bg = pygame.image.load('unnamed.png').convert()
bg = pygame.transform.scale2x(bg)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		

				
		screen.blit(bg,(0,0))
		screen.blit(button,(150,150))
		pygame.display.update()
		clock.tick(120)