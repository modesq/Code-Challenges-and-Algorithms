# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    

class Linkedlist:
     
    def __init__(self):
        self.head=None
        self.links = []
        self.length = 0

    def append(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_node
            self.length+=1
            self.links.append(value)

        else: 
            currentNode= self.head
            
            while currentNode.next != None:
                currentNode = currentNode.next 

            currentNode.next = new_node
            self.links.append(value)
            self.length+=1
            
    def toArray(self):
        result = []
        currentNode = self.head
        while currentNode != None:
                result.append(currentNode.value)
                currentNode = currentNode.next # None
        return result
        
    def removeByNode(self, node : Node):
         
        next_node = node.next
         
        node.value  = next_node.value
        node.next = next_node.next
        
    def getNode(self,val):
        currentNode = self.head
        wantedNode = None
        while (currentNode.value != val):
            currentNode = currentNode.next
        wantedNode = currentNode
        return wantedNode
