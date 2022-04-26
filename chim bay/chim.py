import pygame, sys, random
from tkinter import  messagebox

# nhắc nhở đầu
messagebox.showinfo(title="nhắc nhở nhẹ",
	
			message="chơi đừng có mà quạo nhá!!!!")
# tạo hàm game
def draw_floor():
	screen.blit(floor,(floor_x_pos,600))
	screen.blit(floor,(floor_x_pos+ 432,600))
def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop=(600,random_pipe_pos))	
	top_pipe = pipe_surface.get_rect(midtop=(600,random_pipe_pos-750))	
	return bottom_pipe , top_pipe
def move_pipe(pipes):
	for pipe in pipes :	
		pipe.centerx -= 5
	return pipes
def	draw_pipe(pipes):
	for pipe in pipes:
		if pipe.bottom >= 600:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)
def check_cllistion(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			tg_va_cham.play()
			return False
	if bird_rect.top <= -75 or bird_rect.bottom >= 650:	
		return False
	return True	
def rotate_bird(bird1):
	new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
	return new_bird
def bird_animation():
	new_bird = bird_list[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
	return new_bird, new_bird_rect


def score_display(game_state):
	if game_state == 'main game':
		score_surface = game_font_2.render(str(int(score)),True,(0,51,102))	
		score_rect = score_surface.get_rect(center = (216,100))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font_2.render(str(f' {int(score)}'),True,(0,51,102))	
		score_rect = score_surface.get_rect(center = (216,100))
		screen.blit(score_surface,score_rect)	



# các TH xảy ra khi thua nà
		# nếu vào dđiẻm mà nằm trg này thì bật rick
		rick_num =[13,34,1,26,47,20,100,200,3,20,11,35,40]
		if score == rick_num:
			rick.play()
		if score >= 1 and score < 10 //True:
			high_score_surface = game_font.render(str(f'gà vãi'),True,(0,51,102))	
			high_score_rect = high_score_surface.get_rect(center = (216,500))
			screen.blit(high_score_surface,high_score_rect)
		if score >= 11 and score < 15 //True:
			high_score_surface = game_font.render(str(f'wtf,vẫn gà'),True,(0,51,102))	
			high_score_rect = high_score_surface.get_rect(center = (216,500))
			screen.blit(high_score_surface,high_score_rect)	
		if score >= 16 and score < 29 //True:
			high_score_surface = game_font.render(str(f'play more??'),True,(0,51,102))	
			high_score_rect = high_score_surface.get_rect(center = (216,500))
			screen.blit(high_score_surface,high_score_rect)			
		if score >= 30  and score < 69 //True:
			high_score_surface = game_font.render(str(f'good job'),True,(0,51,102))	
			high_score_rect = high_score_surface.get_rect(center = (216,500))
			screen.blit(high_score_surface,high_score_rect)			

		if score >= 70 //True:
			high_score_surface = game_font.render(str(f'Pro player!!'),True,(0,51,102))	
			high_score_rect = high_score_surface.get_rect(center = (216,500))
			screen.blit(high_score_surface,high_score_rect)
		if score > 1000 // True:
			bg2 = pygame.image.load('assets/nen4.png').convert()
			bg2 = pygame.transform.scale2x(bg2)	
			screen.blit(bg2,(0,0))
		return	
			
	
# tạo khung cho game
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
pygame.display.set_caption("CHIMBAY !!! MADE BY VDUC")
game_font = pygame.font.Font('game font.ttf',40)
game_font_2 = pygame.font.Font('04B_19.TTF', 60)
# tạo biến game
gravity = 0.25
bird_movement = 0
game_active = False
score = 0
high_score = 0
#hình nền nà

bg = pygame.image.load('assets/nen.png').convert()
bg = pygame.transform.scale2x(bg)
# đất nà
floor = pygame.image.load('assets/dat.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# chim nà
# chim bình thường
bird_bthg = pygame.image.load('assets/chim_bthg.png').convert_alpha()
bird_bthg = pygame.transform.scale2x(bird_bthg)
# chim bay
bird_len = pygame.image.load('assets/chim bay.png').convert_alpha()
bird_len = pygame.transform.scale2x(bird_len)
# chim xuống
bird_xuong = pygame.image.load('assets/chim ha.png').convert_alpha()
bird_xuong = pygame.transform.scale2x(bird_xuong)
# danh sách chim
bird_list = [bird_xuong,bird_bthg,bird_len] # 0 1 2
bird_index = 0
bird = bird_list[bird_index]
# Hình chũw nhật quanh con chim
bird_rect = bird.get_rect(center = (100,384))
# TẠO TIME CHO CON CHIM
bird_flap =pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap,200)
#  ống nà
pipe_surface = pygame.image.load('assets/ong.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# tao time lấy ống
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1000)
pipe_height = [300,400,500,350,450,520,410,310,320,430]
# màn hình thua
game_over_surface = pygame.image.load('assets/thua.png').convert()
game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_rect = game_over_surface.get_rect(center = (216,384))

#chèn âm thanh
tg_vo = pygame.mixer.Sound('sound/sfx_wing.wav')
tg_va_cham = pygame.mixer.Sound('sound/punch.webm')
bye  =	pygame.mixer.Sound('sound/bai.wav')
#troll
rick = pygame.mixer.Sound('sound/rick.mp3')
# loop cho game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if	event.type == pygame.KEYDOWN:
			if event.key == pygame.K_g :
				bird_movement = 0
				bird_movement = -8
				tg_vo.play()
			if event.key == pygame.K_g  and game_active == False:	
				game_active = True
				pipe_list.clear()	
				bird_rect.center = (100,384)
				bird_movement = 0	
				score = 0
			if event.key == pygame.K_m:
				score += 10		
				bird_movement = 0
				bird_movement = -8
			if event.key == pygame.K_q:
				bird_movement = 0
				bird_movement = -50

				

			if event.key == pygame.K_p:
				bye.play(3)
				pygame.quit()
				sys.exit()
				
				
		if event.type == spawnpipe :
			pipe_list.extend(create_pipe())	
		if event.type == bird_flap:
			if bird_index <	2:
				bird_index += 1	
			else:
				bird_index = 0
			bird,bird_rect = bird_animation()

						
	screen.blit(bg,(0,0))
	
	if game_active:
		# chim
		bird_movement += gravity
		rotated_bird = rotate_bird(bird)
		bird_rect.centery += bird_movement 
		screen.blit(rotated_bird, bird_rect)
		game_active = check_cllistion(pipe_list)

		# ống
		pipe_list = move_pipe(pipe_list)
		draw_pipe(pipe_list)
		# tăng điẻm theo tg
		score += 0.01
# hiển thi điẻm nà
		
		score_display('main game')
	else:
		screen.blit(game_over_surface,game_over_rect)
		score_display('game_over')
		# hiển thị điẻm cao nà	

	# dất
	floor_x_pos -=1
	draw_floor()
	if floor_x_pos <= -432:
		floor_x_pos = 0		
		screen.blit(floor,(floor_x_pos,600))	


	pygame.display.update()
	clock.tick(120)
