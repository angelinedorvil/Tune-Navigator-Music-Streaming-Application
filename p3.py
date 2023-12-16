from timeit import default_timer as timer
import sys

# Angeline Dorvil
# Music Streaming Application
#

# This class is used to store one node in the linked list.
# A node has a song's title and three pointers to other nodes.
class Song:
    def __init__(self, title):
        self.title = title
        self.nextInOrigOrder = None # pointer to next song on list when initial list is created
        self.prevInPlaylist  = None # pointer to previous song in the user's playlist
        self.nextInPlaylist  = None # pointer to next song in the user's playlist

    # methods used to set the pointers
    def setNextInOrigOrder (self, node):
        self.nextInOrigOrder = node

    def setPrevInPlaylist (self, node):
        self.prevInPlaylist = node

    def setNextInPlaylist (self, node):
        self.nextInPlaylist = node

    # returns the song title of the node    
    def getSongTitle(self):
        return(self.title)

    # returns the next node (in the original order)
    def getNextInOrigOrder(self):
        return(self.nextInOrigOrder)

    # returns the previous node (in the playlist order)
    def getPrevInPlaylist(self):
        return(self.prevInPlaylist)

    # returns the next node (in the playlist order)
    def getNextInPlaylist(self):
       return(self.nextInPlaylist)



# Main Program
# Initializing pointers that will be used to create and traverse the linked list
headNodeOrig = None
headNodePlaylist = None
tailNodePlaylist = None
currentNode = None

# TO DO: write your code below this line.
import time
start = time.time()

#command line arguments
if len(sys.argv) != 4:
 raise ValueError('Please provide three file names.')

inputSongs = sys.argv[1]
inputPlaylist = sys.argv[2]
inputCommands = sys.argv[3]

print("\nThe file that has all the songs is:", inputSongs)
print("\nThe file that has the user's playlist is:", inputPlaylist)
print("\nThe file that has the user's commands is:", inputCommands)

#Reading from files
with open(inputSongs, "r") as f:
    songTitle = f.readline().rstrip() #You can now add this song title to a new node in the linked list.    
    headNodeOrig = Song(songTitle)
    currentNode = headNodeOrig    

    songTitle = f.readline().rstrip()

    while songTitle:
        newNode = Song(songTitle)
        
        currentNode.setNextInOrigOrder(newNode)

        currentNode = newNode
        songTitle = f.readline().rstrip()

    currentNode.setNextInOrigOrder(None)

f.close()

# Playlist creation
with open(inputPlaylist, "r") as p:
    songPlaylist = p.readline().rstrip()
    currentNode = headNodeOrig

    # Search for the first song in the playlist within the original list
    while currentNode is not None and currentNode.getSongTitle() != songPlaylist:
        currentNode = currentNode.getNextInOrigOrder()

    headNodePlaylist = currentNode
    currentNode.setPrevInPlaylist(None)
    tailNodePlaylist = currentNode
    
    songPlaylist = p.readline().rstrip()

    while songPlaylist:
        currentNode = headNodeOrig

        # Find the corresponding node in the original list
        while currentNode is not None and currentNode.getSongTitle() != songPlaylist:
            currentNode = currentNode.getNextInOrigOrder()

        currentNode.setPrevInPlaylist(tailNodePlaylist)  # Set previous node in the playlist to the current tail
        tailNodePlaylist.setNextInPlaylist(currentNode)  # Set next node in the playlist for the current tail
        tailNodePlaylist = currentNode  # Update tail node

        songPlaylist = p.readline().rstrip()

    tailNodePlaylist.setNextInPlaylist(None)

p.close()

print("\n")

# Reading user's commands
with open(inputCommands, "r") as m:
    userCommands = m.readline().rstrip()

    while userCommands:
        if userCommands == "Beginning":
            currentNode = headNodePlaylist
            print(userCommands)
            
        elif userCommands == "End":
            currentNode = tailNodePlaylist
            print(userCommands)
            
        elif userCommands == "Play":
                print("Now Playing:", currentNode.getSongTitle())
                
        elif userCommands == "Previous":
                currentNode = currentNode.getPrevInPlaylist()
                print(userCommands)

        elif userCommands == "Next":
                currentNode = currentNode.getNextInPlaylist()
                print(userCommands)

        userCommands = m.readline().rstrip()

m.close()

end = time.time()
print("\nTotal Time of Program: {0} milliseconds\n" .format(end - start))
