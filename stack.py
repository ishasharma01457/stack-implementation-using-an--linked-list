class Node:
	
	
	def __init__(self,data):
		self.data = data
		self.link = None
	
class Stack:
	
	
	def __init__(self):
		self.top = None
	
	
	def isempty(self):
		if self.top == None:
			return True
		else:
			return False
	
	
	def push(self,data):
		
		if self.top == None:
			self.top=Node(data)
			
		else:
			newnode = Node(data)
			newnode.link = self.top
			self.top = newnode
	
	
	def pop(self):
		
		if self.isempty():
			return None
			
		else:
			
			poppednode = self.top
			self.top = self.top.link
			poppednode.link = None
			return poppednode.data
	
	
	def peek(self):
		
		if self.isempty():
			return None
			
		else:
			return self.top.data
		
	def display(self):
		
		iternode = self.top
		if self.isempty():
			print(" Underflow")
		
		else:
			
			while(iternode != None):
			
				print(iternode.data,"->",end = " ")
				iternode = iternode.link
			return
		
Stacklist = Stack()

Stacklist.push(12)
Stacklist.push(26)
Stacklist.push(37)
Stacklist.push(49)


Stacklist.display()


print("\nTop element is ",Stacklist.peek())


Stacklist.pop()
Stacklist.pop()


Stacklist.display()


print("\nTop element is ", Stacklist.peek())

