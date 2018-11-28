import pygame
import sys
import random
from random import randint

black = (0,0,0)
nodeDefault = (0,0,128)
nodeActive = (0,0,255)
lineActive = (255,0,0)
class Node:
	def __init__(self,xPos,yPos,id):
		self.id = -1
		self.x = xPos
		self.y = yPos
		self.neighbors = []
		
	
	



if __name__ == "__main__":
	allNodes = []
	amt_of_neighbors = 4
	
	for i in range(800):
		node = Node(id = i, xPos = randint(20,880), yPos = randint(20,580))
		allNodes.append(node)
	for node in allNodes:
		for n in range(amt_of_neighbors):
			node.neighbors.append(randint(0,799));
	
	pygame.init()
	vis = pygame.display.set_mode((900,600))
	vis.fill((255,255,255))
	pygame.display.update()
	#draw lines
	for node in allNodes:
		for neighbor in node.neighbors:
			pygame.draw.lines(vis, black, False, [(node.x, node.y),(allNodes[neighbor].x,allNodes[neighbor].y)],1)
	#draw nodes
	for node in allNodes:
		pygame.draw.circle(vis, nodeDefault,(node.x,node.y),8,0)
	pygame.display.update()
	while(True): #we can put all the simulation actions in here
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit(); sys.exit();
