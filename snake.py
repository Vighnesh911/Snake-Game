#1.create a screen-bgcolor,display,width,height
#2.create a snake-moving controls like ip,down,left,right
#3.game over when touch boundries

import pygame
import time
import random

pygame.init()

#Placing colours
white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)

#display size
dis_width=700
dis_height=500


#Creating a caption for game 
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake Game')
clock=pygame.time.Clock()

snake_block=10#size of snake
snake_speed=15#speed of snake

#Creating font sizes 
font_style=pygame.font.SysFont('impact',25)
score_font=pygame.font.SysFont('impact',20)


#creating the score board
def your_score(score):
	value=score_font.render('score:'+ str(score),True,black)
	dis.blit(value,[0,0])#position of the score


#Creating a snake
def our_snake(snake_block,snake_list):
	for x in snake_list:
		pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])


#Creating a message box for player win/lose
def message(msg,color):
	mesg=font_style.render(msg,True,color)
	dis.blit(mesg,[dis_width/8,dis_height/2.5])


#Creating loop for game
#Game Start

def gameLoop():
	game_over=False
	game_close=False

	#here x1 and y1 are the snake head position
	x1=dis_width/2
	y1=dis_height/2

	#initially both set are zero it means snake dosent move until we press a key
	x1_change=0
	y1_change=0

	
	snake_list=[]
	snake_len=1

	#Creating the snake food randomly
	foodx=round(random.randrange(0,dis_width - snake_block)/10.0)*10.0
	foody=round(random.randrange(0,dis_height - snake_block)/10.0)*10.0


	#if game is not over
	while not game_over:

		while game_close ==True:
			dis.fill(blue)
			lost='you lost the game press C to play again or Q to Quit'
			message(lost,red)
			your_score(snake_len-1)
			pygame.display.update()

			#Condition for either to run or Quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_close=False
					game_over=True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over=True
						game_close=False
					if event.key == pygame.K_c:
						gameLoop()

		
		#Creating keys(left,right,up,dowm) to move snake
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_close=False
				game_over=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and x1_change==0:
					x1_change= -snake_block
					y1_change= 0

				elif event.key == pygame.K_RIGHT and x1_change==0:
					x1_change= snake_block
					y1_change= 0

				elif event.key ==pygame.K_UP and y1_change==0:
					y1_change= -snake_block
					x1_change= 0

				elif event.key == pygame.K_DOWN and y1_change==0:
					y1_change= snake_block
					x1_change = 0

    
    	#if the snake hit the boundry game will close
		if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
			game_close=True
		
		#here x1 is the snake head 
		x1=x1+x1_change
		y1=y1+y1_change
		dis.fill(blue)

		#he food is in green color rectangle placed b/w the following x,y axis same as a snake_block size
	
		pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])			
	
		#Creating an array(HEAD) appending the x1 values to head
		snake_Head = []
		snake_Head.append(x1)#increasing snake on x-axis
		snake_Head.append(y1)#increasing snake on y-axis
	
		#Append the snake_Head to the snake_list
		snake_list.append(snake_Head)
		if len(snake_list) > snake_len:
			del snake_list[0]


		

		#here we calling the function we created in the starting
		our_snake(snake_block,snake_list)
		your_score(snake_len-1)

		pygame.display.update()


		if x1 == foodx and y1 == foody:
			foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
			foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
			snake_len=snake_len+1

		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameLoop()














    
