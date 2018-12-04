#!/usr/bin/python3

import pygame
import random

COLOR_NODE_NORMAL = (  0,   0, 128)
COLOR_NODE_ACTIVE = (  0, 255,   0)
COLOR_LINE_NORMAL = (  0,   0,   0)
COLOR_LINE_ACTIVE = (255,   0,   0)
COLOR_BG          = (255, 255, 255)
COLOR_PING        = (255,   0,   0)
COLOR_SEND_TRANSACTION = (255,   0, 255)

def _mapVal(progress, valFrom, valTo, castInt = False):
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

    # only adds the node to an internal dict, does not draw
    def addNode(self, node, x = None, y = None):
        self.visNodes[node] = {
            'pos': (
                x or random.randint(10, self.displaySize[0] - 10),
                y or random.randint(10, self.displaySize[1] - 10) 
            )
        }
        
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

            # Node from circle
            pygame.draw.circle(
                self.window,
                _mapTuple3(
                    ping['progress'],
                    COLOR_NODE_ACTIVE,
                    COLOR_NODE_NORMAL
                ),
                visNodeFrom['pos'],
                8 # radius
            )

            # Node to circle
            pygame.draw.circle(
                self.window,
                _mapTuple3(
                    ping['progress'],
                    COLOR_NODE_ACTIVE,
                    COLOR_NODE_NORMAL
                ),
                visNodeTo['pos'],
                8 # radius
            )

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
            for neighbor in node.neighbors.keys():
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
                COLOR_NODE_NORMAL,
                visNode['pos'],
                8 # radius
            )

        self.needsRedraw = False
        self.drawPings()

        pygame.display.update()

    def tick(self):
        self.draw()