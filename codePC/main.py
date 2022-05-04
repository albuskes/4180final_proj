import pygame
from pygame import mixer 
import math
import random 
import os
from tcpcom import TCPClient
import time
import socket
import threading
import serial

cord = [400,480]

shootList = []
shootBool = False
shoot = False

mod = 0
# ----------- Networking Stuff -----------------




try:
	IP_ADDRESS = socket.gethostbyname('raspberrypi')
	print(IP_ADDRESS)
	IP_PORT = 22000
except:
	pass

def onStateChanged(state, msg):
	global cord
	global isConnected
	if state == "CONNECTING":
		print ("Client:-- Waiting for connection...")
	elif state == "CONNECTED":
		print ("Client:-- Connection estabished.")
	elif state == "DISCONNECTED":
		print ("Client:-- Connection lost.")
		isConnected = False
	elif state == "MESSAGE":
	

		try:
			cord = msg.split(",")
		except:
			pass
		
		
		
try:
	client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged)
	rc = client.connect()
except:
	rc = NULL
	pass

# ----------- Networking Stuff Completed-----------------




# ------ Mbed Accelerometer Stuff ----------------

def toShoot(rawInput):
	"""
	Determines the value of shoot off of mbedInput
	Input: 
	rawInput (bytes[]) : the raw bytes sent from mbed
	"""
	strInput = str(rawInput)
	shootChar = strInput[2]
	shoot = False
	if shootChar == "0":
		shoot = False
	elif(shootChar == "1"):
		shoot = True
	else:
		shoot = shoot
	return shoot

def serialInit():
	global shoot
	global ser
	shoot = False
	ser = serial.Serial()
	ser.timeout = 0.01
	ser.baudrate = 115200
	#ser.port = '/dev/tty.usbmodem1102'
	ser.port = 'COM8'
	ser.open()


# def serialThread():
# 	global shootBool
# 	while(1):
# 		rawInput = ser.readline()
# 		shootBool = toShoot(rawInput)
# 		print(shootBool)
def changeShootBool():
	global shootBool
	global shootList

	
	


	rawInput = ser.read(ser.in_waiting)	
	#rawInput = ser.read(1)

	
	#shootBool = toShoot(rawInput)
	
	'''
	shootList.append(toShoot(rawInput))
	
	
	if(len(shootList) == 3):
		#print(shootList)
		if(False in shootList):
			shootBool = False
		else:
			shootBool = True
		shootList = []
	
	
	
	'''
	

	

	shootBool = toShoot(rawInput)

	
	

def serialThreadRunner():
		serialInit()
		x = threading.Thread(target = serialThread(), args = (), daemon= True )
		x.start()

serialInit()

#---------Done with Serial Stuff-----------------
		


os.chdir(os.path.dirname(os.path.abspath(__file__)))


print(os.getcwd())
# Initializing pygame 
pygame.init()

change_bool = pygame.USEREVENT + 1

pygame.time.set_timer(change_bool, 25)

# Creating a screen 
screen = pygame.display.set_mode((800,600)) 

# Title and Logo 
pygame.display.set_caption("Space Buzzers") 
icon = pygame.image.load("spaceship.png") 
pygame.display.set_icon(icon)  

# Background 
background = pygame.image.load("background.png") 

#Background music 
mixer.music.load('background.wav') 
mixer.music.play(-1) 

# Player 
player_img = pygame.image.load("player.png")
playerX = 370
playerY =  480 
player_delX = 0 
player_delY = 0

def player(X,Y) :
	screen.blit(player_img,(X,Y))  

# Enemies 
num = 5
monster_img = [] 
monsterX = [] 
monsterY = [] 
monster_delX = []
monster_delY = []
for i in range(num) : 
	monster_img.append(pygame.image.load("monster1.png"))
	monsterX.append(random.randint(0,736)) 
	#monsterY.append(random.randint(50,175))
	monsterY.append(175)
	monster_delX.append(2) 
	monster_delY.append(0) 

def monster(img,X,Y) :
	screen.blit(img,(X,Y))


# Bullet 
bullet_img = pygame.image.load("bullet.png") 
bulletX = 0 
bulletY = 480 
bullet_delY = -10 
bullet_state = "ready"

def fire_bullet(X,Y) :  
	global bullet_state 
	bullet_state = "fire" 
	screen.blit(bullet_img,(X+15,Y+16)) 


# Function to check collision 
def collision(x1,y1,x2,y2) :
	dist = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2)) 
	if dist <= 27 : 
		return True 
	return False 


# Player Score 
player_score = 0
font1 = pygame.font.Font('freesansbold.ttf',32)

def show_score() : 
	score = font1.render("Score : "+str(player_score),True,(255,255,255)) 
	screen.blit(score,(10,10))

font2 = pygame.font.Font('freesansbold.ttf',64)
def game_over() :
	text1 = font2.render("GAME OVER",True,(255,255,255))
	text2 = font1.render("Your final score: "+str(player_score),True,(255,255,255))
	screen.blit(text1,(200,250)) 
	screen.blit(text2,(250,310)) 



# --- more networking stuff -- 

if rc:
	isConnected = True
	#print ("Client:-- Sending command: go...")
	client.sendMessage("go")
	#time.sleep(2)
else:
	print ("Client:-- Connection failed")

	#---- More networking stuff --- 

#serialThreadRunner()
# Game loop 




running  = True 
while running  : 
	start = time.time()
	
	changeShootBool()
	

	screen.fill((0,0,0)) 
	screen.blit(background,(0,0)) 

	

	

	
	for event in pygame.event.get() : 
		if event.type == pygame.QUIT : 
			running = False
			os._exit(1)
		
		if event.type == change_bool:
			if shootBool:
				if bullet_state == "ready" : 
					fire_sound = mixer.Sound('fire.wav') 
					fire_sound.play()
					bulletX = playerX
					bulletY = playerY
					fire_bullet(bulletX,bulletY)
			
		


	
	playerX = 800 - int( cord[0])
	playerY = int( cord[1])
	
	if playerX <= 0 :
		playerX = 0
	elif playerX >= 736 :
		playerX = 736

	# Monster movement
	for i in range(num) :
		if monsterY[i] >= 440 :
			for j in range(num) : 
				monsterY[j] = 1000
			game_over()
			break

		monsterX[i] += monster_delX[i]; 
		if monsterX[i] <= 0 : 
			monsterX[i] = 0 
			monster_delX[i] = 2
			monsterY[i] += monster_delY[i]
		elif monsterX[i] >= 736 : 
			monsterX[i] = 736 
			monster_delX[i] = -2
			monsterY[i] += monster_delY[i]


	
	if(bulletY <= 0) :
		bullet_state = "ready" 
		bulletY = 480 	
		bulletX = 0
	if bullet_state == "fire" : 
		fire_bullet(bulletX,bulletY)
		bulletY += bullet_delY 

	# Check Collision
	for i in range(num) :
		if collision(monsterX[i],monsterY[i],bulletX,bulletY) :
			explosion_sound = mixer.Sound('explosion.wav') 
			explosion_sound.play()
			bullet_state = "ready" 
			bulletY = 480
			bulletX = 0
			player_score += 1
			monsterX[i] = random.randint(0,736)
			monsterY[i] = random.randint(50,175)
	
	player(playerX,playerY)
	for i in range(num) :
		monster(monster_img[i],monsterX[i],monsterY[i])
	show_score()

	if(player_score > 10):
		game_over()


	
		
	
	
	

	pygame.display.update()

	












