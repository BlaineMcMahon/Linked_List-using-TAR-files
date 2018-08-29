import threading
import tarfile,os
import sys
import time
import csv
#---------------------------L I N K E D ___ L I S T ___ D A T A S T R U C T U R E-----------------------------------

class node():


	#Constructor Function to define the Node Object
	def __init__(self,data=None):
		self.data = data
		self.nextNode = None #Next pointer that points to the next node in list which is NULL when there is no nodes


class linked_list():

	#Constructor function to define the linked list object  
	def __init__(self):
		
		self.head = node()  #Head of the linked list always points to the first element in list
		self.counter = 0  


	def insert(self,data):

		self.counter += 1

		newNode= node(data)   #Create a new node to insert the data into 

		#If the list is empty
		if not self.head:  #if the linked list is empty
			self.head = newNode

		#The list isn't empty 
		else:
			newNode.nextNode = self.head
			self.head = newNode	

	def traverselist(self):

		elems = []
		current_node = self.head
		while current_node.nextNode != None:
			current_node = current_node.nextNode
			elems.append(current_node.data)
		print(elems)

		return elems


	def length_of_list(self):

		print(self.counter)
		return self.counter 

#============================== F I L E __ I/O __ F U N C T I O N =====================================

#---------------------------E X T R A C T __ BBT N U M B E R -----------------------------------
def opentarfile(bbt_info):
	#Loop that iterates through the first file to find the BBT number
	for member in bbt_info:
		f=tar.extractfile(member)
		
		content= f.read()
		stuff = content[0:45]
		
		return stuff
		sys.exit(1)


#---------------------------T O ___ C S V -----------------------------------

def tocsv(contents):
	with open('testThree.csv','w') as fp:
		csv_writer = csv.writer(fp,delimiter = ',')
		csv_writer.writerows([contents])



#----------------------------C H U N K S -------------------------------------
def chunks(files,n):
	for i in range(0, len(files), n):
		yield files[i:i+ n]
		



#================================M A I N =======================================


linked_list_BBT = linked_list()  #Create linked list object 


os.chdir('Your Directory Here')  #Change to directory tar files are located 


Files = os.listdir('Your Directory Here') #Store files in directory in list

print(Files)




def function(files=[]):  #function to feed to threader 




#function to read files contents 
	def opentarfile(apple):
		
		for member in apple:
			f=tar.extractfile(member)
			content= f.read()
			stuff = content[:45]  #Only store first 45 characters 
			return stuff
			sys.exit(1)


#Arbi	
	listTest=[]

	for file in files:
		
		tar = tarfile.open(str(file)) #create object of tarfile 
		apple = tar.getmembers()   #get first file in tar file 
		
		listTest.append(opentarfile(apple))
		print(file, opentarfile(apple))  #for testing purposes 
		
		linked_list_BBT.insert('(%s %s)' % (opentarfile(apple),file))  #insert the name and file contents in linked list 



n=4  #amount to chunk list 


chunkedList=list(chunks(Files,n))
print(chunkedList)

#Create the threads 
for sublists in chunkedList:
	t = threading.Thread(target=function,name='thread{}'.format(sublists),args=(sublists,))
	t.start()


time.sleep(300)

#Storing linked list contents in a regular list to pass to the CSV function 
list_to_csv = linked_list_BBT.traverselist()


#convert information to CSV file 
tocsv(list_to_csv)
