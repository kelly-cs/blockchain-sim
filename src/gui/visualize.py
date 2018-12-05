#!/usr/bin/python3

import pygame
import random

COLOR_NODE_BLOCK_HIGH = (  0,   0, 255)
COLOR_NODE_BLOCK_LOW  = (255,   0,   0)
COLOR_NODE_ACTIVE = (  0, 255,   0)
COLOR_LINE_NORMAL = (  0,   0,   0)
COLOR_LINE_ACTIVE = (255,   0,   0)
COLOR_BG          = (255, 255, 255)
COLOR_PING        = (255,   0,   0)
COLOR_SEND_TRANSACTION = (255,   0, 255)

def _mapVal(progress, valFrom, valTo, castInt = False):
    if progress <= 0:
        return valFrom
    if progress >= 1:
        return valTo
    result = valFrom + ((valTo - valFrom) * progress)
    if castInt:
        result = int(round(result))
    return result

def _mapTuple2(progress, tupleFrom, tupleTo, castInt = False):
    return (
        _mapVal(progress, tupleFrom[0], tupleTo[0], castInt),
        _mapVal(progress, tupleFrom[1], tupleTo[1], castInt)
    )

def _mapTuple3(progress, tupleFrom, tupleTo, castInt = False):
    return (
        _mapVal(progress, tupleFrom[0], tupleTo[0], castInt),
        _mapVal(progress, tupleFrom[1], tupleTo[1], castInt),
        _mapVal(progress, tupleFrom[2], tupleTo[2], castInt)
    )

class Visualizer:
    def __init__(self, network, displaySize = (1280,720)):
        self.displaySize = displaySize
        pygame.init()
        self.window = pygame.display.set_mode(displaySize)
        self.visNodes = {}
        self.needsRedraw = True
        self.network = network
        self._blockScoreMax = 0
        self._blockScoreDistLow = 5
        
        # self.pings contains dicts in the following form:
        # {
        #   visNodeFrom: [visnode],
        #   visNodeTo: [visnode],
        #   progress: [0 to 1]
        # }
        self.pings = []

        self.network.callbackChannel.add(
            self.listenConnect,
            'connect'
        )

        self.network.callbackChannel.add(
            self.listenDisconnect,
            'disconnect'
        )

        self._addNodePos = [75,75]

    def listenConnect(self, data):
        self.addNode(data['node'])

    def listenDisconnect(self, data):
        self.removeNode(data['node'])

    def listenSendTransaction(self, data):
        self.ping(
            data['node'],
            self.network.findNode(data['destination']),
            COLOR_SEND_TRANSACTION
        )

    def listenNewBlock(self, data):
        blockScore = data['node'].block.calculateScore()

        self._blockScoreMax = max(
            self._blockScoreMax,    
            blockScore
        )

        for node in self.visNodes.keys():
            self.visNodes[node]['color'] = _mapTuple3(
                (
                    self._blockScoreDistLow - (
                        self._blockScoreMax -
                        node.block.calculateScore()
                    )
                ) / self._blockScoreDistLow,
                COLOR_NODE_BLOCK_HIGH,
                COLOR_NODE_BLOCK_LOW
            )
            
    # only adds the node to an internal dict, does not draw
    def addNode(self, node, x = None, y = None):
        if x is None and y is None:
            self._addNodePos[0] += 125
            if self._addNodePos[0] >= self.displaySize[0]:
                self._addNodePos[0] = 125
                self._addNodePos[1] += 125
            x = self._addNodePos[0]
            y = self._addNodePos[1]

        self.visNodes[node] = {
            'pos': (x, y),
            'color': COLOR_NODE_BLOCK_HIGH
        }
        
        node.callbackChannel.add(
            self.listenNewBlock,    
            'newBlock'
        )

        node.callbackChannel.add(
            self.listenSendTransaction,    
            'sendTransaction'
        )

        self.needsRedraw = True

    # only removes the node from an internal dict, does not redraw
    def removeNode(self, node):
        del visNodes[node]
        self.needsRedraw = True

    # highlights a connection from one node to another
    def ping(self, nodeFrom, nodeTo, color = COLOR_PING):
        visNodeFrom = self.visNodes[nodeFrom]
        visNodeTo = self.visNodes[nodeTo]

        self.pings.append({
            'visNodeFrom': visNodeFrom,
            'visNodeTo': visNodeTo,
            'progress': 0,
            'color': color
        })

    def drawPings(self):
        for ping in self.pings:
            visNodeFrom = ping['visNodeFrom']
            visNodeTo = ping['visNodeTo']

            # Draw connecting line
            pygame.draw.line(
                self.window,
                _mapTuple3(
                    ping['progress'],
                    COLOR_LINE_ACTIVE,
                    COLOR_LINE_NORMAL
                ),
                visNodeFrom['pos'],
                visNodeTo['pos'],
                2 # width
            )

            # Ping circle
            pygame.draw.circle(
                self.window,
                ping['color'],
                _mapTuple2(
                    ping['progress'],
                    visNodeFrom['pos'],
                    visNodeTo['pos'],
                    True # castInt
                ),
                4 # radius
            )
            
            # # Node from circle
            # pygame.draw.circle(
            #     self.window,
            #     _mapTuple3(
            #         ping['progress'],
            #         COLOR_NODE_ACTIVE,
            #         visNodeFrom['color']
            #     ),
            #     visNodeFrom['pos'],
            #     8 # radius
            # )

            # # Node to circle
            # pygame.draw.circle(
            #     self.window,
            #     _mapTuple3(
            #         ping['progress'],
            #         COLOR_NODE_ACTIVE,
            #         visNodeTo['color']
            #     ),
            #     visNodeTo['pos'],
            #     8 # radius
            # )

            ping['progress'] += 0.01
            if ping['progress'] >= 1:
                self.pings.remove(ping)

            self.needsRedraw = True

    def draw(self):
        if self.pings:
            self.needsRedraw = True

        if not self.needsRedraw:
            return

        self.window.fill(COLOR_BG) # Set BG to white

        # This could probably be made more efficient; some lines may be drawn twice
        nodes = self.visNodes.keys()
        for node in nodes:
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    continue

                visNode1 = self.visNodes[node]
                visNode2 = self.visNodes[neighbor]
                pygame.draw.line(
                    self.window,
                    COLOR_LINE_NORMAL,
                    visNode1['pos'],
                    visNode2['pos']
                )

        # Draw circles after so that lines do not interfere
        for node in nodes:
            visNode = self.visNodes[node]
            pygame.draw.circle(
                self.window,
                visNode['color'],
                visNode['pos'],
                8 # radius
            )

        self.needsRedraw = False
        self.drawPings()

        pygame.display.update()

    def tick(self):
        self.draw()