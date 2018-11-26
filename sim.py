import random

from random import randint
class Node:
    def __init__(self, reliability=0.00, id=-1, zone=1):                #Initializer
        self.id = id  
        self.reliability = reliability
        self.zone = zone
        self.neighbors = []
        self.sNf = {}
        self.flag = 0


    def sendMsg(self, recNode):#Get Failure/Success
        
        if recNode.flag > 0:
            return 1
        
        rand = random.random()
        
        if rand > recNode.reliability:
            self.sNf[recNode.id][2] = self.sNf[recNode.id][2] + 1
            return 0
            print("hi")
        else:
            recNode.flag = 1
            for neighbor in recNode.neighbors:
                recNode.sendMsg(neighbor)
                self.sNf[recNode.id][1] = self.sNf[recNode.id][1] + 1
            return 1
        
                
       
    

        



        
        
if __name__ == "__main__":
    allNodes = []
    amt_of_neighbors = 16
    
    for i in range(1000):
        node = Node(reliability = 0.90, id = i)                         #Creates Nodes 
        allNodes.append(node)
        
            
    for node in allNodes:                                               #Prints Node Ids and Reliabilities 
        print(str(node.reliability) + " | " + str(node.id))


    for node in allNodes:                                               #Adds Neighbors To Nodes
        for n in range(amt_of_neighbors):
            node.neighbors.append(allNodes[randint(0,999)])

    

    #for node in allNodes:                                               #Prints Node Ids and Their Neighbors.
     #   print("NODE: " + str(node.id))
      #  print("NEIGHBORS:")
       # for n in node.neighbors: # neighbors in each node
             
        #    print(str(n.id)) # print the node id
    



   # testingNode = allNodes[1]       
    
    #print("Node: " + str(allNodes[1].id) + " Reliability " + str(allNodes[1].reliability))

    #for neighbor in testingNode.neighbors:                              #Gets Multiples Responses
     #  a = testingNode.sendMsg(neighbor)
      # print(str(a))




       

    for node in allNodes:
        for neighbor in node.neighbors:                                                                                                                                                        #node.sNf = {"id": node.id ,"successes": 0, "failures":0} # save data about reliability estimate, successes, failures
            node.sNf[neighbor.id] = [0,0,0]     #####
            #print(str(node.sNf))




        
    NODE = allNodes[100]



    
   # for neighbor in NODE.neighbors:
      #  NODE.sendMsg(neighbor)
      #  NODE.sNf[neighbor.id][0] = NODE.sNf[neighbor.id][1]/(NODE.sNf[neighbor.id][1] + NODE.sNf[neighbor.id][2])


        

    #for node in allNodes:
      #  print(str(node.sNf))

    print(str(allNodes[100].sNf))            


        

    #fail = TEST_NODE.sNf[TEST_NODE.id][2] + 1337
    #suc = TEST_NODE.sNf[TEST_NODE.id][1] + 420
    #reli = TEST_NODE.sNf[TEST_NODE.id][0] + 0.5

    
    #TEST_NODE.sNf[TEST_NODE.id] = [reli, suc, fail]

    
    #print(str(TEST_NODE.sNf))
