import pygame

black = (0,0,0)
white = (255,255,255)
'''
to call the function provide it with a mesasge, x coordinate, y coordinate, width, height
initial color, alternate color and the function it should call if clicked
the last is not reuired as nothing will happen by default. When passing a function to be called by this
look to one of the buttons as an example. Don't include the () as it will try to run the code each time 
the button is written to the screen i beliueve or it will at best crash the code
This gets called throughout this file and others so its just copied to the other files, might end up moving
most of the graphics to its own file to keep it centralized but thats not a priority a the moment
'''
def button(gameDisplay,msg,x,y,w,h,ic,ac,action=None,arg=None):
	mouse = pygame.mouse.get_pos()					#gets the postion of the mouse on the menu
	click = pygame.mouse.get_pressed()				#gets wether not the mouse is clicked or not
	if x+w > mouse[0] > x and y+h > mouse[1] > y:	#if the mouse is within the buttons perimeter
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))	#display the alternate color

		if click[0] == 1:		#if you click while on the button do the action
			if arg == None:		
				action()
			else:
				action(arg) 
	else:					
		pygame.draw.rect(gameDisplay, ic,(x,y,w,h))	#otherwise do nothing and leave the inital color

	smallText = pygame.font.SysFont("stencilStd",20)	#defines the font, fuckign comicasns man
	textSurf, textRect = text_objects(msg, smallText)	#textsurface and textrectangle
	textRect.center = ( (x+(w/2)), (y+(h/2)) )			#centers the text
	gameDisplay.blit(textSurf, textRect)				#adds the surface and rectangle to the display

#--------------------------------------------------------------------------

#w and h must be of the image itself, make sure the images are the same size
#img = pygame.image.load('GRAPHICS\\submit_neutral.png')
#ic and hc are images 

def button_image(gameDisplay,msg,x,y,w,h,ic,ac,action=None,arg=None,font="arial",point=20,color=white):
	mouse = pygame.mouse.get_pos()					
	click = pygame.mouse.get_pressed()				
	if x+w > mouse[0] > x and y+h > mouse[1] > y:	
		gameDisplay.blit(ac,(x,y))	

		if click[0] == 1:
			if arg == None:		
				action()
			else:
				action(arg)         
	else:					
		gameDisplay.blit(ic,(x,y))

	smallText = pygame.font.SysFont(font,point)
	textSurf, textRect = text_objects(msg, smallText,color)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

#--------------------------------------------------------------------------

def print_text(gameDisplay,msg,font,point,color,location):
	text = pygame.font.SysFont(font,point)
	renderText = text.render(msg,False,color)
	gameDisplay.blit(renderText,location)
'''
sets center between xleft and xright
					ybot  and ytop
'''
def print_text_center(gameDisplay,msg,font,point,color,xr,xl,yb,yt):
	font = pygame.font.SysFont(font,point)
	text = font.render(msg,True,color)
	text_rect = text.get_rect(center=((xr-xl)/2,(yb-yt)/2))
	gameDisplay.blit(text,text_rect)