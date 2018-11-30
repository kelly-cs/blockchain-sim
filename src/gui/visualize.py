import pygame
import sys
import random
from random import randint

black = (0,0,0)
nodeDefault = (0,0,128)
nodeActive = (0,255,0)
lineActive = (255,0,0)
allNodes = []

class Node:
    def __init__(self,xPos,yPos,id):
        self.id = id
        self.x = xPos
        self.y = yPos
        self.neighbors = []

def drawAllNodes():
        for node in allNodes:
                for neighbor in node.neighbors:
                        pygame.draw.lines(vis, black, False, [(node.x, node.y),(allNodes[neighbor].x,allNodes[neighbor].y)],1)
        for node in allNodes:
                pygame.draw.circle(vis, nodeDefault,(node.x,node.y),8,0)

def highlightConnection(fromNodeID,toNodeID):
        fromNode = allNodes[fromNodeID]
        if toNodeID == -1:
                toNode = allNodes[fromNode.neighbors[randint(0,3)]]
        else:
                toNode = allNodes[toNodeID]                        
        pygame.draw.lines(vis, lineActive, False, [(fromNode.x,fromNode.y),(toNode.x,toNode.y)],2)
        pygame.draw.circle(vis, nodeActive, (fromNode.x, fromNode.y),8,0)
        pygame.draw.circle(vis, nodeActive, (toNode.x, toNode.y),8,0)


if __name__ == "__main__":
        amt_of_neighbors = 4
        for i in range(800):
                #print(i)
                node = Node(id = i, xPos = randint(10,1590), yPos = randint(10,890))
                allNodes.append(node)
                #print(str(node.id)+" "+str(node.x)+" "+str(node.y)+"\n")
        for node in allNodes:
                for n in range(amt_of_neighbors):
                        node.neighbors.append(randint(0,799));
        pygame.init()
        vis = pygame.display.set_mode((1600,900))
        vis.fill((255,255,255))
        pygame.display.update()
        drawAllNodes()
        highlightConnection(642,-1)
        pygame.display.update()
        
        while(True): #we can put all the simulation actions in here
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit(); sys.exit();
                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_a:
                                        print("highlighting...")
                                        highlightConnection(randint(0,799),-1)
                                        pygame.display.update()
                                elif event.key == pygame.K_w:
                                        print('clearing...')
                                        vis.fill((255,255,255))
                                        drawAllNodes()
                                        pygame.display.update()
